# -*- coding: utf-8 -*- #
# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Scan a container image using the On-Demand Scanning API."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import json

from googlecloudsdk.api_lib.ondemandscanning import util as api_util
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.artifacts import flags
from googlecloudsdk.command_lib.artifacts import ondemandscanning_util as ods_util
from googlecloudsdk.command_lib.util.anthos import binary_operations
from googlecloudsdk.core import exceptions as core_exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core.console import progress_tracker
import six

# Extract stage messages to constants for convenience.
SCAN_MESSAGE = 'Scanning container image'
EXTRACT_MESSAGE = ('Locally extracting packages and versions from {} '
                   'container image')
RPC_MESSAGE = 'Remotely initiating analysis of packages and versions'
POLL_MESSAGE = 'Waiting for analysis operation to complete'


class ExtractionFailedError(core_exceptions.Error):
  """Raised when extraction fails."""
  pass


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class Scan(base.Command):
  """Perform a vulnerability scan on a container image.

  You can scan a container image in a Google Cloud registry (Artifact Registry
  or Container Registry), or a local container image.

  Reference an image by tag or digest using any of the formats:

    Artifact Registry:
      LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE[:tag]
      LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE@sha256:digest

    Container Registry:
      [LOCATION.]gcr.io/PROJECT-ID/REPOSITORY-ID/IMAGE[:tag]
      [LOCATION.]gcr.io/PROJECT-ID/REPOSITORY-ID/IMAGE@sha256:digest

    Local:
      IMAGE[:tag]
  """

  detailed_help = {
      'DESCRIPTION':
          '{description}',
      'EXAMPLES':
          """\
    Start a scan of a container image stored in Artifact Registry:

        $ {command} us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz --remote

    Start a scan of a container image stored in the Container Registry, and perform the analysis in Europe:

        $ {command} eu.gcr.io/my-project/my-repository/my-image:latest --remote --location=europe

    Start a scan of a container image stored locally, and perform the analysis in Asia:

        $ {command} ubuntu:latest --location=asia
    """
  }

  @staticmethod
  def Args(parser):
    flags.GetResourceURIArg().AddToParser(parser)
    flags.GetRemoteFlag().AddToParser(parser)
    flags.GetOnDemandScanningFakeExtractionFlag().AddToParser(parser)
    flags.GetOnDemandScanningLocationFlag().AddToParser(parser)
    base.ASYNC_FLAG.AddToParser(parser)

  def Run(self, args):
    """Runs local extraction then calls ODS with the results.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Returns:
      AnalyzePackages operation.
    """
    # Create the command wrapper immediately so we can fail fast if necessary.
    cmd = Command()

    # TODO(b/173619679): Validate RESOURCE_URI argument.

    # Dynamically construct the stages based on the --async flag; when
    # --async=true, we do not need a separate poll stage.
    stages = [
        progress_tracker.Stage(
            EXTRACT_MESSAGE.format('remote' if args.remote else 'local'),
            key='extract'),
        progress_tracker.Stage(RPC_MESSAGE, key='rpc')
    ]
    if not args.async_:
      stages += [progress_tracker.Stage(POLL_MESSAGE, key='poll')]

    messages = api_util.GetMessages()
    with progress_tracker.StagedProgressTracker(
        SCAN_MESSAGE, stages=stages) as tracker:
      # Stage 1) Extract.
      tracker.StartStage('extract')
      operation_result = cmd(
          resource_uri=args.RESOURCE_URI,
          remote=args.remote,
          fake_extraction=args.fake_extraction,
      )
      if operation_result.exit_code:
        tracker.FailStage('extract',
                          ExtractionFailedError(operation_result.stderr))
        return

      # Parse stdout for the JSON-ified PackageData protos.
      pkgs = []
      for pkg in json.loads(operation_result.stdout):
        pkgs += [
            messages.PackageData(
                package=pkg['package'],
                version=pkg['version'],
                cpeUri=pkg['cpe_uri'],
            )
        ]
      tracker.CompleteStage('extract')

      # Stage 2) Make the RPC to the On-Demand Scanning API.
      tracker.StartStage('rpc')
      op = api_util.AnalyzePackages(
          properties.VALUES.core.project.Get(required=True), args.location,
          args.RESOURCE_URI, pkgs)
      tracker.CompleteStage('rpc')

      # Stage 3) Poll the operation if requested.
      response = None
      if not args.async_:
        tracker.StartStage('poll')
        tracker.UpdateStage('poll', '[{}]'.format(op.name))
        response = ods_util.WaitForOperation(op)
        tracker.CompleteStage('poll')

    if args.async_:
      log.status.Print('Check operation [{}] for status.'.format(op.name))
      return op
    return response


class Command(binary_operations.BinaryBackedOperation):
  """Wrapper for call to the Go binary."""

  def __init__(self, **kwargs):
    super(Command, self).__init__(binary='local-extract', **kwargs)

  def _ParseArgsForCommand(self, resource_uri, remote, fake_extraction,
                           **kwargs):
    return [
        '--resource_uri=' + resource_uri,
        '--remote=' + six.text_type(remote),
        '--provide_fake_results=' + six.text_type(fake_extraction),
    ]
