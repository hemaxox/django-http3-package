from django.conf import settings

class HTTP3Middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.host = getattr(settings, 'HTTP3_HOST', None)
        self.port = getattr(settings, 'HTTP3_PORT', None)

    def __call__(self, request):
        response = self.get_response(request)
        if self.host and self.port:
            response["Alt-Svc"] = f'h3="{self.host}:{self.port}"; ma=3600'
        return response