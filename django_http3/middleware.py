from django.conf import settings

class HTTP3Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Alt-Svc"] = f'h3="{settings.HTTP3_HOST}:{settings.HTTP3_PORT}"; ma=3600'
        return response