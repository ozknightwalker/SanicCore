from __future__ import unicode_literals

from http import client as HTTP

from sanic.response import text
from sanic.views import HTTPMethodView

__all__ = [
    'BaseExceptionView',
    'NotFound',
    'MethodNotAllowed',
    'BadRequest',
]


class BaseExceptionView(HTTPMethodView):
    httpCode = HTTP.BAD_REQUEST
    msg = 'Base Exception'
    methods = ('get',)

    async def get(self, request):
        return text(self.msg, status=self.httpCode)


class NotFound(BaseExceptionView):
    httpCode = HTTP.NOT_FOUND
    msg = 'Page Not Found!'


class MethodNotAllowed(BaseExceptionView):
    httpCode = HTTP.METHOD_NOT_ALLOWED
    msg = 'Method Not Allowed!'


class BadRequest(BaseExceptionView):
    httpCode = HTTP.BAD_REQUEST
    msg = 'Bad Request!'
