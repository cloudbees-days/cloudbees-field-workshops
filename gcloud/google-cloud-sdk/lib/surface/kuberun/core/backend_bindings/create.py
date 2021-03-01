# -*- coding: utf-8 -*- #
# Copyright 2021 Google LLC. All Rights Reserved.
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
"""Create a backend binding for a KubeRun service."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import json

from googlecloudsdk.api_lib.kuberun import backendbinding
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.kuberun import flags
from googlecloudsdk.command_lib.kuberun import kuberun_command
from googlecloudsdk.core import exceptions

_DETAILED_HELP = {
    'EXAMPLES':
        """
        To bind KubeRun service `myservice` in the default namespace as a backend
        to Compute Engine backend service `mybackendservice` with a maximum
        limit of 200 requests per second that the service can handle, run

            $ {command} --service=myservice --backend-service=mybackendservice --max-rate=200
        """,
}


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Create(kuberun_command.KubeRunStreamingCommandWithResult):
  """Creates a backend binding."""

  detailed_help = _DETAILED_HELP
  flags = [
      flags.NamespaceFlag(),
      flags.ClusterConnectionFlags(),
      flags.MaxRateFlag(True),
  ]

  @classmethod
  def Args(cls, parser):
    super(Create, cls).Args(parser)
    parser.add_argument(
        '--service',
        help='KubeRun service to use as the backend.',
        required=True)
    parser.add_argument(
        '--backend-service',
        help='Compute Engine backend service to bind the KubeRun service to.',
        required=True)
    parser.display_info.AddFormat("""table(
        name:label=NAME,
        service:label=SERVICE,
        ready:label=READY)""")

  def BuildKubeRunArgs(self, args):
    return [
        '--service', args.service, '--backend-service', args.backend_service,
    ] + super(Create, self).BuildKubeRunArgs(args)

  def Command(self):
    return ['core', 'backend-bindings', 'create']

  def FormatOutput(self, out, args):
    if out:
      return backendbinding.BackendBinding(json.loads(out))
    else:
      raise exceptions.Error(
          'Could not create backend binding [{}] for service [{}]'.format(
              args.domain, args.service))
