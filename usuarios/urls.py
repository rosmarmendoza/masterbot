from rest_framework import routers
from .api import UsuarioViewSet

router = routers.DefaultRouter()

router.register('api/usuario', UsuarioViewSet, 'usuarios')

urlpatterns = router.urls