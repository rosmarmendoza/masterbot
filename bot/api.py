from .models import Bot
from .serializers import BotSerializer
from rest_framework import viewsets, permissions

class BotViewSet(viewsets.ModelViewSet):
    queryset = Bot.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BotSerializer