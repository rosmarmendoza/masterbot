from dataclasses import fields
from rest_framework import serializers
from .models import Bot

class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('id', 'name', 'token', 'welcome_message', 'user', 'created_at')
        read_only_fields = ('created_at',)