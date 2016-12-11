# -*- coding: utf-8 -*-

import json

from tornado.web import RequestHandler


def generate_handler(func):
    class Handler(RequestHandler):
        def get(self, *args, **kwargs):
            argdict = dict(kwargs, **self.request.arguments)
            json.dump(func(*args, **argdict), self)

    return Handler
