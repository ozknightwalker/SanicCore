from __future__ import unicode_literals

from functools import wraps
from http import client as HTTP
from sanic.response import json


def view_method_allowed():
    def decorator(f):
        @wraps(f)
        async def decorated_function(view, *args, **kwargs):
            request = args[0]
            if request.method.lower() not in view.methods:
                return json(
                    {'status': 'METHOD_NOT_ALLOWED'}, HTTP.METHOD_NOT_ALLOWED)
            return await f(view, *args, **kwargs)
        return decorated_function
    return decorator
