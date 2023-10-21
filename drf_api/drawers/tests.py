from django.contrib.auth.models import User
from .models import Drawer
from rest_framework import status
from rest_framework.test import APITestCase


class DrawerListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='chris', password='pass')

    def test_can_list_drawers(self):
        chris = User.objects.get(username='chris')
        Drawer.objects.create(owner=chris, title='a title')
        response = self.client.get('/drawers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

#     def test_logged_in_user_can_create_drawer(self):
#         self.client.login(username='chris', password='pass')
#         response = self.client.post('/drawers/', {'title': 'a title'})
#         count = Drawer.objects.count()
#         self.assertEqual(count, 1)  
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_user_not_logged_in_cant_create_drawer(self):
#         response = self.client.post('/drawers/', {'title': 'a title'})
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)    

class DrawerDetailViewTests(APITestCase):
    def setUp(self):
        chris = User.objects.create_user(username='chris', password='pass')
        fred = User.objects.create_user(username='fred', password='pass')
        Drawer.objects.create(
            owner=chris, title='a title', description='Chris content'
        )
        Drawer.objects.create(
            owner=fred, title='another title', description='Freds content'
        )

    def test_can_retrieve_drawer_using_valid_id(self):
        response = self.client.get('/drawers/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_drawer_using_invalid_id(self):
        response = self.client.get('/drawers/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_drawer(self):
        self.client.login(username='chris', password='pass')
        response = self.client.put('/drawers/1/', {'title': 'asdf'})
        drawer = Drawer.objects.filter(pk=1).first()
        self.assertEqual(drawer.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        self.client.login(username='chris', password='pass')
        response = self.client.put('/drawers/2/', {'title': 'asdf'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
