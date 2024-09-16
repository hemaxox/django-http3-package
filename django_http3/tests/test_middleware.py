# django_http3/tests/test_middleware.py

from django.test import TestCase, RequestFactory
from django.http import HttpResponse
from django_http3.middleware import HTTP3Middleware

class HTTP3MiddlewareTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.get_response = lambda request: HttpResponse("OK")
        self.middleware = HTTP3Middleware(self.get_response)

    def test_http3_request(self):
        request = self.factory.get('/', HTTP_PROTOCOL='HTTP/3')
        response = self.middleware(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"OK")

    def test_http1_request(self):
        request = self.factory.get('/', HTTP_PROTOCOL='HTTP/1.1')
        response = self.middleware(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"OK")
