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

class ClusterNodeTypeExt(object):
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
        'number_of_nodes': 'int',
        'cores_per_node': 'int',
        'max_walltime': 'int',
        'file_transfer_method_id': 'int',
        'projects': 'list[ProjectExt]'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'number_of_nodes': 'NumberOfNodes',
        'cores_per_node': 'CoresPerNode',
        'max_walltime': 'MaxWalltime',
        'file_transfer_method_id': 'FileTransferMethodId',
        'projects': 'Projects'
    }

    def __init__(self, id=None, name=None, description=None, number_of_nodes=None, cores_per_node=None, max_walltime=None, file_transfer_method_id=None, projects=None):  # noqa: E501
        """ClusterNodeTypeExt - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._number_of_nodes = None
        self._cores_per_node = None
        self._max_walltime = None
        self._file_transfer_method_id = None
        self._projects = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if number_of_nodes is not None:
            self.number_of_nodes = number_of_nodes
        if cores_per_node is not None:
            self.cores_per_node = cores_per_node
        if max_walltime is not None:
            self.max_walltime = max_walltime
        if file_transfer_method_id is not None:
            self.file_transfer_method_id = file_transfer_method_id
        if projects is not None:
            self.projects = projects

    @property
    def id(self):
        """Gets the id of this ClusterNodeTypeExt.  # noqa: E501


        :return: The id of this ClusterNodeTypeExt.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterNodeTypeExt.


        :param id: The id of this ClusterNodeTypeExt.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ClusterNodeTypeExt.  # noqa: E501


        :return: The name of this ClusterNodeTypeExt.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterNodeTypeExt.


        :param name: The name of this ClusterNodeTypeExt.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ClusterNodeTypeExt.  # noqa: E501


        :return: The description of this ClusterNodeTypeExt.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClusterNodeTypeExt.


        :param description: The description of this ClusterNodeTypeExt.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def number_of_nodes(self):
        """Gets the number_of_nodes of this ClusterNodeTypeExt.  # noqa: E501


        :return: The number_of_nodes of this ClusterNodeTypeExt.  # noqa: E501
        :rtype: int
        """
        return self._number_of_nodes

    @number_of_nodes.setter
    def number_of_nodes(self, number_of_nodes):
        """Sets the number_of_nodes of this ClusterNodeTypeExt.


        :param number_of_nodes: The number_of_nodes of this ClusterNodeTypeExt.  # noqa: E501
        :type: int
        """

        self._number_of_nodes = number_of_nodes

    @property
    def cores_per_node(self):
        """Gets the cores_per_node of this ClusterNodeTypeExt.  # noqa: E501


        :return: The cores_per_node of this ClusterNodeTypeExt.  # noqa: E501
        :rtype: int
        """
        return self._cores_per_node

    @cores_per_node.setter
    def cores_per_node(self, cores_per_node):
        """Sets the cores_per_node of this ClusterNodeTypeExt.


        :param cores_per_node: The cores_per_node of this ClusterNodeTypeExt.  # noqa: E501
        :type: int
        """

        self._cores_per_node = cores_per_node

    @property
    def max_walltime(self):
        """Gets the max_walltime of this ClusterNodeTypeExt.  # noqa: E501


        :return: The max_walltime of this ClusterNodeTypeExt.  # noqa: E501
        :rtype: int
        """
        return self._max_walltime

    @max_walltime.setter
    def max_walltime(self, max_walltime):
        """Sets the max_walltime of this ClusterNodeTypeExt.


        :param max_walltime: The max_walltime of this ClusterNodeTypeExt.  # noqa: E501
        :type: int
        """

        self._max_walltime = max_walltime

    @property
    def file_transfer_method_id(self):
        """Gets the file_transfer_method_id of this ClusterNodeTypeExt.  # noqa: E501


        :return: The file_transfer_method_id of this ClusterNodeTypeExt.  # noqa: E501
        :rtype: int
        """
        return self._file_transfer_method_id

    @file_transfer_method_id.setter
    def file_transfer_method_id(self, file_transfer_method_id):
        """Sets the file_transfer_method_id of this ClusterNodeTypeExt.


        :param file_transfer_method_id: The file_transfer_method_id of this ClusterNodeTypeExt.  # noqa: E501
        :type: int
        """

        self._file_transfer_method_id = file_transfer_method_id

    @property
    def projects(self):
        """Gets the projects of this ClusterNodeTypeExt.  # noqa: E501


        :return: The projects of this ClusterNodeTypeExt.  # noqa: E501
        :rtype: list[ProjectExt]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this ClusterNodeTypeExt.


        :param projects: The projects of this ClusterNodeTypeExt.  # noqa: E501
        :type: list[ProjectExt]
        """

        self._projects = projects

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
        if issubclass(ClusterNodeTypeExt, dict):
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
        if not isinstance(other, ClusterNodeTypeExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
