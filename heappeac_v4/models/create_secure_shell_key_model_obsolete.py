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

class CreateSecureShellKeyModelObsolete(object):
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
        'username': 'str',
        'password': 'str',
        'project_id': 'int'
    }

    attribute_map = {
        'session_code': 'SessionCode',
        'username': 'Username',
        'password': 'Password',
        'project_id': 'ProjectId'
    }

    def __init__(self, session_code=None, username=None, password=None, project_id=None):  # noqa: E501
        """CreateSecureShellKeyModelObsolete - a model defined in Swagger"""  # noqa: E501
        self._session_code = None
        self._username = None
        self._password = None
        self._project_id = None
        self.discriminator = None
        if session_code is not None:
            self.session_code = session_code
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if project_id is not None:
            self.project_id = project_id

    @property
    def session_code(self):
        """Gets the session_code of this CreateSecureShellKeyModelObsolete.  # noqa: E501


        :return: The session_code of this CreateSecureShellKeyModelObsolete.  # noqa: E501
        :rtype: str
        """
        return self._session_code

    @session_code.setter
    def session_code(self, session_code):
        """Sets the session_code of this CreateSecureShellKeyModelObsolete.


        :param session_code: The session_code of this CreateSecureShellKeyModelObsolete.  # noqa: E501
        :type: str
        """

        self._session_code = session_code

    @property
    def username(self):
        """Gets the username of this CreateSecureShellKeyModelObsolete.  # noqa: E501


        :return: The username of this CreateSecureShellKeyModelObsolete.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CreateSecureShellKeyModelObsolete.


        :param username: The username of this CreateSecureShellKeyModelObsolete.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this CreateSecureShellKeyModelObsolete.  # noqa: E501


        :return: The password of this CreateSecureShellKeyModelObsolete.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateSecureShellKeyModelObsolete.


        :param password: The password of this CreateSecureShellKeyModelObsolete.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def project_id(self):
        """Gets the project_id of this CreateSecureShellKeyModelObsolete.  # noqa: E501


        :return: The project_id of this CreateSecureShellKeyModelObsolete.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateSecureShellKeyModelObsolete.


        :param project_id: The project_id of this CreateSecureShellKeyModelObsolete.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

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
        if issubclass(CreateSecureShellKeyModelObsolete, dict):
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
        if not isinstance(other, CreateSecureShellKeyModelObsolete):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
