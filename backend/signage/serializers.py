from rest_framework import serializers
from django.utils import timezone
from .models import Screen, Content


class ContentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        exclude = ["created_at", "updated_at"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["playlists"] = [
            {
                "id": playlist.id,
                "name": playlist.name,
            }
            for playlist in instance.playlists.filter(is_active=True)
        ]
        return data


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        exclude = ["created_at", "updated_at"]


class ScreenDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["contents"] = []
        contents = []
        now = timezone.now()
        for playlist in instance.playlists.filter(is_active=True):
            active_contents = playlist.contents.filter(
                is_active=True,
                starts_at__lte=now,
            ).exclude(ends_at__lt=now)
            contents.extend(active_contents)

        if active_contents.exists():
            data["contents"] = ContentDetailSerializer(
                active_contents.distinct().order_by("id"), many=True
            ).data
        return data
