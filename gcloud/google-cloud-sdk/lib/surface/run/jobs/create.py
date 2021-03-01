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
"""Deploy a container to Cloud Run that will run to completion."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.run import config_changes
from googlecloudsdk.command_lib.run import connection_context
from googlecloudsdk.command_lib.run import flags
from googlecloudsdk.command_lib.run import messages_util
from googlecloudsdk.command_lib.run import pretty_print
from googlecloudsdk.command_lib.run import resource_args
from googlecloudsdk.command_lib.run import serverless_operations
from googlecloudsdk.command_lib.run import stages
from googlecloudsdk.command_lib.util.concepts import concept_parsers
from googlecloudsdk.command_lib.util.concepts import presentation_specs
from googlecloudsdk.core.console import progress_tracker


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Deploy(base.Command):
  """Deploy a container to Cloud Run that will run to completion."""

  detailed_help = {
      'DESCRIPTION':
          """\
          Deploys a new job to Google Cloud Run.
          """,
      'EXAMPLES':
          """\
          To deploy a new job `my-backend` on Cloud Run:

              $ {command} my-backend --image=gcr.io/my/image

          You may also omit the job name. Then a prompt will be displayed
          with a suggested default value:

              $ {command} --image=gcr.io/my/image
          """,
  }

  @staticmethod
  def CommonArgs(parser):
    # Flags not specific to any platform
    service_presentation = presentation_specs.ResourcePresentationSpec(
        'JOB',
        resource_args.GetJobResourceSpec(prompt=True),
        'Job to create.',
        required=True,
        prefixes=False)
    flags.AddImageArg(parser)
    flags.AddLabelsFlag(parser)
    flags.AddParallelismFlag(parser)
    flags.AddCompletionsFlag(parser)
    flags.AddMaxAttemptsFlag(parser)
    flags.AddServiceAccountFlag(parser)
    flags.AddSetEnvVarsFlag(parser)
    flags.AddMemoryFlag(parser)
    flags.AddCpuFlag(parser, managed_only=True)
    flags.AddCommandFlag(parser)
    flags.AddArgsFlag(parser)
    flags.AddClientNameAndVersionFlags(parser)

    polling_group = parser.add_mutually_exclusive_group()
    flags.AddAsyncFlag(polling_group)
    flags.AddWaitForCompletionFlag(polling_group)

    concept_parsers.ConceptParser([service_presentation]).AddToParser(parser)
    # No output by default, can be overridden by --format
    parser.display_info.AddFormat('none')

  @staticmethod
  def Args(parser):
    Deploy.CommonArgs(parser)

  def Run(self, args):
    """Deploy a container to Cloud Run."""
    job_ref = args.CONCEPTS.job.Parse()
    flags.ValidateResource(job_ref)

    conn_context = connection_context.GetConnectionContext(
        args,
        flags.Product.RUN,
        self.ReleaseTrack(),
        version_override='v1alpha1')
    changes = flags.GetConfigurationChanges(args)
    changes.append(
        config_changes.SetLaunchStageAnnotationChange(self.ReleaseTrack()))

    with serverless_operations.Connect(conn_context) as operations:
      pretty_print.Info(
          messages_util.GetStartDeployMessage(conn_context, job_ref, 'job'))
      header_msg = 'Creating and {} job...'.format(
          'running' if args.wait_for_completion else 'starting')
      with progress_tracker.StagedProgressTracker(
          header_msg,
          stages.JobStages(include_completion=args.wait_for_completion),
          failure_message='Job failed',
          suppress_output=args.async_) as tracker:
        job = operations.CreateJob(
            job_ref,
            changes,
            args.wait_for_completion,
            tracker,
            asyn=args.async_)

      if args.async_:
        pretty_print.Success('Job [{{bold}}{job}{{reset}}] is being created '
                             'asynchronously.'.format(job=job.name))
      else:
        job = operations.GetJob(job_ref)
        pretty_print.Success(
            'Job [{{bold}}{job}{{reset}}] has successfully '
            '{operation}.'.format(
                job=job.name,
                operation=('completed'
                           if args.wait_for_completion else 'started running')))
      return job
