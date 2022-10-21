from . import Faker, Usuario

class UserFactory:
    faker = Faker()

    def built_user(self):
        return{
            'name': self.faker.name(),
            'last_name': f'{self.faker.name()} last',
            'email': self.faker.email(),
            'password': 'contrasena',
        }

    def bulit_admin(self):
        return {
            'name': 'master',
            'last_name': 'root',
            'email': 'administrador@gmail.com',
            'password': 'masterbot',
        }
    
    def create_user(self):
        return Usuario.objects.create_user(**self.built_user())
    
    def create_admin(self):
        return Usuario.objects.create_superuser(**self.bulit_admin())