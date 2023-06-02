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


class JobReportingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def heappe_job_reporting_aggregated_user_group_resource_usage_report_get(self, **kwargs):  # noqa: E501
        """Get aggregated resource report usage for user groups  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_job_reporting_aggregated_user_group_resource_usage_report_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime StartTime:
        :param datetime EndTime:
        :param str SessionCode:
        :return: list[UserGroupReportExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_job_reporting_aggregated_user_group_resource_usage_report_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_job_reporting_aggregated_user_group_resource_usage_report_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_job_reporting_aggregated_user_group_resource_usage_report_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get aggregated resource report usage for user groups  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_job_reporting_aggregated_user_group_resource_usage_report_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime StartTime:
        :param datetime EndTime:
        :param str SessionCode:
        :return: list[UserGroupReportExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['StartTime', 'EndTime', 'SessionCode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heappe_job_reporting_aggregated_user_group_resource_usage_report_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'StartTime' in params:
            query_params.append(('StartTime', params['StartTime']))  # noqa: E501
        if 'EndTime' in params:
            query_params.append(('EndTime', params['EndTime']))  # noqa: E501
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
            '/heappe/JobReporting/AggregatedUserGroupResourceUsageReport', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[UserGroupReportExt]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_job_reporting_jobs_detailed_report_get(self, **kwargs):  # noqa: E501
        """Get job detailed report  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_job_reporting_jobs_detailed_report_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str SessionCode: Session code
        :return: list[UserGroupDetailedReportExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_job_reporting_jobs_detailed_report_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_job_reporting_jobs_detailed_report_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_job_reporting_jobs_detailed_report_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get job detailed report  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_job_reporting_jobs_detailed_report_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str SessionCode: Session code
        :return: list[UserGroupDetailedReportExt]
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
                    " to method heappe_job_reporting_jobs_detailed_report_get" % key
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
            '/heappe/JobReporting/JobsDetailedReport', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[UserGroupDetailedReportExt]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_job_reporting_jobs_state_agregation_report_get(self, **kwargs):  # noqa: E501
        """Get job state aggregation report  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_job_reporting_jobs_state_agregation_report_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str SessionCode: Session code
        :return: list[JobStateAggregationReportExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_job_reporting_jobs_state_agregation_report_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_job_reporting_jobs_state_agregation_report_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_job_reporting_jobs_state_agregation_report_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get job state aggregation report  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_job_reporting_jobs_state_agregation_report_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str SessionCode: Session code
        :return: list[JobStateAggregationReportExt]
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
                    " to method heappe_job_reporting_jobs_state_agregation_report_get" % key
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
            '/heappe/JobReporting/JobsStateAgregationReport', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[JobStateAggregationReportExt]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_job_reporting_list_adaptor_user_groups_get(self, **kwargs):  # noqa: E501
        """Get user groups  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_job_reporting_list_adaptor_user_groups_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str SessionCode: Session code
        :return: UserGroupListReportExt
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_job_reporting_list_adaptor_user_groups_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_job_reporting_list_adaptor_user_groups_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_job_reporting_list_adaptor_user_groups_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get user groups  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_job_reporting_list_adaptor_user_groups_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str SessionCode: Session code
        :return: UserGroupListReportExt
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
                    " to method heappe_job_reporting_list_adaptor_user_groups_get" % key
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
            '/heappe/JobReporting/ListAdaptorUserGroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserGroupListReportExt',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_job_reporting_resource_usage_report_for_job_get(self, **kwargs):  # noqa: E501
        """Get resource usage for executed job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_job_reporting_resource_usage_report_for_job_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str SessionCode: Session code
        :param int JobId: Job ID
        :return: ProjectReportExt
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_job_reporting_resource_usage_report_for_job_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_job_reporting_resource_usage_report_for_job_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_job_reporting_resource_usage_report_for_job_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get resource usage for executed job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_job_reporting_resource_usage_report_for_job_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str SessionCode: Session code
        :param int JobId: Job ID
        :return: ProjectReportExt
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['SessionCode', 'JobId']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heappe_job_reporting_resource_usage_report_for_job_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'SessionCode' in params:
            query_params.append(('SessionCode', params['SessionCode']))  # noqa: E501
        if 'JobId' in params:
            query_params.append(('JobId', params['JobId']))  # noqa: E501

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
            '/heappe/JobReporting/ResourceUsageReportForJob', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectReportExt',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_job_reporting_user_group_resource_usage_report_get(self, **kwargs):  # noqa: E501
        """Get resource usage for user group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_job_reporting_user_group_resource_usage_report_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int GroupId: Group ID
        :param datetime StartTime: StartTime
        :param datetime EndTime: EndTime
        :param str SessionCode: SessionCode
        :return: UserGroupReportExt
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_job_reporting_user_group_resource_usage_report_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_job_reporting_user_group_resource_usage_report_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_job_reporting_user_group_resource_usage_report_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get resource usage for user group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_job_reporting_user_group_resource_usage_report_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int GroupId: Group ID
        :param datetime StartTime: StartTime
        :param datetime EndTime: EndTime
        :param str SessionCode: SessionCode
        :return: UserGroupReportExt
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['GroupId', 'StartTime', 'EndTime', 'SessionCode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heappe_job_reporting_user_group_resource_usage_report_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'GroupId' in params:
            query_params.append(('GroupId', params['GroupId']))  # noqa: E501
        if 'StartTime' in params:
            query_params.append(('StartTime', params['StartTime']))  # noqa: E501
        if 'EndTime' in params:
            query_params.append(('EndTime', params['EndTime']))  # noqa: E501
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
            '/heappe/JobReporting/UserGroupResourceUsageReport', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserGroupReportExt',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heappe_job_reporting_user_resource_usage_report_get(self, **kwargs):  # noqa: E501
        """Get resource usage report for user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_job_reporting_user_resource_usage_report_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int UserId: User ID
        :param datetime StartTime: StartTime
        :param datetime EndTime: EndTime
        :param str SessionCode: SessionCode
        :return: list[UserGroupReportExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heappe_job_reporting_user_resource_usage_report_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.heappe_job_reporting_user_resource_usage_report_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def heappe_job_reporting_user_resource_usage_report_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get resource usage report for user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heappe_job_reporting_user_resource_usage_report_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int UserId: User ID
        :param datetime StartTime: StartTime
        :param datetime EndTime: EndTime
        :param str SessionCode: SessionCode
        :return: list[UserGroupReportExt]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['UserId', 'StartTime', 'EndTime', 'SessionCode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heappe_job_reporting_user_resource_usage_report_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'UserId' in params:
            query_params.append(('UserId', params['UserId']))  # noqa: E501
        if 'StartTime' in params:
            query_params.append(('StartTime', params['StartTime']))  # noqa: E501
        if 'EndTime' in params:
            query_params.append(('EndTime', params['EndTime']))  # noqa: E501
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
            '/heappe/JobReporting/UserResourceUsageReport', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[UserGroupReportExt]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
