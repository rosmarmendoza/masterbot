from rest_framework import routers
from .api import BotViewSet

router = routers.DefaultRouter()
router.register('api/bot', BotViewSet, 'bot')

urlpatterns = router.urls
