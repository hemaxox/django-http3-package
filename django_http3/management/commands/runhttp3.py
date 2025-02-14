from django.core.management.base import BaseCommand
from django.core.asgi import get_asgi_application
from django.conf import settings
from ...server.http3_server import run_server
from ...utils.ssl_utils import ensure_ssl_cert

class Command(BaseCommand):
    help = 'Runs the server with HTTP/3 support'

    def handle(self, *args, **options):
        certfile, keyfile = ensure_ssl_cert()
        asgi_app = get_asgi_application()
        host = getattr(settings, 'HTTP3_HOST', 'localhost')
        port = getattr(settings, 'HTTP3_PORT', 8000)
        run_server(asgi_app, host, port, certfile, keyfile)