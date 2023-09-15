from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# I wrote this code

# View of the main index page
def index(request):
    if request.user.is_authenticated:
        djangouser = request.user # get django user 
        user = AppUser.objects.get(user = djangouser) # get Appuser data corresponding to our django user
        pk= user.pk    #primary key of AppUser instance
        return render(request, 'chat/index.html', {'pk': pk })                 
    else:        
        return render(request, 'chat/index.html')   
    

# View of the home-page cutomised to each user
def user_home(request):   
    # Get user data.
    djangouser = request.user
    user = AppUser.objects.get(user = djangouser)
    name = djangouser.username
    organisation = user.organisation
    status= user.status
    photo = user.photo

    # get friendship data pertaining to the concerned user
    list_received_relations = Friendship.objects.filter(to_user= user)
    incoming_request_list = list_received_relations.filter(request_accepted= False)
    inc_friend_list = list_received_relations.filter(request_accepted= True) 
    list_sent_relations = Friendship.objects.filter(from_user= user)
    outgoing_request_list = list_sent_relations.filter(request_accepted= False)
    out_friend_list = list_sent_relations.filter(request_accepted= True)

    # render page with relevant data
    return render(request, 'chat/home.html', {  'user_name': name,
                                                'user_organisation':organisation,
                                                'user_status':status,
                                                'user_photo':photo,
                                                'incoming_request_list': incoming_request_list,
                                                'outgoing_request_list': outgoing_request_list,
                                                'inc_friend_list': inc_friend_list,
                                                'out_friend_list':out_friend_list,
                                               })

# View of the profile-page for each user (viewable to other users)
def profile(request,user_name):  

    # Public data about a user
    name = user_name
    djangouser =  User.objects.get(username = name)
    user = AppUser.objects.get(user = djangouser)    
    organisation = user.organisation
    status= user.status
    photo = user.photo
   
    return render(request, 'chat/profile.html', {'user_name': name,
                                               'user_organisation':organisation,
                                               'user_status':status,
                                               'user_photo':photo,
                                               })

# View of Action- "update status"
def update_status(request):
    #Get AppUser data based on Django User
    user = AppUser.objects.get(user = request.user)
    if request.method == 'POST':        
        status = request.POST['status'] #Posted status content
        user.status = status
        user.save()  # Saving record in the data model      
        return HttpResponseRedirect("../home/")   

# View of Action- "update status"
 
# View of "Friends and People" page for each user
def people(request):
    master_users = AppUser.objects.all() # Get list of all users in the database
    return render(request, 'chat/people.html', {'master_users': master_users,
                                               })
    
# View, when "Search for people" functionality is used
def search(request):
    master_users = AppUser.objects.all()
    final_result =[] # Stores only the people whose username is related to the search query

    # Not editing database, only retrieving records
    if request.method == 'GET':        
        query = request.GET['search']
        result = User.objects.filter(username__contains=query)         
        for user in result:
            final_result.append(AppUser.objects.get(user=user))          
        return render(request, 'chat/people.html', {'master_users': master_users, # All users
                                                    'search_results': final_result, # Filtered users
                                               }) 

# View for when a friend request is initiated.  
def friend_request(request):
    if request.method == 'POST':
        to_user = request.POST['profile_userName'] # Receiver of friend request
        to_user = AppUser.objects.get(user=User.objects.get(username=to_user))
        from_user = request.user # Sender of friend request
        from_user= AppUser.objects.get(user= from_user)

        # Only send the friend request if it hasnt been sent yet.
        try:
            test_friendship = Friendship.objects.get(from_user= from_user,
                                                    to_user = to_user)
        except:
            row= Friendship.objects.create(from_user= from_user,
                                            to_user = to_user,
                                            request_accepted = False)
            row.save()        
        return HttpResponse("Friend request has been sent")
    
# View for when a friend request is accepted.    
def request_acceptance (request):
    if request.method == 'POST':
        # Each relationship/friendship has a unique id
        friendship_id = request.POST['friendship_id']
        friendship = Friendship.objects.get(friendship_id= friendship_id)
        friendship.request_accepted = True # change status of friendship to confirmed
        friendship.save()
        return HttpResponseRedirect("../home/") 

# View for posting-profile-photo action    
def photo(request):
    user = AppUser.objects.get(user = request.user)
    if request.method == 'POST':              
        photo = request.FILES
        user.photo = photo
        user.save()    # saving profile photo to database    
        return HttpResponseRedirect("../home/")  
    
# end of code I wrote


# Start of code from module with minor edits by me
# View for logout functionality
@login_required  
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('../')

# View for Registration functionality
def register(request):        
    registered = False #Initilise this variable as false
    # After registration form is filled and posted
    if request.method == 'POST':        
        user_form = UserForm(request.POST, request.FILES)
        profile_form = UserProfileForm(request.POST, request.FILES)
        # Validation of form
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            # 'organisation' data can be left blank.
            if 'organisation' in user_form.cleaned_data:
                profile.organisation = request.DATA['organisation']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:        
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'chat/register.html',
                  {'user_form': user_form,
                    'profile_form': profile_form,
                    'registered': registered ,})

# View for Login functionality
def user_login(request):
    master_genes = AppUser.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("../")
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'chat/login.html', {'master_genes': master_genes})

def room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name })

# End of code from module with minor edits by me