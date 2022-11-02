from .models import Bot
from .serializers import BotSerializer
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated



class BotViewSet(viewsets.ModelViewSet):
    queryset = Bot.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BotSerializer