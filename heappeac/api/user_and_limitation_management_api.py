# coding: utf-8

"""
    HEAppE Web API

    HEAppE middleware API v4.0.0  # noqa: E501

    OpenAPI spec version: v4.0.0
    Contact: support.heappe@it4i.cz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from heappeac.api_client import ApiClient


class UserAndLimitationManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def heappe_user_and_limitation_management_authenticate_user_digital_signature_post(self, **kwargs):  # noqa: E501
        """Provide user authentication  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_user_and_limitation_management_authenticate_user_digital_signature_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthenticateUserDigitalSignatureModel body: Authentication credentials
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_user_and_limitation_management_authenticate_user_digital_signature_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_user_and_limitation_management_authenticate_user_digital_signature_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_user_and_limitation_management_authenticate_user_digital_signature_post_with_http_info(self, **kwargs):  # noqa: E501
        """Provide user authentication  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_user_and_limitation_management_authenticate_user_digital_signature_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthenticateUserDigitalSignatureModel body: Authentication credentials
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heappe_user_and_limitation_management_authenticate_user_digital_signature_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/heappe/UserAndLimitationManagement/AuthenticateUserDigitalSignature', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_user_and_limitation_management_authenticate_user_open_id_post(self, **kwargs):  # noqa: E501
        """Provide user authentication via OpenId token.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_user_and_limitation_management_authenticate_user_open_id_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthenticateUserOpenIdModel body: Authentication credentials
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_user_and_limitation_management_authenticate_user_open_id_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_user_and_limitation_management_authenticate_user_open_id_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_user_and_limitation_management_authenticate_user_open_id_post_with_http_info(self, **kwargs):  # noqa: E501
        """Provide user authentication via OpenId token.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_user_and_limitation_management_authenticate_user_open_id_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthenticateUserOpenIdModel body: Authentication credentials
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heappe_user_and_limitation_management_authenticate_user_open_id_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/heappe/UserAndLimitationManagement/AuthenticateUserOpenId', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_user_and_limitation_management_authenticate_user_open_stack_post(self, **kwargs):  # noqa: E501
        """Provide user authentication to OpenStack.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_user_and_limitation_management_authenticate_user_open_stack_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthenticateUserOpenIdOpenStackModel body: Authentication credentials
        :return: OpenStackApplicationCredentialsExt
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_user_and_limitation_management_authenticate_user_open_stack_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_user_and_limitation_management_authenticate_user_open_stack_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_user_and_limitation_management_authenticate_user_open_stack_post_with_http_info(self, **kwargs):  # noqa: E501
        """Provide user authentication to OpenStack.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_user_and_limitation_management_authenticate_user_open_stack_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthenticateUserOpenIdOpenStackModel body: Authentication credentials
        :return: OpenStackApplicationCredentialsExt
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heappe_user_and_limitation_management_authenticate_user_open_stack_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/heappe/UserAndLimitationManagement/AuthenticateUserOpenStack', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OpenStackApplicationCredentialsExt',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_user_and_limitation_management_authenticate_user_password_post(self, **kwargs):  # noqa: E501
        """Provide user authentication  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_user_and_limitation_management_authenticate_user_password_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthenticateUserPasswordModel body: Authentication credentials
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_user_and_limitation_management_authenticate_user_password_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_user_and_limitation_management_authenticate_user_password_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_user_and_limitation_management_authenticate_user_password_post_with_http_info(self, **kwargs):  # noqa: E501
        """Provide user authentication  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_user_and_limitation_management_authenticate_user_password_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthenticateUserPasswordModel body: Authentication credentials
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heappe_user_and_limitation_management_authenticate_user_password_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/heappe/UserAndLimitationManagement/AuthenticateUserPassword', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_user_and_limitation_management_current_usage_and_limitations_for_current_user_get(self, **kwargs):  # noqa: E501
        """Get current resource usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_user_and_limitation_management_current_usage_and_limitations_for_current_user_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_code:
        :return: list[ProjectResourceUsageExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_user_and_limitation_management_current_usage_and_limitations_for_current_user_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_user_and_limitation_management_current_usage_and_limitations_for_current_user_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_user_and_limitation_management_current_usage_and_limitations_for_current_user_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get current resource usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_user_and_limitation_management_current_usage_and_limitations_for_current_user_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_code:
        :return: list[ProjectResourceUsageExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heappe_user_and_limitation_management_current_usage_and_limitations_for_current_user_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'session_code' in params:
            query_params.append(('sessionCode', params['session_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/heappe/UserAndLimitationManagement/CurrentUsageAndLimitationsForCurrentUser', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProjectResourceUsageExt]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_user_and_limitation_management_get_current_usage_and_limitations_for_current_user_post(self, **kwargs):  # noqa: E501
        """Get current resource usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_user_and_limitation_management_get_current_usage_and_limitations_for_current_user_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetCurrentUsageAndLimitationsForCurrentUserModel body: Session code
        :return: list[ResourceUsageExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_user_and_limitation_management_get_current_usage_and_limitations_for_current_user_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_user_and_limitation_management_get_current_usage_and_limitations_for_current_user_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_user_and_limitation_management_get_current_usage_and_limitations_for_current_user_post_with_http_info(self, **kwargs):  # noqa: E501
        """Get current resource usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_user_and_limitation_management_get_current_usage_and_limitations_for_current_user_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetCurrentUsageAndLimitationsForCurrentUserModel body: Session code
        :return: list[ResourceUsageExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heappe_user_and_limitation_management_get_current_usage_and_limitations_for_current_user_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/heappe/UserAndLimitationManagement/GetCurrentUsageAndLimitationsForCurrentUser', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ResourceUsageExt]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_user_and_limitation_management_projects_for_current_user_get(self, **kwargs):  # noqa: E501
        """Get projects for current user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_user_and_limitation_management_projects_for_current_user_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_code:
        :return: list[ProjectReferenceExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_user_and_limitation_management_projects_for_current_user_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_user_and_limitation_management_projects_for_current_user_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_user_and_limitation_management_projects_for_current_user_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get projects for current user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_user_and_limitation_management_projects_for_current_user_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_code:
        :return: list[ProjectReferenceExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heappe_user_and_limitation_management_projects_for_current_user_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'session_code' in params:
            query_params.append(('sessionCode', params['session_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/heappe/UserAndLimitationManagement/ProjectsForCurrentUser', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProjectReferenceExt]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
