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

class ClusterNodeTypeForTaskExt(object):
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
        'project': 'ProjectForTaskExt'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'project': 'Project'
    }

    def __init__(self, id=None, name=None, description=None, project=None):  # noqa: E501
        """ClusterNodeTypeForTaskExt - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._project = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if project is not None:
            self.project = project

    @property
    def id(self):
        """Gets the id of this ClusterNodeTypeForTaskExt.  # noqa: E501


        :return: The id of this ClusterNodeTypeForTaskExt.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterNodeTypeForTaskExt.


        :param id: The id of this ClusterNodeTypeForTaskExt.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ClusterNodeTypeForTaskExt.  # noqa: E501


        :return: The name of this ClusterNodeTypeForTaskExt.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterNodeTypeForTaskExt.


        :param name: The name of this ClusterNodeTypeForTaskExt.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ClusterNodeTypeForTaskExt.  # noqa: E501


        :return: The description of this ClusterNodeTypeForTaskExt.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClusterNodeTypeForTaskExt.


        :param description: The description of this ClusterNodeTypeForTaskExt.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def project(self):
        """Gets the project of this ClusterNodeTypeForTaskExt.  # noqa: E501


        :return: The project of this ClusterNodeTypeForTaskExt.  # noqa: E501
        :rtype: ProjectForTaskExt
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ClusterNodeTypeForTaskExt.


        :param project: The project of this ClusterNodeTypeForTaskExt.  # noqa: E501
        :type: ProjectForTaskExt
        """

        self._project = project

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
        if issubclass(ClusterNodeTypeForTaskExt, dict):
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
        if not isinstance(other, ClusterNodeTypeForTaskExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
