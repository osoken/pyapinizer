# -*- coding: utf-8 -*-

import codecs
import json
from urllib.request import urlopen
from threading import Thread

from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.testing import AsyncHTTPTestCase

from pyapinizer.tornado import generate_handler


class TestGenerateHandler(AsyncHTTPTestCase):
    def get_app(self):
        return Application([
            (r"/(?P<x>.*)", generate_handler(lambda **kwargs: dict({'a': 12}, **kwargs))),
        ])

    def test_get(self):
        response = self.fetch('/')
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(res['a'], 12)
        response = self.fetch('/xyz')
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(res['x'], 'xyz')
