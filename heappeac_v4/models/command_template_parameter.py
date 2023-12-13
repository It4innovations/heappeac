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

class CommandTemplateParameter(object):
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
        'identifier': 'str',
        'query': 'str',
        'description': 'str',
        'is_visible': 'bool',
        'command_template_id': 'int',
        'command_template': 'CommandTemplate'
    }

    attribute_map = {
        'id': 'Id',
        'identifier': 'Identifier',
        'query': 'Query',
        'description': 'Description',
        'is_visible': 'IsVisible',
        'command_template_id': 'CommandTemplateId',
        'command_template': 'CommandTemplate'
    }

    def __init__(self, id=None, identifier=None, query=None, description=None, is_visible=None, command_template_id=None, command_template=None):  # noqa: E501
        """CommandTemplateParameter - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._identifier = None
        self._query = None
        self._description = None
        self._is_visible = None
        self._command_template_id = None
        self._command_template = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.identifier = identifier
        self.query = query
        self.description = description
        if is_visible is not None:
            self.is_visible = is_visible
        if command_template_id is not None:
            self.command_template_id = command_template_id
        if command_template is not None:
            self.command_template = command_template

    @property
    def id(self):
        """Gets the id of this CommandTemplateParameter.  # noqa: E501


        :return: The id of this CommandTemplateParameter.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CommandTemplateParameter.


        :param id: The id of this CommandTemplateParameter.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def identifier(self):
        """Gets the identifier of this CommandTemplateParameter.  # noqa: E501


        :return: The identifier of this CommandTemplateParameter.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this CommandTemplateParameter.


        :param identifier: The identifier of this CommandTemplateParameter.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def query(self):
        """Gets the query of this CommandTemplateParameter.  # noqa: E501


        :return: The query of this CommandTemplateParameter.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this CommandTemplateParameter.


        :param query: The query of this CommandTemplateParameter.  # noqa: E501
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def description(self):
        """Gets the description of this CommandTemplateParameter.  # noqa: E501


        :return: The description of this CommandTemplateParameter.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CommandTemplateParameter.


        :param description: The description of this CommandTemplateParameter.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def is_visible(self):
        """Gets the is_visible of this CommandTemplateParameter.  # noqa: E501


        :return: The is_visible of this CommandTemplateParameter.  # noqa: E501
        :rtype: bool
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        """Sets the is_visible of this CommandTemplateParameter.


        :param is_visible: The is_visible of this CommandTemplateParameter.  # noqa: E501
        :type: bool
        """

        self._is_visible = is_visible

    @property
    def command_template_id(self):
        """Gets the command_template_id of this CommandTemplateParameter.  # noqa: E501


        :return: The command_template_id of this CommandTemplateParameter.  # noqa: E501
        :rtype: int
        """
        return self._command_template_id

    @command_template_id.setter
    def command_template_id(self, command_template_id):
        """Sets the command_template_id of this CommandTemplateParameter.


        :param command_template_id: The command_template_id of this CommandTemplateParameter.  # noqa: E501
        :type: int
        """

        self._command_template_id = command_template_id

    @property
    def command_template(self):
        """Gets the command_template of this CommandTemplateParameter.  # noqa: E501


        :return: The command_template of this CommandTemplateParameter.  # noqa: E501
        :rtype: CommandTemplate
        """
        return self._command_template

    @command_template.setter
    def command_template(self, command_template):
        """Sets the command_template of this CommandTemplateParameter.


        :param command_template: The command_template of this CommandTemplateParameter.  # noqa: E501
        :type: CommandTemplate
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
        if issubclass(CommandTemplateParameter, dict):
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
        if not isinstance(other, CommandTemplateParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
