from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Usuario
from .factory import UserFactory

class UserTests():
    def setUp(self) -> None:
        Faker.seed(45)
        faker = Faker()
        self.user_factory = UserFactory()
        self.urls = {
            'login':'/user/auth',
            'create':'/user/create'
        }

        self.format = 'json'
        

        self.data_bad_login = {
            'password':'no hay',
            'email':'qwe@gmail.com'
        }

        return super().setUp()

    #test para probar cuando se quiere authentificar con datos erroneos
    def test_bad_login(self):
        respose = self.client.post(
            path= self.urls['login'],
            data= self.data_bad_login,
            format=self.format
            )

        self.assertFalse(self.client.login(**self.data_bad_login))     
        self.assertNotEquals(respose.status_code, status.HTTP_200_OK)
        self.assertEquals(respose.status_code, status.HTTP_400_BAD_REQUEST)
    
    #test para probar cuando no ingresa todos los credenciales
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

    #test para probar cuando no ingresa algun credencial
    def test_faltan_credenciales(self):
        response = self.client.post(
            path=self.urls['login'],
            data={ 'email':'admin@gmail.com' },
            format=self.format
        )

        self.assertFalse(self.client.login(**self.data_bad_login))
        self.assertNotEquals(response.status_code, status.HTTP_200_OK)

    #test para probar cuando se quiere authentificar con datos correctos
    def test_login(self):
        respose = self.client.post(
                path=self.urls['login'],
                data=self.data_login,
                format=self.format
            )
        self.assertTrue(self.client.login(**self.data_login))     
        self.assertNotEquals(respose.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(respose.status_code, status.HTTP_200_OK)

    #test para ver si decuelve un token
    def test_exist_token(self):
        response = self.client.post(
            self.urls['login'],
            self.data_login,
            format=self.format
        )
    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.client.login(**self.data_login))
        self.assertContains(response,response.data['token'])


    def test_create(self):
        data = self.user_factory.bulit_admin()
      
        response = self.client.post(
            self.urls['create'],
            {
                **data,
                "remember_password":"remember"
            },
            format=self.format
        )
        
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(self.client.login(**{
            "email":data['email'],
            "password": data["password"]
        }
        ))
        self.assertIn("Usuario creado",response.data['message'])

    def test_bad_create(self):
        data = self.user_factory.bulit_admin()
      
        response = self.client.post(
            self.urls['create'],
            {
            },
            format=self.format
        )
        
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(self.client.login(**{
            "email":data['email'],
            "password": data["password"]
        }
        ))