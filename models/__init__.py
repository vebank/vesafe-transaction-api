# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from config import Config
from lib import DaoModel, AsyncDaoModel
from connect import connect_db, redis_cluster, asyncio_mongo

safeTxnModel = DaoModel(connect_db.db.safe_txn) 
safeLogsModel = DaoModel(connect_db.db.safe_logs) 

