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

from heappeac_v4.api_client import ApiClient


class ManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def heappe_management_command_template_delete(self, **kwargs):  # noqa: E501
        """Remove command template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_management_command_template_delete(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RemoveCommandTemplateModel body: RemoveCommandTemplateModel
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_management_command_template_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_management_command_template_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_management_command_template_delete_with_http_info(self, **kwargs):  # noqa: E501
        """Remove command template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_management_command_template_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RemoveCommandTemplateModel body: RemoveCommandTemplateModel
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
                    " to method heappe_management_command_template_delete" % key
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
            '/heappe/Management/CommandTemplate', 'DELETE',
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

    def heappe_management_command_template_post(self, **kwargs):  # noqa: E501
        """Create Command Template from Generic Command Template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_management_command_template_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateCommandTemplateModel body: CreateCommandTemplate
        :return: CommandTemplateExt
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_management_command_template_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_management_command_template_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_management_command_template_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create Command Template from Generic Command Template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_management_command_template_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateCommandTemplateModel body: CreateCommandTemplate
        :return: CommandTemplateExt
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
                    " to method heappe_management_command_template_post" % key
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
            '/heappe/Management/CommandTemplate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommandTemplateExt',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_management_command_template_put(self, **kwargs):  # noqa: E501
        """Modify command template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_management_command_template_put(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModifyCommandTemplateModel body: ModifyCommandTemplateModel
        :return: CommandTemplateExt
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_management_command_template_put_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_management_command_template_put_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_management_command_template_put_with_http_info(self, **kwargs):  # noqa: E501
        """Modify command template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_management_command_template_put_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModifyCommandTemplateModel body: ModifyCommandTemplateModel
        :return: CommandTemplateExt
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
                    " to method heappe_management_command_template_put" % key
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
            '/heappe/Management/CommandTemplate', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommandTemplateExt',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_management_instance_informations_get(self, **kwargs):  # noqa: E501
        """Get HEAppE Infromation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_management_instance_informations_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str SessionCode: SessionCode
        :return: InstanceInformationExt
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_management_instance_informations_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_management_instance_informations_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_management_instance_informations_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get HEAppE Infromation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_management_instance_informations_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str SessionCode: SessionCode
        :return: InstanceInformationExt
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['SessionCode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heappe_management_instance_informations_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'SessionCode' in params:
            query_params.append(('SessionCode', params['SessionCode']))  # noqa: E501

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
            '/heappe/Management/InstanceInformations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InstanceInformationExt',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)