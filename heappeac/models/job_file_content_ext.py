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


class JobFileContentExt(object):
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
        'content': 'str',
        'relative_path': 'str',
        'offset': 'int',
        'file_type': 'SynchronizableFilesExt',
        'submitted_task_info_id': 'int'
    }

    attribute_map = {
        'content': 'Content',
        'relative_path': 'RelativePath',
        'offset': 'Offset',
        'file_type': 'FileType',
        'submitted_task_info_id': 'SubmittedTaskInfoId'
    }

    def __init__(self, content=None, relative_path=None, offset=None, file_type=None, submitted_task_info_id=None):  # noqa: E501
        """JobFileContentExt - a model defined in Swagger"""  # noqa: E501
        self._content = None
        self._relative_path = None
        self._offset = None
        self._file_type = None
        self._submitted_task_info_id = None
        self.discriminator = None
        if content is not None:
            self.content = content
        if relative_path is not None:
            self.relative_path = relative_path
        if offset is not None:
            self.offset = offset
        if file_type is not None:
            self.file_type = file_type
        if submitted_task_info_id is not None:
            self.submitted_task_info_id = submitted_task_info_id

    @property
    def content(self):
        """Gets the content of this JobFileContentExt.  # noqa: E501


        :return: The content of this JobFileContentExt.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this JobFileContentExt.


        :param content: The content of this JobFileContentExt.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def relative_path(self):
        """Gets the relative_path of this JobFileContentExt.  # noqa: E501


        :return: The relative_path of this JobFileContentExt.  # noqa: E501
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this JobFileContentExt.


        :param relative_path: The relative_path of this JobFileContentExt.  # noqa: E501
        :type: str
        """

        self._relative_path = relative_path

    @property
    def offset(self):
        """Gets the offset of this JobFileContentExt.  # noqa: E501


        :return: The offset of this JobFileContentExt.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this JobFileContentExt.


        :param offset: The offset of this JobFileContentExt.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def file_type(self):
        """Gets the file_type of this JobFileContentExt.  # noqa: E501


        :return: The file_type of this JobFileContentExt.  # noqa: E501
        :rtype: SynchronizableFilesExt
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this JobFileContentExt.


        :param file_type: The file_type of this JobFileContentExt.  # noqa: E501
        :type: SynchronizableFilesExt
        """

        self._file_type = file_type

    @property
    def submitted_task_info_id(self):
        """Gets the submitted_task_info_id of this JobFileContentExt.  # noqa: E501


        :return: The submitted_task_info_id of this JobFileContentExt.  # noqa: E501
        :rtype: int
        """
        return self._submitted_task_info_id

    @submitted_task_info_id.setter
    def submitted_task_info_id(self, submitted_task_info_id):
        """Sets the submitted_task_info_id of this JobFileContentExt.


        :param submitted_task_info_id: The submitted_task_info_id of this JobFileContentExt.  # noqa: E501
        :type: int
        """

        self._submitted_task_info_id = submitted_task_info_id

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
        if issubclass(JobFileContentExt, dict):
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
        if not isinstance(other, JobFileContentExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other