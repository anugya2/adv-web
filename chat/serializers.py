# I wrote this code

#Imports
from rest_framework import serializers
from .models import *

# Serialiser for user's images' details
class ImageSerializer(serializers.ModelSerializer):

    # Retrieval of data
    class Meta:
        model = Image
        fields = ['name', 'image', 'user']
    
    # Creation of data
    def create (self, validated_data):
        user = self.context['request'].user.username # Get current user's name        
        img = Image(**{**validated_data, 
                       'user': user,  # Add data about which user the image belongs to
                       })
        img.save() # Save image data
        return img


# Serialiser for list if images in the database 
class ImageListSerializer(serializers.ModelSerializer):
    # For retrieval
    class Meta:
        model = Image
        fields = ['name', 'image', 'thumbnail', 'user']

# Serialiser for Django User data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'last_login', 'date_joined'] 

# Serialiser for User data API
class UserDataSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = AppUser
        fields = ['user', 'organisation', 'status', 'photo']

# Serialiser for Profile name for a Django user to be used inside another serialiser
class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

# Serialiser for Profile data about a user
class ProfileSerializer(serializers.ModelSerializer):
    user = ProfileUserSerializer()
    class Meta:
        model = AppUser
        fields = ['user', 'organisation', 'status', 'photo']

# Serialiser for Friendship data
class FriendshipDataSerializer(serializers.ModelSerializer):
    from_user = ProfileSerializer() # Sub serialisers required
    to_user = ProfileSerializer()
    class Meta:
        model = Friendship
        fields = ['friendship_id', 'from_user', 'to_user', 'request_accepted']

# end of code I wrote 