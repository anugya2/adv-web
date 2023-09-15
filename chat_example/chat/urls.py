# I wrote this code

from django.urls import path
from django.contrib.auth.decorators import login_required
from . import api
from . import views
urlpatterns = [
    # 1. Index page (differentiation between loggedn in / public in templates)
    path('', views.index, name='index'),

    # 2. Registration page
    path('register/', views.register, name='register'),

    # 3. Login page
    path('login/', views.user_login, name='login'),
    
    # Login required is ensured in views
    # 4 Logout url, home page and people page for each user)
    path('logout/',  views.user_logout, name='logout'),    
    # 5 Home page of user
    path('home/', views.user_home, name='home'),
    # 6 People/Friends page of user
    path('people/', views.people, name='people'),

    # 7. Chat room Page
    path('chat/<str:room_name>/', views.room, name='room'),

    # 8. Profile page
    path('profile'+'<str:user_name>/', views.profile, name='profile'),

    # 9. Status url
    path('status/', views.update_status, name='status'),
    
    # 10. Search url
    path('search/', views.search, name='search'),

    # 11. Friend request initiation url
    path('friend_request/', views.friend_request, name='friend_request'),#send.friend.request
    
    # 12. Friend request acceptance url
    path('request_acceptance/', views.request_acceptance, name='request_acceptance'),#accept.friend.request
    
    # 13. Profile photo url
    path('photo/', views.photo, name="photo"),

    # 14. User images url
    path('api/image/', api.ImageDetail.as_view(), name="image_api"),
    path('api/images/', api.ImageList.as_view(), name="images_api"),

    # 15. User data api 
    path('api/userData/<int:pk>', api.UserData.as_view(), name="userData_api"),
    
    # 16. Friendship data api 
    path('api/friendshipData/<int:pk>', api.FriendshipData.as_view(), name="friendshipData_api"),
]

# end of code I wrote


# path('people/', login_required(login_url='login'), views.people, name='people'),

