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
        'generic_command_template_id': 'int',
        'name': 'str',
        'project_id': 'int',
        'description': 'str',
        'code': 'str',
        'executable_file': 'str',
        'preparation_script': 'str'
    }

    attribute_map = {
        'session_code': 'SessionCode',
        'generic_command_template_id': 'GenericCommandTemplateId',
        'name': 'Name',
        'project_id': 'ProjectId',
        'description': 'Description',
        'code': 'Code',
        'executable_file': 'ExecutableFile',
        'preparation_script': 'PreparationScript'
    }

    def __init__(self, session_code=None, generic_command_template_id=None, name=None, project_id=None, description=None, code=None, executable_file=None, preparation_script=None):  # noqa: E501
        """CreateCommandTemplateModel - a model defined in Swagger"""  # noqa: E501
        self._session_code = None
        self._generic_command_template_id = None
        self._name = None
        self._project_id = None
        self._description = None
        self._code = None
        self._executable_file = None
        self._preparation_script = None
        self.discriminator = None
        if session_code is not None:
            self.session_code = session_code
        if generic_command_template_id is not None:
            self.generic_command_template_id = generic_command_template_id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if description is not None:
            self.description = description
        if code is not None:
            self.code = code
        if executable_file is not None:
            self.executable_file = executable_file
        if preparation_script is not None:
            self.preparation_script = preparation_script

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
    def generic_command_template_id(self):
        """Gets the generic_command_template_id of this CreateCommandTemplateModel.  # noqa: E501


        :return: The generic_command_template_id of this CreateCommandTemplateModel.  # noqa: E501
        :rtype: int
        """
        return self._generic_command_template_id

    @generic_command_template_id.setter
    def generic_command_template_id(self, generic_command_template_id):
        """Sets the generic_command_template_id of this CreateCommandTemplateModel.


        :param generic_command_template_id: The generic_command_template_id of this CreateCommandTemplateModel.  # noqa: E501
        :type: int
        """

        self._generic_command_template_id = generic_command_template_id

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
    def code(self):
        """Gets the code of this CreateCommandTemplateModel.  # noqa: E501


        :return: The code of this CreateCommandTemplateModel.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CreateCommandTemplateModel.


        :param code: The code of this CreateCommandTemplateModel.  # noqa: E501
        :type: str
        """

        self._code = code

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
