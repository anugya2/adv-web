# I wrote this code
from .serializers import *
import json
from django.urls import reverse
from rest_framework.test import APITestCase
from .model_factories import *
from .serializers import *

# Custom function to avoid repitition. 
# (Deletes database to start tests with empty test database.)
def deleteObj(self):
    User.objects.all().delete()
    AppUser.objects.all().delete()
    Friendship.objects.all().delete()
    Image.objects.all().delete()

#Tests for the API's and Serialisers:

#Tests User data API       
class UserDataTest(APITestCase): 
    user1 = None
    user2 = None
    good_url = ''
    bad_url = ''
    delete_url = ''

    def setUp(self):
        self.user1 = AppUserFactory.create(user=UserFactory.create(username ="Dolly"))
        self.user2  = AppUserFactory.create(user=UserFactory.create(username ="Molly"))
        self.user3  = AppUserFactory.create(user=UserFactory.create(username ="Sally"))                
        self.good_url = reverse('userData_api', kwargs={'pk':  1})
        self.bad_url = "api/userData/H/"
        self.delete_url = reverse('userData_api', kwargs={'pk': 2})

    def tearDown(self):
        deleteObj(self)

    # Checks if expected data is returned
    def test_userDetailReturnsSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200) # 404 is incorrect/ error, 200 is correct/success
        data = json.loads(response.content)
        self.assertTrue('status' in data)
        self.assertEqual(data['organisation'], "Hobby association society")

    # Expected failure used as a control
    def test_userDetailReturnFailOnBadPk(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)

#Tests Friendship data API
class FriendshipDataTest(APITestCase):     
    friendship1 = None    
    friendship2 = None
    good_url = ''
    bad_url = ''
    delete_url = ''

    # Setting up friendship networks to test
    def setUp(self): 
        # Friendship network 1
        user1 = AppUserFactory.create(pk=11)
        user2 = AppUserFactory.create(pk=22)
        user3 = AppUserFactory.create(pk=33)
        self.friendship1 = FriendshipFactory.create(from_user= user1, to_user= user2 )
        self.friendship2 = FriendshipFactory.create(from_user= user3, to_user= user1 )
        # Friendship network 2
        user4 = AppUserFactory.create(pk=44)
        user5 = AppUserFactory.create(pk=55)
        self.friendship3 = FriendshipFactory.create(from_user= user4, to_user= user5)
        
        self.good_url = reverse('friendshipData_api', kwargs={'pk':  11})
        self.bad_url = "api/friendshipData/H/"
        self.delete_url = reverse('friendshipData_api', kwargs={'pk': 44})

    def tearDown(self):
        deleteObj(self)

    # Checks if expected data is returned
    def test_friendshipDetailReturnsSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200) # 404 is incorrect/ error, 200 is correct/success
        data = json.loads(response.content)
        self.assertTrue('friendship_id' in data[0])
        self.assertEqual(type(data[0]['friendship_id']), int)

    # Checks if correct number of data rows are returned
    def test_correctNumberofRelations(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200) # 404 is incorrect/ error, 200 is correct/success
        data = json.loads(response.content)
        self.assertTrue(len(data) is 2)
        
    # Expected failure used as a control
    def test_friendshipDetailReturnFailOnBadPk(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)

#Tests Friendship data Serialiser
class FriendshipDataSerializerTest(APITestCase):
    friendship1 = None
    friendshipserializer = None

    # Initialising Friendship instance and its serialiaser
    def setUp(self):
        self.friendship1 = FriendshipFactory.create()
        self.friendshipserializer = FriendshipDataSerializer(instance=self.friendship1 )

    # Emptying test database
    def tearDown(self):
        deleteObj(self)

    # Data attributes as expected
    def test_friendshipSerilaiser(self): 
        data = self.friendshipserializer.data
        self.assertEqual(set(data.keys()), set(['friendship_id', 'from_user', 'to_user', 'request_accepted']))
   
    # Data values as expected
    def test_friendshipSerilaiserfriendshipIDIsHasCorrectData(self):
        data = self.friendshipserializer.data
        self.assertEqual(type(data['friendship_id']), int) 

#Tests Friendship data Serialiser
class UserDataSerializerTest(APITestCase):
    # Initialising User instance and user data serialiaser
    user = None
    userserializer = None
    def setUp(self):
        self.user = AppUserFactory.create()
        self.userserializer = UserDataSerializer(instance=self.user )

    # Emptying test database
    def tearDown(self):
        deleteObj(self)

    # Data attributes as expected
    def test_userDataSerilaiser(self): 
        data = self.userserializer.data
        self.assertEqual(set(data.keys()), set(['user', 'organisation', 'status', 'photo']))

    # Data values as expected
    def test_userDataSerilaiseruserIDIsHasCorrectData(self):
        data = self.userserializer.data
        self.assertEqual(type(data['organisation']), str) 

# Test for Image detail api for user images'
class ImageDetailTest(APITestCase):   
    bad_url = ''
    def setUp(self):  
        self.bad_url = "/api/image/"    
        def test_ImageDetailReturnFailOnBadPk(self):
            response = self.client.get(self.bad_url, format='json')
            response.render()
            self.assertEqual(response.status_code, 405) # 404 is incorrect/ error, 200 is correct/success

# Test for Image list serialiser
class ImageListSerializerTest(APITestCase):
    # Initialisation and clearing database
    image = None
    imageListSerializer = None
    def setUp(self):
        self.image = ImageFactory.create()
        self.imageListSerializer = ImageListSerializer(instance=self.image )
    def tearDown(self):
        deleteObj(self)
    # Expected data attribute list
    def test_imageListSerilaiser(self): 
        data = self.imageListSerializer.data
        self.assertEqual(set(data.keys()), set(['name', 'image', 'thumbnail', 'user']))
    # Expected data values
    def test_imageListSerialiserHasCorrectData(self):
        data = self.imageListSerializer.data
        self.assertEqual(type(data['name']), str)

# end of code I wrote