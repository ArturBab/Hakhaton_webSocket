import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import myproj.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            myproj.routing.websocket_urlpatterns
        )
    )
})
