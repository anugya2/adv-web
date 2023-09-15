# Code from module with minor edits from me

from celery import shared_task
from PIL import Image as img #image manipulation package
from .models import *
from django.core.files.uploadedfile import SimpleUploadedFile #insert into database
import io

@shared_task #task decorator
def make_thumbnail(record_pk):
    # get record from database
    record = Image.objects.get(pk=record_pk)
    # open the image before scaling the size
    image = img.open('images/'+str(record.image))
    x_scale_factor = image.size[0]/100
    thumbnail = image.resize((100, int(image.size[1]/x_scale_factor)))
    thumbnail.save("test.png")
    # save the image to django file after reading it
    byteArr = io.BytesIO()
    thumbnail.save(byteArr, format='png')
    file = SimpleUploadedFile("thumb_"+str(record.image), byteArr.getvalue())
    record.thumbnail = file
    record.save()   

# End of code from module with minor edits from me