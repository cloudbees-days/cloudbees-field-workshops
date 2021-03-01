# -*- coding: utf-8 -*- #
# Copyright 2019 Google LLC. All Rights Reserved.
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
"""The command to describe the status of the Identity Service Feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from apitools.base.py import exceptions as apitools_exceptions
from googlecloudsdk.calliope import base as gcloud_base
from googlecloudsdk.command_lib.container.hub.features import base
from googlecloudsdk.command_lib.container.hub.identity_service import state_util
from googlecloudsdk.core import exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core import properties


class Describe(gcloud_base.ListCommand):
  r"""Prints the status of all clusters with Identity Service installed.

  Prints the status of the Identity Service Feature resource in Hub.

  ## Examples

  To describe the status of the Identity Service configuration, run:

    $ {command}

  """

  FEATURE_NAME = 'identityservice'
  FEATURE_DISPLAY_NAME = 'Identity Service'

  @classmethod
  def Args(cls, parser):
    pass

  def Run(self, args):
    # Get Hub memberships (cluster registered with Hub) from GCP Project.
    try:
      project = args.project or properties.VALUES.core.project.GetOrFail()
      memberships = base.ListMemberships(project)
      name = 'projects/{0}/locations/global/features/{1}'.format(
          project, self.FEATURE_NAME)
      response = base.GetFeature(name)
    except apitools_exceptions.HttpUnauthorizedError as e:
      raise exceptions.Error(
          'Not authorized to see Feature {} status from project [{}]. '
          'Underlying error: {}'.format(self.FEATURE_DISPLAY_NAME, project, e))
    except apitools_exceptions.HttpNotFoundError as e:
      raise exceptions.Error(
          '{} Feature for project [{}] is not enabled'.format(
              self.FEATURE_DISPLAY_NAME, project))
    if not memberships:
      log.status.Print('No Memberships available in Hub.')
      return {}

    feature_spec_memberships = state_util.parse_feature_spec_memberships(
        response)
    feature_state_memberships = state_util.parse_feature_state_memberships(
        response)
    # Populate and print out status of memberships.
    ais_status = []
    for name in memberships:
      cluster_in_spec = None
      cluster_in_state = None
      if name in feature_spec_memberships:
        cluster_in_spec = feature_spec_memberships[name]
        if name in feature_state_memberships:
          cluster_in_state = feature_state_memberships[name].value
        cluster_out = state_util.IdentityServiceMembershipState(
            name, cluster_in_spec=cluster_in_spec,
            cluster_in_state=cluster_in_state)
        ais_status.append(cluster_out)
      else:
        ais_status.append({name: 'config not applied'})
    return {'Membership Status for Identity Service': ais_status}
