# Code from the module with minor edits from me

from . import consumers
from django.urls import re_path

# urls for the api should be in the pattern of regular expression string "ws" and then the string for room name. 
websocket_urlpatterns = [
    re_path(r'ws/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()), #chatConsumer is a class
]

# End of code from the module with minor edits from me