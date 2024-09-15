import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import re_path,path
from ps.consumers import *
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()
websocket_urlpatterns = [
    path("ws/main/", ChatConsumer.as_asgi()),
]

application =ProtocolTypeRouter(
    {
        'websocket':(
            (
                URLRouter( [path("main/", ChatConsumer),
])
                )
            ),
       # "http": django_asgi_app,
        
        
    }
)