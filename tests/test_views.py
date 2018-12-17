from __future__ import unicode_literals

import unittest
from http import client as HTTP

from sanic import Sanic
from core.views import View

app = Sanic(__name__)


class TestView(View):
    methods = ('get',)


app.add_route(TestView.as_view(), '/')


class ViewTestCase(unittest.TestCase):

    def test_dispatch_request_allowed(self):
        __, response = app.test_client.get('/')
        self.assertEqual(HTTP.OK, response.status)

    def test_dispatch_request_forbidden(self):
        __, response = app.test_client.post('/')
        self.assertEqual(HTTP.METHOD_NOT_ALLOWED, response.status)
