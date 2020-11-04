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


class SubmittedJobInfoExt(object):
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
        'state': 'JobStateExt',
        'project': 'str',
        'creation_time': 'datetime',
        'submit_time': 'datetime',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'total_allocated_time': 'float',
        'tasks': 'list[SubmittedTaskInfoExt]'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'state': 'State',
        'project': 'Project',
        'creation_time': 'CreationTime',
        'submit_time': 'SubmitTime',
        'start_time': 'StartTime',
        'end_time': 'EndTime',
        'total_allocated_time': 'TotalAllocatedTime',
        'tasks': 'Tasks'
    }

    def __init__(self, id=None, name=None, state=None, project=None, creation_time=None, submit_time=None, start_time=None, end_time=None, total_allocated_time=None, tasks=None):  # noqa: E501
        """SubmittedJobInfoExt - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._state = None
        self._project = None
        self._creation_time = None
        self._submit_time = None
        self._start_time = None
        self._end_time = None
        self._total_allocated_time = None
        self._tasks = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if project is not None:
            self.project = project
        if creation_time is not None:
            self.creation_time = creation_time
        if submit_time is not None:
            self.submit_time = submit_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if total_allocated_time is not None:
            self.total_allocated_time = total_allocated_time
        if tasks is not None:
            self.tasks = tasks

    @property
    def id(self):
        """Gets the id of this SubmittedJobInfoExt.  # noqa: E501


        :return: The id of this SubmittedJobInfoExt.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubmittedJobInfoExt.


        :param id: The id of this SubmittedJobInfoExt.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SubmittedJobInfoExt.  # noqa: E501


        :return: The name of this SubmittedJobInfoExt.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubmittedJobInfoExt.


        :param name: The name of this SubmittedJobInfoExt.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def state(self):
        """Gets the state of this SubmittedJobInfoExt.  # noqa: E501


        :return: The state of this SubmittedJobInfoExt.  # noqa: E501
        :rtype: JobStateExt
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubmittedJobInfoExt.


        :param state: The state of this SubmittedJobInfoExt.  # noqa: E501
        :type: JobStateExt
        """

        self._state = state

    @property
    def project(self):
        """Gets the project of this SubmittedJobInfoExt.  # noqa: E501


        :return: The project of this SubmittedJobInfoExt.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this SubmittedJobInfoExt.


        :param project: The project of this SubmittedJobInfoExt.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def creation_time(self):
        """Gets the creation_time of this SubmittedJobInfoExt.  # noqa: E501


        :return: The creation_time of this SubmittedJobInfoExt.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this SubmittedJobInfoExt.


        :param creation_time: The creation_time of this SubmittedJobInfoExt.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def submit_time(self):
        """Gets the submit_time of this SubmittedJobInfoExt.  # noqa: E501


        :return: The submit_time of this SubmittedJobInfoExt.  # noqa: E501
        :rtype: datetime
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        """Sets the submit_time of this SubmittedJobInfoExt.


        :param submit_time: The submit_time of this SubmittedJobInfoExt.  # noqa: E501
        :type: datetime
        """

        self._submit_time = submit_time

    @property
    def start_time(self):
        """Gets the start_time of this SubmittedJobInfoExt.  # noqa: E501


        :return: The start_time of this SubmittedJobInfoExt.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this SubmittedJobInfoExt.


        :param start_time: The start_time of this SubmittedJobInfoExt.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this SubmittedJobInfoExt.  # noqa: E501


        :return: The end_time of this SubmittedJobInfoExt.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SubmittedJobInfoExt.


        :param end_time: The end_time of this SubmittedJobInfoExt.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def total_allocated_time(self):
        """Gets the total_allocated_time of this SubmittedJobInfoExt.  # noqa: E501


        :return: The total_allocated_time of this SubmittedJobInfoExt.  # noqa: E501
        :rtype: float
        """
        return self._total_allocated_time

    @total_allocated_time.setter
    def total_allocated_time(self, total_allocated_time):
        """Sets the total_allocated_time of this SubmittedJobInfoExt.


        :param total_allocated_time: The total_allocated_time of this SubmittedJobInfoExt.  # noqa: E501
        :type: float
        """

        self._total_allocated_time = total_allocated_time

    @property
    def tasks(self):
        """Gets the tasks of this SubmittedJobInfoExt.  # noqa: E501


        :return: The tasks of this SubmittedJobInfoExt.  # noqa: E501
        :rtype: list[SubmittedTaskInfoExt]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this SubmittedJobInfoExt.


        :param tasks: The tasks of this SubmittedJobInfoExt.  # noqa: E501
        :type: list[SubmittedTaskInfoExt]
        """

        self._tasks = tasks

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
        if issubclass(SubmittedJobInfoExt, dict):
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
        if not isinstance(other, SubmittedJobInfoExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other