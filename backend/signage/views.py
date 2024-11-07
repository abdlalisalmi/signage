from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from django.shortcuts import get_object_or_404, render
from django.utils.safestring import mark_safe


from .models import Screen
from .serializers import (
    ScreenSerializer,
    ScreenDetailSerializer,
    ContentDetailSerializer,
)
from .utils import get_contents_progress, get_signage_kpi


def dashboard_callback(request, context):

    context.update(
        {
            "kpi": get_signage_kpi(),
            "progress": get_contents_progress(),
        }
    )

    return context


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
