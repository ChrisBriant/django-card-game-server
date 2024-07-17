import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'card_game_server.settings')

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from cards_consumer import routing

from channels.security.websocket import AllowedHostsOriginValidator


#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'card_game_server.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'card_game_server.settings')
django.setup() 

from .middleware import TokenAuthMiddleware

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             routing.websocket_urlpatterns
#         )
#     ),
# })


application = ProtocolTypeRouter({
        "http": get_asgi_application(),
        'websocket': AuthMiddlewareStack(
            TokenAuthMiddleware(
                URLRouter(
                    routing.websocket_urlpatterns,
                )
            )
        )
    })
