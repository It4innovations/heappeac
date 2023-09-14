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

class ResourceLimitationExt(object):
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
        'total_max_cores': 'int',
        'max_cores_per_job': 'int'
    }

    attribute_map = {
        'total_max_cores': 'TotalMaxCores',
        'max_cores_per_job': 'MaxCoresPerJob'
    }

    def __init__(self, total_max_cores=None, max_cores_per_job=None):  # noqa: E501
        """ResourceLimitationExt - a model defined in Swagger"""  # noqa: E501
        self._total_max_cores = None
        self._max_cores_per_job = None
        self.discriminator = None
        if total_max_cores is not None:
            self.total_max_cores = total_max_cores
        if max_cores_per_job is not None:
            self.max_cores_per_job = max_cores_per_job

    @property
    def total_max_cores(self):
        """Gets the total_max_cores of this ResourceLimitationExt.  # noqa: E501


        :return: The total_max_cores of this ResourceLimitationExt.  # noqa: E501
        :rtype: int
        """
        return self._total_max_cores

    @total_max_cores.setter
    def total_max_cores(self, total_max_cores):
        """Sets the total_max_cores of this ResourceLimitationExt.


        :param total_max_cores: The total_max_cores of this ResourceLimitationExt.  # noqa: E501
        :type: int
        """

        self._total_max_cores = total_max_cores

    @property
    def max_cores_per_job(self):
        """Gets the max_cores_per_job of this ResourceLimitationExt.  # noqa: E501


        :return: The max_cores_per_job of this ResourceLimitationExt.  # noqa: E501
        :rtype: int
        """
        return self._max_cores_per_job

    @max_cores_per_job.setter
    def max_cores_per_job(self, max_cores_per_job):
        """Sets the max_cores_per_job of this ResourceLimitationExt.


        :param max_cores_per_job: The max_cores_per_job of this ResourceLimitationExt.  # noqa: E501
        :type: int
        """

        self._max_cores_per_job = max_cores_per_job

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
        if issubclass(ResourceLimitationExt, dict):
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
        if not isinstance(other, ResourceLimitationExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other