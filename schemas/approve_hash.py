# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from marshmallow import Schema, EXCLUDE, RAISE, fields, validate
from lib.schema import IsObjectId, NotBlank

_statuses = [
    "init",
    "approved",
    "ExecutionSuccess",
    "ExecutionFailure",
]

_states = [
    "unverified",
    "verified",
]

class ApproveHashSchema(Schema):
    class Meta:
        unknown = RAISE

    txn_hash = fields.Str(required=True, validate=NotBlank())
    tx = fields.Dict(required=True)
    raw = fields.Dict(required=True)



class GetApproveHashSchema(Schema):
    class Meta:
        unknown = RAISE
        
    status = fields.Str(required=True, validate=validate.OneOf(_statuses))
    # state = fields.Str(required=True, validate=validate.OneOf(_states))


class ApproveHashItemResponse(Schema):
    class Meta:
        unknown = EXCLUDE

    txn_hash = fields.Str(required=True)
    owner = fields.Str(required=False)
    status = fields.Str(required=False)
    tx = fields.Dict(required=False)
    raw = fields.Dict(required=False)

class ApproveHashResponse(Schema):
    class Meta:
        unknown = EXCLUDE

    transactions = fields.List(fields.Nested(ApproveHashItemResponse))
  
