# coding: utf-8

"""
    HEAppE Web API

    HEAppE middleware API v4.2.0  # noqa: E501

    OpenAPI spec version: v4.2.0
    Contact: support.heappe@it4i.cz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProjectForTaskExt(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'accounting_string': 'str',
        'command_template': 'CommandTemplateExt'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'accounting_string': 'AccountingString',
        'command_template': 'CommandTemplate'
    }

    def __init__(self, id=None, name=None, description=None, accounting_string=None, command_template=None):  # noqa: E501
        """ProjectForTaskExt - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._accounting_string = None
        self._command_template = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if accounting_string is not None:
            self.accounting_string = accounting_string
        if command_template is not None:
            self.command_template = command_template

    @property
    def id(self):
        """Gets the id of this ProjectForTaskExt.  # noqa: E501


        :return: The id of this ProjectForTaskExt.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectForTaskExt.


        :param id: The id of this ProjectForTaskExt.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProjectForTaskExt.  # noqa: E501


        :return: The name of this ProjectForTaskExt.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectForTaskExt.


        :param name: The name of this ProjectForTaskExt.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProjectForTaskExt.  # noqa: E501


        :return: The description of this ProjectForTaskExt.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectForTaskExt.


        :param description: The description of this ProjectForTaskExt.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def accounting_string(self):
        """Gets the accounting_string of this ProjectForTaskExt.  # noqa: E501


        :return: The accounting_string of this ProjectForTaskExt.  # noqa: E501
        :rtype: str
        """
        return self._accounting_string

    @accounting_string.setter
    def accounting_string(self, accounting_string):
        """Sets the accounting_string of this ProjectForTaskExt.


        :param accounting_string: The accounting_string of this ProjectForTaskExt.  # noqa: E501
        :type: str
        """

        self._accounting_string = accounting_string

    @property
    def command_template(self):
        """Gets the command_template of this ProjectForTaskExt.  # noqa: E501


        :return: The command_template of this ProjectForTaskExt.  # noqa: E501
        :rtype: CommandTemplateExt
        """
        return self._command_template

    @command_template.setter
    def command_template(self, command_template):
        """Sets the command_template of this ProjectForTaskExt.


        :param command_template: The command_template of this ProjectForTaskExt.  # noqa: E501
        :type: CommandTemplateExt
        """

        self._command_template = command_template

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ProjectForTaskExt, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProjectForTaskExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
