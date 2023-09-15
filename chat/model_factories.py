# I wrote this code

import factory
from .models import *
import factory.faker #Creates random username and email ids

# Create Django users for testing
class UserFactory(factory.django.DjangoModelFactory):    
    username = factory.Faker("name")
    email = factory.Faker("email")
    password ="dehw"
    class Meta:
        model = User

# Create App users for testing
class AppUserFactory(factory.django.DjangoModelFactory):    
    user = factory.SubFactory(UserFactory)
    organisation = "Hobby association society"
    status = "Getting sun on the beach. Enjoying life"
    photo = "http://127.0.0.1:8080/images/images/test.jpg"
    class Meta:
        model = AppUser

# Create Frienships for testing
class FriendshipFactory(factory.django.DjangoModelFactory):
    # Do not initialise frienship_is as it is autoField.
    from_user = factory.SubFactory(AppUserFactory)
    to_user = factory.SubFactory(AppUserFactory)
    request_accepted  = True    
    class Meta:
        model = Friendship

# Create image instances for testing
class ImageFactory(factory.django.DjangoModelFactory):   
    name = "photoey" 
    image = "http://127.0.0.1:8080/images/images/test.jpg"
    thumbnail = "http://127.0.0.1:8080/images/images/test.jpg"   
    user = "Dominic"
    class Meta:
        model = Image

# end of code I wrote
   









