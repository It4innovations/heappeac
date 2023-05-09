# coding: utf-8

"""
    HEAppE Web API

    HEAppE middleware API v4.0.0  # noqa: E501

    OpenAPI spec version: v4.0.0
    Contact: support.heappe@it4i.cz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DigitalSignatureCredentialsExt(object):
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
        'username': 'str',
        'noise': 'str',
        'digital_signature': 'list[int]'
    }

    attribute_map = {
        'username': 'Username',
        'noise': 'Noise',
        'digital_signature': 'DigitalSignature'
    }

    def __init__(self, username=None, noise=None, digital_signature=None):  # noqa: E501
        """DigitalSignatureCredentialsExt - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._noise = None
        self._digital_signature = None
        self.discriminator = None
        if username is not None:
            self.username = username
        if noise is not None:
            self.noise = noise
        if digital_signature is not None:
            self.digital_signature = digital_signature

    @property
    def username(self):
        """Gets the username of this DigitalSignatureCredentialsExt.  # noqa: E501


        :return: The username of this DigitalSignatureCredentialsExt.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this DigitalSignatureCredentialsExt.


        :param username: The username of this DigitalSignatureCredentialsExt.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def noise(self):
        """Gets the noise of this DigitalSignatureCredentialsExt.  # noqa: E501


        :return: The noise of this DigitalSignatureCredentialsExt.  # noqa: E501
        :rtype: str
        """
        return self._noise

    @noise.setter
    def noise(self, noise):
        """Sets the noise of this DigitalSignatureCredentialsExt.


        :param noise: The noise of this DigitalSignatureCredentialsExt.  # noqa: E501
        :type: str
        """

        self._noise = noise

    @property
    def digital_signature(self):
        """Gets the digital_signature of this DigitalSignatureCredentialsExt.  # noqa: E501


        :return: The digital_signature of this DigitalSignatureCredentialsExt.  # noqa: E501
        :rtype: list[int]
        """
        return self._digital_signature

    @digital_signature.setter
    def digital_signature(self, digital_signature):
        """Sets the digital_signature of this DigitalSignatureCredentialsExt.


        :param digital_signature: The digital_signature of this DigitalSignatureCredentialsExt.  # noqa: E501
        :type: list[int]
        """

        self._digital_signature = digital_signature

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
        if issubclass(DigitalSignatureCredentialsExt, dict):
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
        if not isinstance(other, DigitalSignatureCredentialsExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
