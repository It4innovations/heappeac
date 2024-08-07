# coding: utf-8

"""
    HEAppE Web API

    HEAppE middleware API v4.2.1  # noqa: E501

    OpenAPI spec version: v4.2.1
    Contact: support.heappe@it4i.cz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AdaptorUser(object):
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
        'username': 'str',
        'password': 'str',
        'public_key': 'str',
        'email': 'str',
        'synchronize': 'bool',
        'deleted': 'bool',
        'created_at': 'datetime',
        'modified_at': 'datetime',
        'user_type': 'AdaptorUserType',
        'adaptor_user_user_group_roles': 'list[AdaptorUserUserGroupRole]',
        'groups': 'list[AdaptorUserGroup]'
    }

    attribute_map = {
        'id': 'Id',
        'username': 'Username',
        'password': 'Password',
        'public_key': 'PublicKey',
        'email': 'Email',
        'synchronize': 'Synchronize',
        'deleted': 'Deleted',
        'created_at': 'CreatedAt',
        'modified_at': 'ModifiedAt',
        'user_type': 'UserType',
        'adaptor_user_user_group_roles': 'AdaptorUserUserGroupRoles',
        'groups': 'Groups'
    }

    def __init__(self, id=None, username=None, password=None, public_key=None, email=None, synchronize=None, deleted=None, created_at=None, modified_at=None, user_type=None, adaptor_user_user_group_roles=None, groups=None):  # noqa: E501
        """AdaptorUser - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._username = None
        self._password = None
        self._public_key = None
        self._email = None
        self._synchronize = None
        self._deleted = None
        self._created_at = None
        self._modified_at = None
        self._user_type = None
        self._adaptor_user_user_group_roles = None
        self._groups = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.username = username
        if password is not None:
            self.password = password
        if public_key is not None:
            self.public_key = public_key
        if email is not None:
            self.email = email
        if synchronize is not None:
            self.synchronize = synchronize
        if deleted is not None:
            self.deleted = deleted
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        self.user_type = user_type
        if adaptor_user_user_group_roles is not None:
            self.adaptor_user_user_group_roles = adaptor_user_user_group_roles
        if groups is not None:
            self.groups = groups

    @property
    def id(self):
        """Gets the id of this AdaptorUser.  # noqa: E501


        :return: The id of this AdaptorUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdaptorUser.


        :param id: The id of this AdaptorUser.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this AdaptorUser.  # noqa: E501


        :return: The username of this AdaptorUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AdaptorUser.


        :param username: The username of this AdaptorUser.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this AdaptorUser.  # noqa: E501


        :return: The password of this AdaptorUser.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AdaptorUser.


        :param password: The password of this AdaptorUser.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def public_key(self):
        """Gets the public_key of this AdaptorUser.  # noqa: E501


        :return: The public_key of this AdaptorUser.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this AdaptorUser.


        :param public_key: The public_key of this AdaptorUser.  # noqa: E501
        :type: str
        """

        self._public_key = public_key

    @property
    def email(self):
        """Gets the email of this AdaptorUser.  # noqa: E501


        :return: The email of this AdaptorUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AdaptorUser.


        :param email: The email of this AdaptorUser.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def synchronize(self):
        """Gets the synchronize of this AdaptorUser.  # noqa: E501


        :return: The synchronize of this AdaptorUser.  # noqa: E501
        :rtype: bool
        """
        return self._synchronize

    @synchronize.setter
    def synchronize(self, synchronize):
        """Sets the synchronize of this AdaptorUser.


        :param synchronize: The synchronize of this AdaptorUser.  # noqa: E501
        :type: bool
        """

        self._synchronize = synchronize

    @property
    def deleted(self):
        """Gets the deleted of this AdaptorUser.  # noqa: E501


        :return: The deleted of this AdaptorUser.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this AdaptorUser.


        :param deleted: The deleted of this AdaptorUser.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def created_at(self):
        """Gets the created_at of this AdaptorUser.  # noqa: E501


        :return: The created_at of this AdaptorUser.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AdaptorUser.


        :param created_at: The created_at of this AdaptorUser.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this AdaptorUser.  # noqa: E501


        :return: The modified_at of this AdaptorUser.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this AdaptorUser.


        :param modified_at: The modified_at of this AdaptorUser.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def user_type(self):
        """Gets the user_type of this AdaptorUser.  # noqa: E501


        :return: The user_type of this AdaptorUser.  # noqa: E501
        :rtype: AdaptorUserType
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this AdaptorUser.


        :param user_type: The user_type of this AdaptorUser.  # noqa: E501
        :type: AdaptorUserType
        """
        if user_type is None:
            raise ValueError("Invalid value for `user_type`, must not be `None`")  # noqa: E501

        self._user_type = user_type

    @property
    def adaptor_user_user_group_roles(self):
        """Gets the adaptor_user_user_group_roles of this AdaptorUser.  # noqa: E501


        :return: The adaptor_user_user_group_roles of this AdaptorUser.  # noqa: E501
        :rtype: list[AdaptorUserUserGroupRole]
        """
        return self._adaptor_user_user_group_roles

    @adaptor_user_user_group_roles.setter
    def adaptor_user_user_group_roles(self, adaptor_user_user_group_roles):
        """Sets the adaptor_user_user_group_roles of this AdaptorUser.


        :param adaptor_user_user_group_roles: The adaptor_user_user_group_roles of this AdaptorUser.  # noqa: E501
        :type: list[AdaptorUserUserGroupRole]
        """

        self._adaptor_user_user_group_roles = adaptor_user_user_group_roles

    @property
    def groups(self):
        """Gets the groups of this AdaptorUser.  # noqa: E501


        :return: The groups of this AdaptorUser.  # noqa: E501
        :rtype: list[AdaptorUserGroup]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this AdaptorUser.


        :param groups: The groups of this AdaptorUser.  # noqa: E501
        :type: list[AdaptorUserGroup]
        """

        self._groups = groups

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
        if issubclass(AdaptorUser, dict):
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
        if not isinstance(other, AdaptorUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
