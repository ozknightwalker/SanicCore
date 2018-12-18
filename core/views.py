from __future__ import unicode_literals

from sanic.response import html, text
from sanic.views import HTTPMethodView

from .template import template_env
from .exceptions import ImproperlyConfigured
from .decorators import view_method_allowed


class View(HTTPMethodView):
    methods = ()

    @view_method_allowed()
    def dispatch_request(self, request):
        return super().dispatch_request(request)

    async def get(self, request):
        return text('I am get method')

    async def post(self, request):

        return text('I am post method')

    async def put(self, request):

        return text('I am put method')

    async def patch(self, request):

        return text('I am patch method')

    async def delete(self, request):

        return text('I am delete method')


class ContextMixin(object):

    def get_context_data(self, *args, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        return kwargs


class TemplateResponseMixin(object):
    template_name = None

    def get_template(self):
        if self.template_name is None:
            error_msg = '{} `template_name` is not provided'.format(
                self.__class__.__name__)
            raise ImproperlyConfigured(error_msg)
        try:
            return template_env.get_template(self.template_name)
        except Exception:
            error_msg = 'Template {} not found'.format(self.template_name)
            raise ImproperlyConfigured(error_msg)

    async def render_response(self, context):
        template = self.get_template()
        rendered_template = await template.render_async(context)
        return html(rendered_template)


class TemplateView(TemplateResponseMixin, ContextMixin, View):
    methods = ('get',)

    async def get(self, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return await self.render_response(context)
