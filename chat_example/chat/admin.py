# I wrote this code

from django.contrib import admin
from .models import *

# All the 3 tables/ORM models of our database:
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('user','organisation','status','photo')    

class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('friendship_id','from_user','to_user','request_accepted') 

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name','image', 'thumbnail','user' )


#registering data models and their respective admin classes
admin.site.register(AppUser,AppUserAdmin )
admin.site.register(Friendship, FriendshipAdmin)
admin.site.register(Image, ImageAdmin)

# end of code I wrote