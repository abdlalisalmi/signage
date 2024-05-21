from rest_framework import serializers
from .models import Screen


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        exclude = ["playlists", "created_at", "updated_at"]


class ScreenDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = "__all__"
        depth = 2
