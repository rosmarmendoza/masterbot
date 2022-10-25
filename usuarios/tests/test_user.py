from . import *

class UserTests(UserTests, APITestCase):
    def setUp(self) -> None:
        self.user = Usuario.objects.create_user(
            name='normal',
            last_name='user',
            password='usuario',
            email='usuario@gmail.com'
        )

        self.data_login = {
            'password':'usuario',
            'email':'usuario@gmail.com'
        }

        return super().setUp()

    