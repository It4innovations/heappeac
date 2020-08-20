# coding: utf-8

"""
    HEAppE Web API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AsymmetricKeyCredentialsExt(object):
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
        'private_key': 'str',
        'public_key': 'str',
        'username': 'str'
    }

    attribute_map = {
        'private_key': 'privateKey',
        'public_key': 'publicKey',
        'username': 'username'
    }

    def __init__(self, private_key=None, public_key=None, username=None):  # noqa: E501
        """AsymmetricKeyCredentialsExt - a model defined in Swagger"""  # noqa: E501
        self._private_key = None
        self._public_key = None
        self._username = None
        self.discriminator = None
        if private_key is not None:
            self.private_key = private_key
        if public_key is not None:
            self.public_key = public_key
        if username is not None:
            self.username = username

    @property
    def private_key(self):
        """Gets the private_key of this AsymmetricKeyCredentialsExt.  # noqa: E501


        :return: The private_key of this AsymmetricKeyCredentialsExt.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this AsymmetricKeyCredentialsExt.


        :param private_key: The private_key of this AsymmetricKeyCredentialsExt.  # noqa: E501
        :type: str
        """

        self._private_key = private_key

    @property
    def public_key(self):
        """Gets the public_key of this AsymmetricKeyCredentialsExt.  # noqa: E501


        :return: The public_key of this AsymmetricKeyCredentialsExt.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this AsymmetricKeyCredentialsExt.


        :param public_key: The public_key of this AsymmetricKeyCredentialsExt.  # noqa: E501
        :type: str
        """

        self._public_key = public_key

    @property
    def username(self):
        """Gets the username of this AsymmetricKeyCredentialsExt.  # noqa: E501


        :return: The username of this AsymmetricKeyCredentialsExt.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AsymmetricKeyCredentialsExt.


        :param username: The username of this AsymmetricKeyCredentialsExt.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(AsymmetricKeyCredentialsExt, dict):
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
        if not isinstance(other, AsymmetricKeyCredentialsExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
