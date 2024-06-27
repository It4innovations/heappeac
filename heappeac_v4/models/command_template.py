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

class CommandTemplate(object):
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
        'extended_allocation_command': 'str',
        'executable_file': 'str',
        'command_parameters': 'str',
        'preparation_script': 'str',
        'is_generic': 'bool',
        'is_enabled': 'bool',
        'template_parameters': 'list[CommandTemplateParameter]',
        'cluster_node_type_id': 'int',
        'cluster_node_type': 'ClusterNodeType',
        'project_id': 'int',
        'project': 'Project',
        'created_from_id': 'int',
        'created_from': 'CommandTemplate',
        'created_at': 'datetime',
        'modified_at': 'datetime'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'extended_allocation_command': 'ExtendedAllocationCommand',
        'executable_file': 'ExecutableFile',
        'command_parameters': 'CommandParameters',
        'preparation_script': 'PreparationScript',
        'is_generic': 'IsGeneric',
        'is_enabled': 'IsEnabled',
        'template_parameters': 'TemplateParameters',
        'cluster_node_type_id': 'ClusterNodeTypeId',
        'cluster_node_type': 'ClusterNodeType',
        'project_id': 'ProjectId',
        'project': 'Project',
        'created_from_id': 'CreatedFromId',
        'created_from': 'CreatedFrom',
        'created_at': 'CreatedAt',
        'modified_at': 'ModifiedAt'
    }

    def __init__(self, id=None, name=None, description=None, extended_allocation_command=None, executable_file=None, command_parameters=None, preparation_script=None, is_generic=None, is_enabled=None, template_parameters=None, cluster_node_type_id=None, cluster_node_type=None, project_id=None, project=None, created_from_id=None, created_from=None, created_at=None, modified_at=None):  # noqa: E501
        """CommandTemplate - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._extended_allocation_command = None
        self._executable_file = None
        self._command_parameters = None
        self._preparation_script = None
        self._is_generic = None
        self._is_enabled = None
        self._template_parameters = None
        self._cluster_node_type_id = None
        self._cluster_node_type = None
        self._project_id = None
        self._project = None
        self._created_from_id = None
        self._created_from = None
        self._created_at = None
        self._modified_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        self.description = description
        if extended_allocation_command is not None:
            self.extended_allocation_command = extended_allocation_command
        self.executable_file = executable_file
        if command_parameters is not None:
            self.command_parameters = command_parameters
        if preparation_script is not None:
            self.preparation_script = preparation_script
        self.is_generic = is_generic
        self.is_enabled = is_enabled
        if template_parameters is not None:
            self.template_parameters = template_parameters
        if cluster_node_type_id is not None:
            self.cluster_node_type_id = cluster_node_type_id
        if cluster_node_type is not None:
            self.cluster_node_type = cluster_node_type
        if project_id is not None:
            self.project_id = project_id
        if project is not None:
            self.project = project
        if created_from_id is not None:
            self.created_from_id = created_from_id
        if created_from is not None:
            self.created_from = created_from
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at

    @property
    def id(self):
        """Gets the id of this CommandTemplate.  # noqa: E501


        :return: The id of this CommandTemplate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CommandTemplate.


        :param id: The id of this CommandTemplate.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CommandTemplate.  # noqa: E501


        :return: The name of this CommandTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CommandTemplate.


        :param name: The name of this CommandTemplate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CommandTemplate.  # noqa: E501


        :return: The description of this CommandTemplate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CommandTemplate.


        :param description: The description of this CommandTemplate.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def extended_allocation_command(self):
        """Gets the extended_allocation_command of this CommandTemplate.  # noqa: E501


        :return: The extended_allocation_command of this CommandTemplate.  # noqa: E501
        :rtype: str
        """
        return self._extended_allocation_command

    @extended_allocation_command.setter
    def extended_allocation_command(self, extended_allocation_command):
        """Sets the extended_allocation_command of this CommandTemplate.


        :param extended_allocation_command: The extended_allocation_command of this CommandTemplate.  # noqa: E501
        :type: str
        """

        self._extended_allocation_command = extended_allocation_command

    @property
    def executable_file(self):
        """Gets the executable_file of this CommandTemplate.  # noqa: E501


        :return: The executable_file of this CommandTemplate.  # noqa: E501
        :rtype: str
        """
        return self._executable_file

    @executable_file.setter
    def executable_file(self, executable_file):
        """Sets the executable_file of this CommandTemplate.


        :param executable_file: The executable_file of this CommandTemplate.  # noqa: E501
        :type: str
        """
        if executable_file is None:
            raise ValueError("Invalid value for `executable_file`, must not be `None`")  # noqa: E501

        self._executable_file = executable_file

    @property
    def command_parameters(self):
        """Gets the command_parameters of this CommandTemplate.  # noqa: E501


        :return: The command_parameters of this CommandTemplate.  # noqa: E501
        :rtype: str
        """
        return self._command_parameters

    @command_parameters.setter
    def command_parameters(self, command_parameters):
        """Sets the command_parameters of this CommandTemplate.


        :param command_parameters: The command_parameters of this CommandTemplate.  # noqa: E501
        :type: str
        """

        self._command_parameters = command_parameters

    @property
    def preparation_script(self):
        """Gets the preparation_script of this CommandTemplate.  # noqa: E501


        :return: The preparation_script of this CommandTemplate.  # noqa: E501
        :rtype: str
        """
        return self._preparation_script

    @preparation_script.setter
    def preparation_script(self, preparation_script):
        """Sets the preparation_script of this CommandTemplate.


        :param preparation_script: The preparation_script of this CommandTemplate.  # noqa: E501
        :type: str
        """

        self._preparation_script = preparation_script

    @property
    def is_generic(self):
        """Gets the is_generic of this CommandTemplate.  # noqa: E501


        :return: The is_generic of this CommandTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._is_generic

    @is_generic.setter
    def is_generic(self, is_generic):
        """Sets the is_generic of this CommandTemplate.


        :param is_generic: The is_generic of this CommandTemplate.  # noqa: E501
        :type: bool
        """
        if is_generic is None:
            raise ValueError("Invalid value for `is_generic`, must not be `None`")  # noqa: E501

        self._is_generic = is_generic

    @property
    def is_enabled(self):
        """Gets the is_enabled of this CommandTemplate.  # noqa: E501


        :return: The is_enabled of this CommandTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this CommandTemplate.


        :param is_enabled: The is_enabled of this CommandTemplate.  # noqa: E501
        :type: bool
        """
        if is_enabled is None:
            raise ValueError("Invalid value for `is_enabled`, must not be `None`")  # noqa: E501

        self._is_enabled = is_enabled

    @property
    def template_parameters(self):
        """Gets the template_parameters of this CommandTemplate.  # noqa: E501


        :return: The template_parameters of this CommandTemplate.  # noqa: E501
        :rtype: list[CommandTemplateParameter]
        """
        return self._template_parameters

    @template_parameters.setter
    def template_parameters(self, template_parameters):
        """Sets the template_parameters of this CommandTemplate.


        :param template_parameters: The template_parameters of this CommandTemplate.  # noqa: E501
        :type: list[CommandTemplateParameter]
        """

        self._template_parameters = template_parameters

    @property
    def cluster_node_type_id(self):
        """Gets the cluster_node_type_id of this CommandTemplate.  # noqa: E501


        :return: The cluster_node_type_id of this CommandTemplate.  # noqa: E501
        :rtype: int
        """
        return self._cluster_node_type_id

    @cluster_node_type_id.setter
    def cluster_node_type_id(self, cluster_node_type_id):
        """Sets the cluster_node_type_id of this CommandTemplate.


        :param cluster_node_type_id: The cluster_node_type_id of this CommandTemplate.  # noqa: E501
        :type: int
        """

        self._cluster_node_type_id = cluster_node_type_id

    @property
    def cluster_node_type(self):
        """Gets the cluster_node_type of this CommandTemplate.  # noqa: E501


        :return: The cluster_node_type of this CommandTemplate.  # noqa: E501
        :rtype: ClusterNodeType
        """
        return self._cluster_node_type

    @cluster_node_type.setter
    def cluster_node_type(self, cluster_node_type):
        """Sets the cluster_node_type of this CommandTemplate.


        :param cluster_node_type: The cluster_node_type of this CommandTemplate.  # noqa: E501
        :type: ClusterNodeType
        """

        self._cluster_node_type = cluster_node_type

    @property
    def project_id(self):
        """Gets the project_id of this CommandTemplate.  # noqa: E501


        :return: The project_id of this CommandTemplate.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CommandTemplate.


        :param project_id: The project_id of this CommandTemplate.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def project(self):
        """Gets the project of this CommandTemplate.  # noqa: E501


        :return: The project of this CommandTemplate.  # noqa: E501
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this CommandTemplate.


        :param project: The project of this CommandTemplate.  # noqa: E501
        :type: Project
        """

        self._project = project

    @property
    def created_from_id(self):
        """Gets the created_from_id of this CommandTemplate.  # noqa: E501


        :return: The created_from_id of this CommandTemplate.  # noqa: E501
        :rtype: int
        """
        return self._created_from_id

    @created_from_id.setter
    def created_from_id(self, created_from_id):
        """Sets the created_from_id of this CommandTemplate.


        :param created_from_id: The created_from_id of this CommandTemplate.  # noqa: E501
        :type: int
        """

        self._created_from_id = created_from_id

    @property
    def created_from(self):
        """Gets the created_from of this CommandTemplate.  # noqa: E501


        :return: The created_from of this CommandTemplate.  # noqa: E501
        :rtype: CommandTemplate
        """
        return self._created_from

    @created_from.setter
    def created_from(self, created_from):
        """Sets the created_from of this CommandTemplate.


        :param created_from: The created_from of this CommandTemplate.  # noqa: E501
        :type: CommandTemplate
        """

        self._created_from = created_from

    @property
    def created_at(self):
        """Gets the created_at of this CommandTemplate.  # noqa: E501


        :return: The created_at of this CommandTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CommandTemplate.


        :param created_at: The created_at of this CommandTemplate.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this CommandTemplate.  # noqa: E501


        :return: The modified_at of this CommandTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this CommandTemplate.


        :param modified_at: The modified_at of this CommandTemplate.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

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
        if issubclass(CommandTemplate, dict):
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
        if not isinstance(other, CommandTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
