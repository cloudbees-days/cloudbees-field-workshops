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
"""Delete command for the Tag Manager - Tag Bindings CLI."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.resource_manager import tags
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.resource_manager import operations
from googlecloudsdk.command_lib.resource_manager import tag_arguments as arguments
from googlecloudsdk.command_lib.resource_manager import tag_utils

from six.moves.urllib.parse import quote


@base.Hidden
@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Delete(base.Command):
  """Deletes a TagBinding.

    Deletes a TagBinding given the TagValue and the parent resource that the
    TagValue is attached to. The parent must be given as the full resource name.
    See: https://cloud.google.com/apis/design/resource_names#full_resource_name.
    The TagValue can be represented with its numeric id or
    its namespaced name of {org_id}/{tag_key_short_name}.
  """

  detailed_help = {
      "EXAMPLES":
          """
          To delete a TagBinding between 'tagValue/111' and Project with
          name '//cloudresourcemanager.googleapis.com/projects/1234' run:

            $ {command} --tag-value=tagValue/123 --parent=//cloudresourcemanager.googleapis.com/projects/1234

          To delete a binding between TagValue test under TagKey 'env' that
          lives under 'organizations/789' and Project with name '//cloudresourcemanager.googleapis.com/projects/1234' run:

            $ {command} --tag-value=789/env/test --parent=//cloudresourcemanager.googleapis.com/projects/1234
          """
  }

  @staticmethod
  def Args(parser):
    arguments.AddTagValueArgToParser(parser)
    arguments.AddParentArgToParser(
        parser,
        message="Full resource name of the resource attached to the tagValue.")
    arguments.AddAsyncArgToParser(parser)

  def Run(self, args):
    service = tags.TagBindingsService()
    messages = tags.TagMessages()

    if args.tag_value.find("tagValues/") == 0:
      tag_value = args.tag_value
    else:
      tag_value = tag_utils.GetTagValueFromNamespacedName(
          args.tag_value).name

    binding_name = "/".join(
        ["tagBindings", quote(args.parent, safe=""), tag_value])
    del_req = messages.CloudresourcemanagerTagBindingsDeleteRequest(
        name=binding_name)

    op = service.Delete(del_req)

    if args.async_ or op.done:
      return op
    else:
      return operations.WaitForOperation(
          op,
          "Waiting for TagBinding for resource [{}] and tag value [{}] to be "
          "deleted with [{}]".format(args.parent, args.tag_value, op.name),
          service=service)
