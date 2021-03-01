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
"""Create command for the Resource Manager - Tag Bindings CLI."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.resource_manager import tags
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.resource_manager import operations
from googlecloudsdk.command_lib.resource_manager import tag_arguments as arguments
from googlecloudsdk.command_lib.resource_manager import tag_utils


@base.Hidden
@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Create(base.Command):
  """Creates a TagBinding resource.

    Creates a TagBinding given the TagValue and the parent cloud resource the
    TagValue will be attached to. The TagValue can be represented with its
    numeric id or its namespaced name of
    organizations/{org_id}/{tag_key_short_name}. The parent resource should be
    represented with its full resource name. See:
    https://cloud.google.com/apis/design/resource_names#full_resource_name.
  """

  detailed_help = {
      "EXAMPLES":
          """
          To create a TagBinding  between tagValues/123 and Project with name
          '//cloudresourcemanager.googleapis.com/projects/1234' run:

            $ {command} --tag-value=tagValues/123 --parent=//cloudresourcemanager.googleapis.com/projects/1234

          To create a TagBinding between TagValue 'test' under TagKey 'env' and
          Project with name '//cloudresourcemanager.googleapis.com/projects/1234' run:

            $ {command} --tag-value=789/env/test --parent=//cloudresourcemanager.googleapis.com/projects/1234
            """
  }

  @staticmethod
  def Args(parser):
    arguments.AddTagValueArgToParser(parser)
    arguments.AddParentArgToParser(
        parser,
        message="Full resource name of the resource to attach to the tagValue.")
    arguments.AddAsyncArgToParser(parser)

  def Run(self, args):
    service = tags.TagBindingsService()
    messages = tags.TagMessages()

    if args.tag_value.find("tagValues/") == 0:
      tag_value = args.tag_value
    else:
      tag_value = tag_utils.GetTagValueFromNamespacedName(
          args.tag_value).name

    tag_binding = messages.TagBinding(
        parent=args.parent, tagValue=tag_value)

    create_req = messages.CloudresourcemanagerTagBindingsCreateRequest(
        tagBinding=tag_binding)

    op = service.Create(create_req)

    if args.async_ or op.done:
      return op
    else:
      return operations.WaitForOperation(
          op,
          "Waiting for TagBinding for parent [{}] and tag value [{}] to be "
          "created with [{}]".format(args.parent, args.tag_value, op.name),
          service=service)
