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

class SubmitJobModel(object):
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
        'created_job_info_id': 'int'
    }

    attribute_map = {
        'session_code': 'SessionCode',
        'created_job_info_id': 'CreatedJobInfoId'
    }

    def __init__(self, session_code=None, created_job_info_id=None):  # noqa: E501
        """SubmitJobModel - a model defined in Swagger"""  # noqa: E501
        self._session_code = None
        self._created_job_info_id = None
        self.discriminator = None
        if session_code is not None:
            self.session_code = session_code
        if created_job_info_id is not None:
            self.created_job_info_id = created_job_info_id

    @property
    def session_code(self):
        """Gets the session_code of this SubmitJobModel.  # noqa: E501


        :return: The session_code of this SubmitJobModel.  # noqa: E501
        :rtype: str
        """
        return self._session_code

    @session_code.setter
    def session_code(self, session_code):
        """Sets the session_code of this SubmitJobModel.


        :param session_code: The session_code of this SubmitJobModel.  # noqa: E501
        :type: str
        """

        self._session_code = session_code

    @property
    def created_job_info_id(self):
        """Gets the created_job_info_id of this SubmitJobModel.  # noqa: E501


        :return: The created_job_info_id of this SubmitJobModel.  # noqa: E501
        :rtype: int
        """
        return self._created_job_info_id

    @created_job_info_id.setter
    def created_job_info_id(self, created_job_info_id):
        """Sets the created_job_info_id of this SubmitJobModel.


        :param created_job_info_id: The created_job_info_id of this SubmitJobModel.  # noqa: E501
        :type: int
        """

        self._created_job_info_id = created_job_info_id

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
        if issubclass(SubmitJobModel, dict):
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
        if not isinstance(other, SubmitJobModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
