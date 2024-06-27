# coding: utf-8

"""
    HEAppE Web API

    HEAppE middleware API v4.2.1  # noqa: E501

    OpenAPI spec version: v4.2.1
    Contact: support.heappe@it4i.cz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExtendedCommandTemplateParameterExt(object):
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
        'description': 'str',
        'query': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'identifier': 'Identifier',
        'description': 'Description',
        'query': 'Query'
    }

    def __init__(self, id=None, identifier=None, description=None, query=None):  # noqa: E501
        """ExtendedCommandTemplateParameterExt - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._identifier = None
        self._description = None
        self._query = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if identifier is not None:
            self.identifier = identifier
        if description is not None:
            self.description = description
        if query is not None:
            self.query = query

    @property
    def id(self):
        """Gets the id of this ExtendedCommandTemplateParameterExt.  # noqa: E501


        :return: The id of this ExtendedCommandTemplateParameterExt.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExtendedCommandTemplateParameterExt.


        :param id: The id of this ExtendedCommandTemplateParameterExt.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def identifier(self):
        """Gets the identifier of this ExtendedCommandTemplateParameterExt.  # noqa: E501


        :return: The identifier of this ExtendedCommandTemplateParameterExt.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ExtendedCommandTemplateParameterExt.


        :param identifier: The identifier of this ExtendedCommandTemplateParameterExt.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def description(self):
        """Gets the description of this ExtendedCommandTemplateParameterExt.  # noqa: E501


        :return: The description of this ExtendedCommandTemplateParameterExt.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExtendedCommandTemplateParameterExt.


        :param description: The description of this ExtendedCommandTemplateParameterExt.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def query(self):
        """Gets the query of this ExtendedCommandTemplateParameterExt.  # noqa: E501


        :return: The query of this ExtendedCommandTemplateParameterExt.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this ExtendedCommandTemplateParameterExt.


        :param query: The query of this ExtendedCommandTemplateParameterExt.  # noqa: E501
        :type: str
        """

        self._query = query

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
        if issubclass(ExtendedCommandTemplateParameterExt, dict):
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
        if not isinstance(other, ExtendedCommandTemplateParameterExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other