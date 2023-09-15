# Code from module with minor edits from me

from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
from channels.auth import AuthMiddlewareStack

# declaration of new version of application
application = ProtocolTypeRouter({ 
    # Requests sent to the chat application   
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

# End of Code from module with minor edits from me