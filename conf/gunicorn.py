# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""


def pre_request(worker, req):
    if '/health_check' in req.path:
        return
    worker.log.debug("Request: %s %s" % (req.method, req.path))


def post_request(worker, req, environ, resp):
    if '/health_check' in req.path:
        return
    worker.log.debug("Response: %s %s - %s" % (req.method, req.path, resp.status))
