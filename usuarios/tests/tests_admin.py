from . import *

# Create your tests here.
class UserTests(UserTests):
    def setUp(self) -> None:
        self.user = Usuario.objects.create_superuser(
            name='master',
            last_name='root',
            password='admin123',
            email='admin@gmail.com'
        )

        self.data_login = {
            'password':'admin123',
            'email':'admin@gmail.com'
        }

        
        return super().setUp()
    
    def test_login(self):
        respose = self.client.post(
                path=self.urls['login'],
                data=self.data_login,
                format=self.format
            )
        self.assertTrue(self.client.login(**self.data_login))     
        self.assertNotEquals(respose.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(respose.status_code, status.HTTP_200_OK)

    def test_exist_token(self):
        response = self.client.post(
            self.urls['login'],
            self.data_login,
            format=self.format
        )
    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.client.login(**self.data_login))
        self.assertContains(response,response.data['token'])