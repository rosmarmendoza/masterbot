from . import *

# Create your tests here.
class UserTests(UserTests, APITestCase):
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

   