# Code from module with minor edits from me

from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

#Include celery configurations for django here.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_example.settings') #Location for django settings
app = Celery('chat_example',  broker='redis://localhost/', backend='redis://localhost/') #initiate celery
app.config_from_object('django.conf:settings' , namespace = 'CELERY') 
app.autodiscover_tasks()

# End of code from module with minor edits from me