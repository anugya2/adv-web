# I wrote this code

# Imports
from django.db import models
from django.contrib.auth.models import User

# ORM Model for user
class AppUser(models.Model):
    # Relates to Django User object.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    organisation = models.CharField(max_length=256, null=True, blank=True)

    # Changeable and can be added later
    status = models.CharField(max_length=1256, null=True, blank=True)
    
    photo = models.ImageField(upload_to='images/', null=True, blank=True)

    def __unicode__(self):
        return self.user.username

# ORM model for Friendship/ Relationship Link
# Process:
# Everytime a request is sent a new friendship object is created. 
# Once the receiver accepts, the attribute value  of request_acceptance changes to True 
# False request_accepted = Friendship initiated
# True request_accepted = Confirmed friendship 
class Friendship(models.Model):
    friendship_id = models.AutoField(auto_created = True, primary_key = True, serialize = False) 
    from_user = models.ForeignKey(AppUser,related_name='first_user', on_delete=models.DO_NOTHING)
    to_user = models.ForeignKey(AppUser,related_name='second_user', on_delete=models.DO_NOTHING)
    request_accepted = models.BooleanField()
    def __str__(self):
        return str(self.friendship_id)

# ORM model for Image data
class Image(models.Model):
    name = models.CharField(max_length=256, unique=True, db_index=True)
    image = models.FileField(blank=False)
    thumbnail = models.FileField(null=True)
    # Store owner of the image
    user = models.CharField(max_length=256,blank=True, null=True, db_index=True)
    def __str__(self):
        return self.name

# end of code I wrote 