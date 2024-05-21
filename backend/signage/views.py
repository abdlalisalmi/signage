from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404

from .models import Screen
from .serializers import ScreenSerializer, ScreenDetailSerializer


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
