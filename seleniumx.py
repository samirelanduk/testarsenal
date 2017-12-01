from unittest.mock import patch
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import resolve

class TestCaseX:

    def check_url_returns_view(self, url, view):
        resolver = resolve(url)
        self.assertEqual(resolver.func, view)


    def get_request(self, path, method="get", data=None):
        factory = RequestFactory()
        data = data if data else {}
        if  method == "post":
            request = factory.post(path, data=data)
        request = factory.get(path, data=data)
        return request


    def check_view_uses_template(self, view, request, template, *args):
        render_patcher = patch("django.shortcuts.render")
        mock_render = render_patcher.start()
        try:
            response = view(request, *args)
            self.assertTrue(mock_render.called)
            self.assertEqual(mock_render.call_args_list[0][0][1], template)
        finally:
            render_patcher.stop()


    def get(self, path):
        self.browser.get(self.live_server_url + path)
