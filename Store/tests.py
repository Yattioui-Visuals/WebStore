import datetime

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class WebstoreTest(APITestCase):
    """
    I started working on my testcase , had to learn how Api's got tested, but wasn't too hard to get into
    Due to my time , I didnt have enough time to create full tests, but I do believe it shows I was going the right way
    """

    def setup(self):
        self.client = APIClient()

    def create_user(self):
        self.username = "test_admin"
        self.password = User.objects.make_random_password()
        user, created = User.objects.get_or_create(username=self.username)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        self.user = user

    def login(self):
        self.create_user()
        self.client.login(username=self.username, password=self.password)

    def test_create_customer(self):
        """
        Ensure we can create a new Customer object.
        """
        self.login()

        url = reverse('customer')
        data = {
            'first_name': 'Annakin',
            'last_name': 'Skywalker',
            'birth_date': '05-12-1999',
            'email': 'dark@force.nl',
            'street_name': 'Galaxy',
            'house_number': '7th',
            'postal_code': '5434TU',
            'user': 'test_admin',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_product(self):
        """
        Ensure we can create a new Product object.
        """
        self.login()

        url = reverse('products')
        data = {
            'product_name': 'lightsaber',
            'product_description': 'does damage',
            'price': '50.0',
            'ean': '50023212LO',
            'stock': '10'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
