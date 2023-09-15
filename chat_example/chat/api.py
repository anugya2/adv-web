from rest_framework import generics
from rest_framework import mixins
from .models import *
from .serializers import *
from django.http import HttpResponseRedirect
from .tasks import *

class ImageDetail(mixins.CreateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    def perform_create(self, serializer):
        record = serializer.save()
        make_thumbnail.delay(record.pk)
    def create(self, request, *args, **kwargs):
        response = super(ImageDetail, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='../../home/')
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)   

class ImageList(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageListSerializer

# I wrote this code

# API that gives data about a user
class UserData( mixins.RetrieveModelMixin,
                 generics.GenericAPIView):
    # Use integer pk in place of user which is an object
    lookup_field = "pk" 
    queryset = AppUser.objects.all()
    serializer_class = UserDataSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
# API that gives out data about friends of an user (Both confirmed and unconfirmed friends)
class FriendshipData(generics.ListAPIView,mixins.RetrieveModelMixin):
    friendships = Friendship.objects.all()
    # Filter friendships pertaining to this user.
    def get_queryset(self):
        filtered_friendship =[x for x in self.friendships if ( x.to_user.pk==self.kwargs['pk'] 
                                                               or x.from_user.pk==self.kwargs['pk'] )]
                                                            # Both received and sent frienships
        
        return filtered_friendship
    serializer_class = FriendshipDataSerializer

# end of code I wrote 


    

