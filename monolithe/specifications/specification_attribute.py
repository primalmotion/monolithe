# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import json
import pkgutil

from copy import deepcopy

from monolithe.lib import SDKUtils


class SpecificationAttribute(object):
    """ Define an attribute of an object

    """
    def __init__(self, rest_name, specification=None, data=None):
        """ Define an attribute

            Example:
                rest_name: associatedGatewayID
                local_name: associated_gateway_id
                local_type: str
        """
        # Main attributes
        self.description = None
        self._rest_name = None
        self.local_name = None
        self.local_type = None

        # Other attributes
        self.channel = None
        self.allowed_chars = None
        self.allowed_choices = None
        self.autogenerated = False
        self.availability = None
        self.creation_only = False
        self.default_order = False
        self.default_value = None
        self.deprecated = False
        self.filterable = True
        self.format = "free"
        self.max_length = None
        self.max_value = None
        self.min_length = None
        self.min_value = None
        self.orderable = True
        self.read_only = False
        self.required = False
        self.unique = False
        self.unique_scope = None
        self._type = None
        self.exposed = True
        self.transient = False

        self.specification = specification
        self.rest_name = rest_name

        # Load information from data
        if data:
            self.from_dict(data)

    @property
    def type(self):
        """
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        """
        self._type = SDKUtils.massage_type_name(type_name=value)
        self.local_type = SDKUtils.get_python_type_name(type_name=value)

    @property
    def rest_name(self):
        """
        """
        return self._rest_name

    @rest_name.setter
    def rest_name(self, value):
        """
        """
        self._rest_name = value
        if self.specification and self.specification.monolithe_config:
            self.local_name = SDKUtils.get_python_name(self.specification.monolithe_config.map_attribute(self.specification.rest_name, value))
        else:
            self.local_name = SDKUtils.get_python_name(value)

    def from_dict(self, data):
        """

        """
        try:
            # mandatory characteristics
            self.description = data["description"]
            self.type = data["type"]

            # optional characteristics
            self.allowed_chars = data["allowed_chars"] if "allowed_chars" in data else None
            self.allowed_choices = data["allowed_choices"] if "allowed_choices" in data else None
            self.autogenerated = data["autogenerated"] if "autogenerated" in data else False
            self.channel = data["channel"] if "channel" in data else None
            self.creation_only = data["creation_only"] if "creation_only" in data else False
            self.default_order = data["default_order"] if "default_order" in data else False
            self.default_value = data["default_value"] if "default_value" in data else None
            self.deprecated = data["deprecated"] if "deprecated" in data else False
            self.exposed = data["exposed"] if "exposed" in data else True
            self.filterable = data["filterable"] if "filterable" in data else True
            self.format = data["format"] if "format" in data else "free"
            self.max_length = data["max_length"] if "max_length" in data else None
            self.max_value = data["max_value"] if "max_value" in data else None
            self.min_length = data["min_length"] if "min_length" in data else None
            self.min_value = data["min_value"] if "min_value" in data else None
            self.orderable = data["orderable"] if "orderable" in data else True
            self.read_only = data["read_only"] if "read_only" in data else False
            self.required = data["required"] if "required" in data else False
            self.transient = data["transient"] if "transient" in data else False
            self.unique = data["unique"] if "unique" in data else False
            self.unique_scope = data["unique_scope"] if "unique_scope" in data else 'no'

        except Exception as ex:
            raise Exception("Unable to parse attribute %s for specification %s: %s" % (self.name, self.specification.rest_name, ex))

    def to_dict(self):
        """ Transform an attribute to a dict
        """
        data = {}

        # mandatory characteristics
        data["description"] = self.description
        data["type"] = self.type

        # optional characteristics
        if self.allowed_chars:
            data["allowed_chars"] = self.allowed_chars

        if self.allowed_choices:
            data["allowed_choices"] = self.allowed_choices

        if self.autogenerated:
            data["autogenerated"] = self.autogenerated

        if self.channel:
            data["channel"] = self.channel

        if self.creation_only:
            data["creation_only"] = self.creation_only

        if self.default_order:
            data["default_order"] = self.default_order

        if self.default_value:
            data["default_value"] = self.default_value

        if self.deprecated:
            data["deprecated"] = self.deprecated

        if self.exposed:
            data["exposed"] = self.exposed

        if self.filterable:
            data["filterable"] = self.filterable

        if self.format:
            data["format"] = self.format

        if self.max_length:
            data["max_length"] = self.max_length

        if self.max_value:
            data["max_value"] = self.max_value

        if self.min_length:
            data["min_length"] = self.min_length

        if self.min_value:
            data["min_value"] = self.min_value

        if self.orderable:
            data["orderable"] = self.orderable

        if self.read_only:
            data["read_only"] = self.read_only

        if self.required:
            data["required"] = self.required

        if self.transient:
            data["transient"] = self.transient

        if self.unique:
            data["unique"] = self.unique

        if self.unique_scope:
            data["uniqueScope"] = self.unique_scope

        return data
