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


class GetAllocatedNodesIPsView(object):
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
        'submitted_job_info_id': 'int',
        'session_code': 'str'
    }

    attribute_map = {
        'submitted_job_info_id': 'SubmittedJobInfoId',
        'session_code': 'SessionCode'
    }

    def __init__(self, submitted_job_info_id=None, session_code=None):  # noqa: E501
        """GetAllocatedNodesIPsView - a model defined in Swagger"""  # noqa: E501
        self._submitted_job_info_id = None
        self._session_code = None
        self.discriminator = None
        if submitted_job_info_id is not None:
            self.submitted_job_info_id = submitted_job_info_id
        if session_code is not None:
            self.session_code = session_code

    @property
    def submitted_job_info_id(self):
        """Gets the submitted_job_info_id of this GetAllocatedNodesIPsView.  # noqa: E501


        :return: The submitted_job_info_id of this GetAllocatedNodesIPsView.  # noqa: E501
        :rtype: int
        """
        return self._submitted_job_info_id

    @submitted_job_info_id.setter
    def submitted_job_info_id(self, submitted_job_info_id):
        """Sets the submitted_job_info_id of this GetAllocatedNodesIPsView.


        :param submitted_job_info_id: The submitted_job_info_id of this GetAllocatedNodesIPsView.  # noqa: E501
        :type: int
        """

        self._submitted_job_info_id = submitted_job_info_id

    @property
    def session_code(self):
        """Gets the session_code of this GetAllocatedNodesIPsView.  # noqa: E501


        :return: The session_code of this GetAllocatedNodesIPsView.  # noqa: E501
        :rtype: str
        """
        return self._session_code

    @session_code.setter
    def session_code(self, session_code):
        """Sets the session_code of this GetAllocatedNodesIPsView.


        :param session_code: The session_code of this GetAllocatedNodesIPsView.  # noqa: E501
        :type: str
        """

        self._session_code = session_code

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
        if issubclass(GetAllocatedNodesIPsView, dict):
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
        if not isinstance(other, GetAllocatedNodesIPsView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
