from django.apps import AppConfig
from django.conf import settings

class DjangoHttp3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_http3'

    def ready(self):
        settings.HTTP3_HOST = getattr(settings, 'HTTP3_HOST', 'localhost')
        settings.HTTP3_PORT = getattr(settings, 'HTTP3_PORT', 8000)