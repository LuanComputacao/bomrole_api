from django.test import TestCase, Client
from rest_framework import status
from rest_framework.utils import json


class ToutirstSpotViewSetTestCase(TestCase):
    def setUp(self):
        self.route = '/api/touristspots/'
        self.c = Client()

    def test_access_list_tourist_spots_with_anonimous_user(self):
        response = self.c.get(self.route)
        content = json.loads(response.content)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content, [])

    def test_list_has_one_tourist_spot(self):
        response = self.c.get(self.route)
        content = json.loads(response.content)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(content), 1)
