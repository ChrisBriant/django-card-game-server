# from channels.security.websocket import AllowedHostsOriginValidator
# from channels.routing import ProtocolTypeRouter, URLRouter

# from django.conf.urls import url

from django.urls import re_path
from cards_consumer import consumers
#from .middleware import TokenAuthMiddleware



websocket_urlpatterns = [
    re_path(r'ws/cards-consumer/$', consumers.CardsConsumer.as_asgi()),
    #url(r"^ws/cards-consumer/$", consumers.CardsConsumer.as_asgi()),
]

# application = ProtocolTypeRouter({
#         'websocket': AllowedHostsOriginValidator(
#             TokenAuthMiddleware(
#                 URLRouter(
#                     [
#                         url(r"^ws/cards-consumer/$", consumers.CardsConsumer.as_asgi()),
#                     ]
#                 )
#             )
#         )
#     })
