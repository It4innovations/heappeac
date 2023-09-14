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

class TaskReportExt(object):
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
        'state': 'TaskStateExt',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'command_template_id': 'int',
        'usage': 'float'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'state': 'State',
        'start_time': 'StartTime',
        'end_time': 'EndTime',
        'command_template_id': 'CommandTemplateId',
        'usage': 'Usage'
    }

    def __init__(self, id=None, name=None, state=None, start_time=None, end_time=None, command_template_id=None, usage=None):  # noqa: E501
        """TaskReportExt - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._state = None
        self._start_time = None
        self._end_time = None
        self._command_template_id = None
        self._usage = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if command_template_id is not None:
            self.command_template_id = command_template_id
        if usage is not None:
            self.usage = usage

    @property
    def id(self):
        """Gets the id of this TaskReportExt.  # noqa: E501


        :return: The id of this TaskReportExt.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskReportExt.


        :param id: The id of this TaskReportExt.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TaskReportExt.  # noqa: E501


        :return: The name of this TaskReportExt.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskReportExt.


        :param name: The name of this TaskReportExt.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def state(self):
        """Gets the state of this TaskReportExt.  # noqa: E501


        :return: The state of this TaskReportExt.  # noqa: E501
        :rtype: TaskStateExt
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TaskReportExt.


        :param state: The state of this TaskReportExt.  # noqa: E501
        :type: TaskStateExt
        """

        self._state = state

    @property
    def start_time(self):
        """Gets the start_time of this TaskReportExt.  # noqa: E501


        :return: The start_time of this TaskReportExt.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TaskReportExt.


        :param start_time: The start_time of this TaskReportExt.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this TaskReportExt.  # noqa: E501


        :return: The end_time of this TaskReportExt.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TaskReportExt.


        :param end_time: The end_time of this TaskReportExt.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def command_template_id(self):
        """Gets the command_template_id of this TaskReportExt.  # noqa: E501


        :return: The command_template_id of this TaskReportExt.  # noqa: E501
        :rtype: int
        """
        return self._command_template_id

    @command_template_id.setter
    def command_template_id(self, command_template_id):
        """Sets the command_template_id of this TaskReportExt.


        :param command_template_id: The command_template_id of this TaskReportExt.  # noqa: E501
        :type: int
        """

        self._command_template_id = command_template_id

    @property
    def usage(self):
        """Gets the usage of this TaskReportExt.  # noqa: E501


        :return: The usage of this TaskReportExt.  # noqa: E501
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this TaskReportExt.


        :param usage: The usage of this TaskReportExt.  # noqa: E501
        :type: float
        """

        self._usage = usage

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
        if issubclass(TaskReportExt, dict):
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
        if not isinstance(other, TaskReportExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other