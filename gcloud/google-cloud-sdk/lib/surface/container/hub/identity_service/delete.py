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
"""The command to update Config Management Feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import sys
import textwrap
from googlecloudsdk.api_lib.util import apis as core_apis
from googlecloudsdk.command_lib.container.hub.features import base
from googlecloudsdk.core import exceptions
from googlecloudsdk.core import properties
from googlecloudsdk.core.console import console_io


class Delete(base.UpdateCommand):
  """Remove the Identity Service Feature Spec for the given membership.

  Removes the Identity Service Feature Spec for the given
  membership.

  ## Examples

  To delete an Identity Service configuration for a membership, run:

    $ {command} --membership=CLUSTER_NAME
  """

  FEATURE_NAME = 'identityservice'
  FEATURE_DISPLAY_NAME = 'Identity Service'

  @classmethod
  def Args(cls, parser):
    parser.add_argument(
        '--membership',
        type=str,
        help=textwrap.dedent("""\
            Membership name provided during registration.
            """),
    )

  def Run(self, args):
    # Get Hub memberships (cluster registered with Hub) from GCP Project.
    project = args.project or properties.VALUES.core.project.GetOrFail()
    memberships = base.ListMemberships(project)
    if not memberships:
      raise exceptions.Error('No Memberships available in Hub.')

    # Acquire membership.
    membership = None
    # Prompt user for an existing hub membership if none is provided.
    if not args.membership:
      index = 0
      if len(memberships) > 1:
        index = console_io.PromptChoice(
            options=memberships,
            message=
            'Please specify a membership to delete Identity Service {}:\n')
      membership = memberships[index]
      sys.stderr.write('Selecting membership [{}].\n'
                       .format(membership))
    else:
      membership = args.membership
      if membership not in memberships:
        raise exceptions.Error(
            'Membership {} is not in Hub.'.format(membership))

    # Create new identity service feature spec.
    client = core_apis.GetClientInstance('gkehub', 'v1alpha1')
    msg = client.MESSAGES_MODULE

    # UpdateFeature uses the patch method to update member_configs map, hence
    # there's no need to get the existing feature spec.
    applied_config = msg.IdentityServiceFeatureSpec.MemberConfigsValue.AdditionalProperty(
        key=membership,
        value=msg.MemberConfig())
    m_configs = msg.IdentityServiceFeatureSpec.MemberConfigsValue(
        additionalProperties=[applied_config])

    # Execute update to delete identity service feature spec for membership.
    self.RunCommand(
        'identityservice_feature_spec.member_configs',
        identityserviceFeatureSpec=msg.IdentityServiceFeatureSpec(
            memberConfigs=m_configs))
