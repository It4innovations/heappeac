# coding: utf-8

"""
    HEAppE Web API

    HEAppE middleware API v2  # noqa: E501

    OpenAPI spec version: v2
    Contact: support.heappe@it4i.cz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ResourceUsageExt(object):
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
        'node_type': 'ClusterNodeTypeExt',
        'cores_used': 'int',
        'limitation': 'ResourceLimitationExt'
    }

    attribute_map = {
        'node_type': 'NodeType',
        'cores_used': 'CoresUsed',
        'limitation': 'Limitation'
    }

    def __init__(self, node_type=None, cores_used=None, limitation=None):  # noqa: E501
        """ResourceUsageExt - a model defined in Swagger"""  # noqa: E501
        self._node_type = None
        self._cores_used = None
        self._limitation = None
        self.discriminator = None
        self.node_type = node_type
        if cores_used is not None:
            self.cores_used = cores_used
        if limitation is not None:
            self.limitation = limitation

    @property
    def node_type(self):
        """Gets the node_type of this ResourceUsageExt.  # noqa: E501


        :return: The node_type of this ResourceUsageExt.  # noqa: E501
        :rtype: ClusterNodeTypeExt
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this ResourceUsageExt.


        :param node_type: The node_type of this ResourceUsageExt.  # noqa: E501
        :type: ClusterNodeTypeExt
        """
        if node_type is None:
            raise ValueError("Invalid value for `node_type`, must not be `None`")  # noqa: E501

        self._node_type = node_type

    @property
    def cores_used(self):
        """Gets the cores_used of this ResourceUsageExt.  # noqa: E501


        :return: The cores_used of this ResourceUsageExt.  # noqa: E501
        :rtype: int
        """
        return self._cores_used

    @cores_used.setter
    def cores_used(self, cores_used):
        """Sets the cores_used of this ResourceUsageExt.


        :param cores_used: The cores_used of this ResourceUsageExt.  # noqa: E501
        :type: int
        """

        self._cores_used = cores_used

    @property
    def limitation(self):
        """Gets the limitation of this ResourceUsageExt.  # noqa: E501


        :return: The limitation of this ResourceUsageExt.  # noqa: E501
        :rtype: ResourceLimitationExt
        """
        return self._limitation

    @limitation.setter
    def limitation(self, limitation):
        """Sets the limitation of this ResourceUsageExt.


        :param limitation: The limitation of this ResourceUsageExt.  # noqa: E501
        :type: ResourceLimitationExt
        """

        self._limitation = limitation

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
        if issubclass(ResourceUsageExt, dict):
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
        if not isinstance(other, ResourceUsageExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other