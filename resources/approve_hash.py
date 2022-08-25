# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask_restful import Resource
import json
from schemas.approve_hash import ApproveHashSchema, ApproveHashResponse, GetApproveHashSchema
from connect import security
from models import safeTxnModel

class ApprovedTransactionResource(Resource):

    @security.http(
        login_required=False,
        params=GetApproveHashSchema(),
        response=ApproveHashResponse()
    )
    def get(self, params):
        _transactions = safeTxnModel.find(
            filter={
             "status": params['status'],
            #  "state": params['state'],
        })
        return {
            'transactions': _transactions,
            }

    @security.http(
        form_data=ApproveHashSchema(),  # form_data
        login_required=False  # user
    )
    def post(self, form_data):
        
        _txn = safeTxnModel.find_one( filter={
                "txn_hash": form_data["txn_hash"],
                })
        _status = "init" 
        if _txn and "status" in _txn:
            _status = _txn['status']
        
        safeTxnModel.update_one(
            filter={
                "txn_hash": form_data["txn_hash"],
                }, 
            obj= {
            "state": "verified",
            "status": _status,
            "updated_by": "safe-client",
            "tx": form_data['tx'],
            "raw": form_data['raw']
            }, upsert=True
        )
        
       
        return {
            "txn_hash": form_data["txn_hash"],
            "status": _status
        }
