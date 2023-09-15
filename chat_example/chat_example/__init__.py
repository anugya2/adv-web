# Code from module with minor edits from me

from .celery import app as celery_app #import the celery application
__all__ = ('celery_app',) #loads the celery app when django starts

# End of code from module with minor edits from me