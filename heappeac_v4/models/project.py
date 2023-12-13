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

class Project(object):
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
        'description': 'str',
        'accounting_string': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'created_at': 'datetime',
        'modified_at': 'datetime',
        'is_deleted': 'bool',
        'use_accounting_string_for_scheduler': 'bool',
        'usage_type': 'UsageType',
        'adaptor_user_groups': 'list[AdaptorUserGroup]',
        'cluster_projects': 'list[ClusterProject]',
        'command_templates': 'list[CommandTemplate]',
        'project_contacts': 'list[ProjectContact]'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'accounting_string': 'AccountingString',
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'created_at': 'CreatedAt',
        'modified_at': 'ModifiedAt',
        'is_deleted': 'IsDeleted',
        'use_accounting_string_for_scheduler': 'UseAccountingStringForScheduler',
        'usage_type': 'UsageType',
        'adaptor_user_groups': 'AdaptorUserGroups',
        'cluster_projects': 'ClusterProjects',
        'command_templates': 'CommandTemplates',
        'project_contacts': 'ProjectContacts'
    }

    def __init__(self, id=None, name=None, description=None, accounting_string=None, start_date=None, end_date=None, created_at=None, modified_at=None, is_deleted=None, use_accounting_string_for_scheduler=None, usage_type=None, adaptor_user_groups=None, cluster_projects=None, command_templates=None, project_contacts=None):  # noqa: E501
        """Project - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._accounting_string = None
        self._start_date = None
        self._end_date = None
        self._created_at = None
        self._modified_at = None
        self._is_deleted = None
        self._use_accounting_string_for_scheduler = None
        self._usage_type = None
        self._adaptor_user_groups = None
        self._cluster_projects = None
        self._command_templates = None
        self._project_contacts = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.accounting_string = accounting_string
        self.start_date = start_date
        self.end_date = end_date
        self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        self.is_deleted = is_deleted
        self.use_accounting_string_for_scheduler = use_accounting_string_for_scheduler
        self.usage_type = usage_type
        if adaptor_user_groups is not None:
            self.adaptor_user_groups = adaptor_user_groups
        if cluster_projects is not None:
            self.cluster_projects = cluster_projects
        if command_templates is not None:
            self.command_templates = command_templates
        if project_contacts is not None:
            self.project_contacts = project_contacts

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501


        :return: The id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.


        :param id: The id of this Project.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501


        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.


        :param name: The name of this Project.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Project.  # noqa: E501


        :return: The description of this Project.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Project.


        :param description: The description of this Project.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def accounting_string(self):
        """Gets the accounting_string of this Project.  # noqa: E501


        :return: The accounting_string of this Project.  # noqa: E501
        :rtype: str
        """
        return self._accounting_string

    @accounting_string.setter
    def accounting_string(self, accounting_string):
        """Sets the accounting_string of this Project.


        :param accounting_string: The accounting_string of this Project.  # noqa: E501
        :type: str
        """
        if accounting_string is None:
            raise ValueError("Invalid value for `accounting_string`, must not be `None`")  # noqa: E501

        self._accounting_string = accounting_string

    @property
    def start_date(self):
        """Gets the start_date of this Project.  # noqa: E501


        :return: The start_date of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Project.


        :param start_date: The start_date of this Project.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Project.  # noqa: E501


        :return: The end_date of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Project.


        :param end_date: The end_date of this Project.  # noqa: E501
        :type: datetime
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def created_at(self):
        """Gets the created_at of this Project.  # noqa: E501


        :return: The created_at of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Project.


        :param created_at: The created_at of this Project.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this Project.  # noqa: E501


        :return: The modified_at of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this Project.


        :param modified_at: The modified_at of this Project.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def is_deleted(self):
        """Gets the is_deleted of this Project.  # noqa: E501


        :return: The is_deleted of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this Project.


        :param is_deleted: The is_deleted of this Project.  # noqa: E501
        :type: bool
        """
        if is_deleted is None:
            raise ValueError("Invalid value for `is_deleted`, must not be `None`")  # noqa: E501

        self._is_deleted = is_deleted

    @property
    def use_accounting_string_for_scheduler(self):
        """Gets the use_accounting_string_for_scheduler of this Project.  # noqa: E501


        :return: The use_accounting_string_for_scheduler of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._use_accounting_string_for_scheduler

    @use_accounting_string_for_scheduler.setter
    def use_accounting_string_for_scheduler(self, use_accounting_string_for_scheduler):
        """Sets the use_accounting_string_for_scheduler of this Project.


        :param use_accounting_string_for_scheduler: The use_accounting_string_for_scheduler of this Project.  # noqa: E501
        :type: bool
        """
        if use_accounting_string_for_scheduler is None:
            raise ValueError("Invalid value for `use_accounting_string_for_scheduler`, must not be `None`")  # noqa: E501

        self._use_accounting_string_for_scheduler = use_accounting_string_for_scheduler

    @property
    def usage_type(self):
        """Gets the usage_type of this Project.  # noqa: E501


        :return: The usage_type of this Project.  # noqa: E501
        :rtype: UsageType
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        """Sets the usage_type of this Project.


        :param usage_type: The usage_type of this Project.  # noqa: E501
        :type: UsageType
        """
        if usage_type is None:
            raise ValueError("Invalid value for `usage_type`, must not be `None`")  # noqa: E501

        self._usage_type = usage_type

    @property
    def adaptor_user_groups(self):
        """Gets the adaptor_user_groups of this Project.  # noqa: E501


        :return: The adaptor_user_groups of this Project.  # noqa: E501
        :rtype: list[AdaptorUserGroup]
        """
        return self._adaptor_user_groups

    @adaptor_user_groups.setter
    def adaptor_user_groups(self, adaptor_user_groups):
        """Sets the adaptor_user_groups of this Project.


        :param adaptor_user_groups: The adaptor_user_groups of this Project.  # noqa: E501
        :type: list[AdaptorUserGroup]
        """

        self._adaptor_user_groups = adaptor_user_groups

    @property
    def cluster_projects(self):
        """Gets the cluster_projects of this Project.  # noqa: E501


        :return: The cluster_projects of this Project.  # noqa: E501
        :rtype: list[ClusterProject]
        """
        return self._cluster_projects

    @cluster_projects.setter
    def cluster_projects(self, cluster_projects):
        """Sets the cluster_projects of this Project.


        :param cluster_projects: The cluster_projects of this Project.  # noqa: E501
        :type: list[ClusterProject]
        """

        self._cluster_projects = cluster_projects

    @property
    def command_templates(self):
        """Gets the command_templates of this Project.  # noqa: E501


        :return: The command_templates of this Project.  # noqa: E501
        :rtype: list[CommandTemplate]
        """
        return self._command_templates

    @command_templates.setter
    def command_templates(self, command_templates):
        """Sets the command_templates of this Project.


        :param command_templates: The command_templates of this Project.  # noqa: E501
        :type: list[CommandTemplate]
        """

        self._command_templates = command_templates

    @property
    def project_contacts(self):
        """Gets the project_contacts of this Project.  # noqa: E501


        :return: The project_contacts of this Project.  # noqa: E501
        :rtype: list[ProjectContact]
        """
        return self._project_contacts

    @project_contacts.setter
    def project_contacts(self, project_contacts):
        """Sets the project_contacts of this Project.


        :param project_contacts: The project_contacts of this Project.  # noqa: E501
        :type: list[ProjectContact]
        """

        self._project_contacts = project_contacts

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
        if issubclass(Project, dict):
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
        if not isinstance(other, Project):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
