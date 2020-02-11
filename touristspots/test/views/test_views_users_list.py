from django.test import TestCase, Client
from rest_framework import status
from rest_framework.utils import json


class UserViewSetTestCase(TestCase):
    def setUp(self):
        self.route = '/api/users/'
        self.c = Client()

    def test_access_list_user_with_anonimous_user(self):
        response = self.c.get('/api/users/')
        content = json.loads(response.content)

        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEquals(content['detail'], "Authentication credentials were not provided.")
