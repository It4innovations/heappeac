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

class CreateCommandTemplateModel(object):
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
        'session_code': 'str',
        'name': 'str',
        'description': 'str',
        'extended_allocation_command': 'str',
        'executable_file': 'str',
        'preparation_script': 'str',
        'cluster_node_type_id': 'int',
        'project_id': 'int',
        'template_parameters': 'list[CreateCommandInnerTemplateParameterModel]'
    }

    attribute_map = {
        'session_code': 'SessionCode',
        'name': 'Name',
        'description': 'Description',
        'extended_allocation_command': 'ExtendedAllocationCommand',
        'executable_file': 'ExecutableFile',
        'preparation_script': 'PreparationScript',
        'cluster_node_type_id': 'ClusterNodeTypeId',
        'project_id': 'ProjectId',
        'template_parameters': 'TemplateParameters'
    }

    def __init__(self, session_code=None, name=None, description=None, extended_allocation_command=None, executable_file=None, preparation_script=None, cluster_node_type_id=None, project_id=None, template_parameters=None):  # noqa: E501
        """CreateCommandTemplateModel - a model defined in Swagger"""  # noqa: E501
        self._session_code = None
        self._name = None
        self._description = None
        self._extended_allocation_command = None
        self._executable_file = None
        self._preparation_script = None
        self._cluster_node_type_id = None
        self._project_id = None
        self._template_parameters = None
        self.discriminator = None
        if session_code is not None:
            self.session_code = session_code
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if extended_allocation_command is not None:
            self.extended_allocation_command = extended_allocation_command
        if executable_file is not None:
            self.executable_file = executable_file
        if preparation_script is not None:
            self.preparation_script = preparation_script
        if cluster_node_type_id is not None:
            self.cluster_node_type_id = cluster_node_type_id
        if project_id is not None:
            self.project_id = project_id
        if template_parameters is not None:
            self.template_parameters = template_parameters

    @property
    def session_code(self):
        """Gets the session_code of this CreateCommandTemplateModel.  # noqa: E501


        :return: The session_code of this CreateCommandTemplateModel.  # noqa: E501
        :rtype: str
        """
        return self._session_code

    @session_code.setter
    def session_code(self, session_code):
        """Sets the session_code of this CreateCommandTemplateModel.


        :param session_code: The session_code of this CreateCommandTemplateModel.  # noqa: E501
        :type: str
        """

        self._session_code = session_code

    @property
    def name(self):
        """Gets the name of this CreateCommandTemplateModel.  # noqa: E501


        :return: The name of this CreateCommandTemplateModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCommandTemplateModel.


        :param name: The name of this CreateCommandTemplateModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateCommandTemplateModel.  # noqa: E501


        :return: The description of this CreateCommandTemplateModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateCommandTemplateModel.


        :param description: The description of this CreateCommandTemplateModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def extended_allocation_command(self):
        """Gets the extended_allocation_command of this CreateCommandTemplateModel.  # noqa: E501


        :return: The extended_allocation_command of this CreateCommandTemplateModel.  # noqa: E501
        :rtype: str
        """
        return self._extended_allocation_command

    @extended_allocation_command.setter
    def extended_allocation_command(self, extended_allocation_command):
        """Sets the extended_allocation_command of this CreateCommandTemplateModel.


        :param extended_allocation_command: The extended_allocation_command of this CreateCommandTemplateModel.  # noqa: E501
        :type: str
        """

        self._extended_allocation_command = extended_allocation_command

    @property
    def executable_file(self):
        """Gets the executable_file of this CreateCommandTemplateModel.  # noqa: E501


        :return: The executable_file of this CreateCommandTemplateModel.  # noqa: E501
        :rtype: str
        """
        return self._executable_file

    @executable_file.setter
    def executable_file(self, executable_file):
        """Sets the executable_file of this CreateCommandTemplateModel.


        :param executable_file: The executable_file of this CreateCommandTemplateModel.  # noqa: E501
        :type: str
        """

        self._executable_file = executable_file

    @property
    def preparation_script(self):
        """Gets the preparation_script of this CreateCommandTemplateModel.  # noqa: E501


        :return: The preparation_script of this CreateCommandTemplateModel.  # noqa: E501
        :rtype: str
        """
        return self._preparation_script

    @preparation_script.setter
    def preparation_script(self, preparation_script):
        """Sets the preparation_script of this CreateCommandTemplateModel.


        :param preparation_script: The preparation_script of this CreateCommandTemplateModel.  # noqa: E501
        :type: str
        """

        self._preparation_script = preparation_script

    @property
    def cluster_node_type_id(self):
        """Gets the cluster_node_type_id of this CreateCommandTemplateModel.  # noqa: E501


        :return: The cluster_node_type_id of this CreateCommandTemplateModel.  # noqa: E501
        :rtype: int
        """
        return self._cluster_node_type_id

    @cluster_node_type_id.setter
    def cluster_node_type_id(self, cluster_node_type_id):
        """Sets the cluster_node_type_id of this CreateCommandTemplateModel.


        :param cluster_node_type_id: The cluster_node_type_id of this CreateCommandTemplateModel.  # noqa: E501
        :type: int
        """

        self._cluster_node_type_id = cluster_node_type_id

    @property
    def project_id(self):
        """Gets the project_id of this CreateCommandTemplateModel.  # noqa: E501


        :return: The project_id of this CreateCommandTemplateModel.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateCommandTemplateModel.


        :param project_id: The project_id of this CreateCommandTemplateModel.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def template_parameters(self):
        """Gets the template_parameters of this CreateCommandTemplateModel.  # noqa: E501


        :return: The template_parameters of this CreateCommandTemplateModel.  # noqa: E501
        :rtype: list[CreateCommandInnerTemplateParameterModel]
        """
        return self._template_parameters

    @template_parameters.setter
    def template_parameters(self, template_parameters):
        """Sets the template_parameters of this CreateCommandTemplateModel.


        :param template_parameters: The template_parameters of this CreateCommandTemplateModel.  # noqa: E501
        :type: list[CreateCommandInnerTemplateParameterModel]
        """

        self._template_parameters = template_parameters

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
        if issubclass(CreateCommandTemplateModel, dict):
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
        if not isinstance(other, CreateCommandTemplateModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
