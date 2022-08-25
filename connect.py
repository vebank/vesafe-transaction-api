# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import asyncio

import motor
from flask_pymongo import PyMongo
import motor.motor_asyncio
from rediscluster import RedisCluster
from config import Config


class InterfaceAsync:
    def __init__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(Config.MONGO_URI)
        self.client.get_io_loop = asyncio.get_event_loop
        self.db = self.client.core


asyncio_mongo = InterfaceAsync()
connect_db = PyMongo()

redis_cluster = RedisCluster(
    startup_nodes=Config.REDIS_CLUSTER,
    decode_responses=True,
    skip_full_coverage_check=True
)
from lib import HTTPSecurity

security = HTTPSecurity(redis=redis_cluster, auth_address=Config.AUTH_ADDRESS)
