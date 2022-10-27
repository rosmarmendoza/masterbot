## Requisitos
* Python 3.9 o superiror
* pip
* virtualenv
## Instalación
 1. Crear una carpeta que contendrá el repositorio y el entorno virtual.
 2. Dentro de ella crear un entorno virtual usando virtualenv. virtualenv venv
 3. Activar el entorno en Linux. source venv/bin/activate
 4. Clona el repositorio con:
 5. Instala los requerimientos con:

 6. pip install -r requirements.txt
 7. Ejecutar migraciones:
    python manage.py migrate
## Ejecución
python manage.py runserver

### Para probar Login y obtener un token válido deberá enviar una petición de tipo POST a http://127.0.0.1:8000/user/auth definir en un FormData las siguientes atributos:
    email => email
    password => contraseña 
Como respuesta visualizará el access token y refresh token.

## Urls:
### api rest
    Listar
        http://127.0.0.1:8000/user/list
        http://127.0.0.1:8000/user/list/<int:id>
    Crear
        http://127.0.0.1:8000/user/create
    Actualizar
        http://127.0.0.1:8000/user/update/<int:id>
    Eliminar
        http://127.0.0.1:8000/user/delete/<int:id>
