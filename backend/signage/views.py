from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404, render

from .models import Screen, Content
from .serializers import (
    ScreenSerializer,
    ScreenDetailSerializer,
    ContentDetailSerializer,
)


class TestView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return render(request, "test.html", {})


class ContentPreviw(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving screens.
    """

    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        content = get_object_or_404(Content, pk=pk)
        return Response(
            ContentDetailSerializer(content).data, status=status.HTTP_200_OK
        )


class ScreensList(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving screens.
    """

    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = Screen.objects.filter(is_active=True)
        serializer = ScreenSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        screen = get_object_or_404(Screen, pk=pk)
        serializer = ScreenDetailSerializer(screen)
        return Response(serializer.data, status=status.HTTP_200_OK)
