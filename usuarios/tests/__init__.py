from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Usuario
from .factory import UserFactory

class UserTests(APITestCase):
    def setUp(self) -> None:
        Faker.seed(45)
        faker = Faker()

        self.urls = {
            'login':'/user/auth',
            'create':'create_user'
        }

        self.format = 'json'
        

        self.data_bad_login = {
            'password':'no hay',
            'email':'qwe@gmail.com'
        }

        return super().setUp()

    def test_bad_login(self):
        respose = self.client.post(
            path= self.urls['login'],
            data= self.data_bad_login,
            format=self.format
            )

        self.assertFalse(self.client.login(**self.data_bad_login))     
        self.assertNotEquals(respose.status_code, status.HTTP_200_OK)
        self.assertEquals(respose.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_sin_cresenciales(self):
        response = self.client.post(
            path=self.urls['login'],
            data={ },
            format=self.format
        )
        self.assertFalse(self.client.login(**self.data_bad_login))     
        self.assertNotEquals(response.status_code, status.HTTP_200_OK) 
        self.assertIn('error',response.data)
        self.assertEqual(response.data['error'], 'el usario con estas credenciales no existe')

    def test_faltan_credenciales(self):
        response = self.client.post(
            path=self.urls['login'],
            data={ 'email':'admin@gmail.com' },
            format=self.format
        )

        self.assertFalse(self.client.login(**self.data_bad_login))
        self.assertNotEquals(response.status_code, status.HTTP_200_OK)

   