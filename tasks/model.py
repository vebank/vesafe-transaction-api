# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from bson import json_util
from pydash import get

from worker import worker
import models as md

_tasks = {

}
for __model__ in md.__models__:
    _tasks[getattr(md, __model__).__class__.__name__] = getattr(md, __model__)

for __model__ in md.__models__:
    @worker.task(name=getattr(md, __model__).task_name, rate_limit='100000/s')
    def task_model(msg):
        _func = getattr(_tasks[get(msg, 'model')], get(msg, 'func'))
        if _func:
            _payload = json_util.loads(get(msg, 'payload'))
            return _func(*get(_payload, 'args'), **get(_payload, 'kwargs'))
