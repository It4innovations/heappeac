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


class GetUserGroupResourceUsageReportView(object):
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
        'group_id': 'int',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'session_code': 'str'
    }

    attribute_map = {
        'group_id': 'groupId',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'session_code': 'sessionCode'
    }

    def __init__(self, group_id=None, start_time=None, end_time=None, session_code=None):  # noqa: E501
        """GetUserGroupResourceUsageReportView - a model defined in Swagger"""  # noqa: E501
        self._group_id = None
        self._start_time = None
        self._end_time = None
        self._session_code = None
        self.discriminator = None
        if group_id is not None:
            self.group_id = group_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if session_code is not None:
            self.session_code = session_code

    @property
    def group_id(self):
        """Gets the group_id of this GetUserGroupResourceUsageReportView.  # noqa: E501


        :return: The group_id of this GetUserGroupResourceUsageReportView.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GetUserGroupResourceUsageReportView.


        :param group_id: The group_id of this GetUserGroupResourceUsageReportView.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def start_time(self):
        """Gets the start_time of this GetUserGroupResourceUsageReportView.  # noqa: E501


        :return: The start_time of this GetUserGroupResourceUsageReportView.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this GetUserGroupResourceUsageReportView.


        :param start_time: The start_time of this GetUserGroupResourceUsageReportView.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this GetUserGroupResourceUsageReportView.  # noqa: E501


        :return: The end_time of this GetUserGroupResourceUsageReportView.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this GetUserGroupResourceUsageReportView.


        :param end_time: The end_time of this GetUserGroupResourceUsageReportView.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def session_code(self):
        """Gets the session_code of this GetUserGroupResourceUsageReportView.  # noqa: E501


        :return: The session_code of this GetUserGroupResourceUsageReportView.  # noqa: E501
        :rtype: str
        """
        return self._session_code

    @session_code.setter
    def session_code(self, session_code):
        """Sets the session_code of this GetUserGroupResourceUsageReportView.


        :param session_code: The session_code of this GetUserGroupResourceUsageReportView.  # noqa: E501
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
        if issubclass(GetUserGroupResourceUsageReportView, dict):
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
        if not isinstance(other, GetUserGroupResourceUsageReportView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
