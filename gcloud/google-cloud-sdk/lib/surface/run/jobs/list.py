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
"""Command for listing available reivions."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.run import commands
from googlecloudsdk.command_lib.run import connection_context
from googlecloudsdk.command_lib.run import flags
from googlecloudsdk.command_lib.run import pretty_print
from googlecloudsdk.command_lib.run import serverless_operations
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources


def _ActiveStatus(job):
  return '{} / {}'.format(
      job.get('status', {}).get('active', 0),
      job.get('spec', {}).get('parallelism', 0))


def _SucceededStatus(job):
  return '{} / {}'.format(
      job.get('status', {}).get('succeeded', 0),
      job.get('spec', {}).get('completions', 0))


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class List(commands.List):
  """List available revisions."""

  detailed_help = {
      'DESCRIPTION': """
          {description}
          """,
      'EXAMPLES': """
          To list all jobs in all regions:

              $ {command}
         """,
  }

  @classmethod
  def CommonArgs(cls, parser):
    parser.display_info.AddFormat(
        'table('
        '{ready_column},'
        'name:label=JOB:sort=3,'
        'active_status():label=ACTIVE:sort=1:reverse,'
        'succeeded_status():label=COMPLETE,'
        'creation_timestamp.date("%Y-%m-%d %H:%M:%S %Z"):'
        'label=CREATED:sort=2:reverse,'
        'author:label="CREATED BY")'.format(
            ready_column=pretty_print.READY_COLUMN))
    parser.display_info.AddUriFunc(cls._GetResourceUri)
    parser.display_info.AddTransforms({
        'active_status': _ActiveStatus,
        'succeeded_status': _SucceededStatus,
    })

  @classmethod
  def Args(cls, parser):
    cls.CommonArgs(parser)

  def Run(self, args):
    """List available revisions."""
    conn_context = connection_context.GetConnectionContext(
        args,
        flags.Product.RUN,
        self.ReleaseTrack(),
        version_override='v1alpha1')
    namespace_ref = resources.REGISTRY.Parse(
        properties.VALUES.core.project.Get(required=True),
        collection='run.namespaces',
        api_version='v1alpha1')
    with serverless_operations.Connect(conn_context) as client:
      self.SetCompleteApiEndpoint(conn_context.endpoint)
      return commands.SortByName(client.ListJobs(namespace_ref))
