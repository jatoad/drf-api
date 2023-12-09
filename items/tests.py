from django.contrib.auth.models import User
from .models import Drawer
from .models import Item
from rest_framework import status
from rest_framework.test import APITestCase


class ItemListViewTests(APITestCase):
    def setUp(self):
        chaz = User.objects.create_user(username='chaz', password='pass')
        Drawer.objects.create(
            owner=chaz, title='a title', description='chaz content'
        )

    def test_can_list_items(self):
        chaz = User.objects.get(username='chaz')
        paleo_drawer = Drawer.objects.filter(pk=1).first()
        Item.objects.create(owner=chaz, drawer=paleo_drawer, description='a item')
        response = self.client.get('/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))


class ItemDetailViewTests(APITestCase):
    def setUp(self):
        chaz = User.objects.create_user(username='chaz', password='pass')
        Drawer.objects.create(
            owner=chaz, title='a title', description='chaz content'
        )

    def test_can_retrieve_item_using_valid_id(self):
        chaz = User.objects.get(username='chaz')
        paleo_drawer = Drawer.objects.filter(pk=1).first()
        Item.objects.create(owner=chaz, drawer=paleo_drawer, description='a item')
        response = self.client.get('/items/1/')
        self.assertEqual(response.data['description'], 'a item')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_item_using_invalid_id(self):
        response = self.client.get('/items/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)