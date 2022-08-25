# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from resources.health_check import HealthCheck
from resources.approve_hash import ApprovedTransactionResource
from resources.iapi import iapi_resources

api_resources = {
    '/approve_hash': ApprovedTransactionResource,
    '/common/health_check': HealthCheck,
    **{f'/iapi{k}': val for k, val in iapi_resources.items()}
}
