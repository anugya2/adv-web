# Code from module with minor edits from me

#To make the chat functionality asynchronous.
import os
from django.core.asgi import get_asgi_application

# locate settings for the app
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat_example.settings")
application = get_asgi_application()

# End of code from module with minor edits from me
