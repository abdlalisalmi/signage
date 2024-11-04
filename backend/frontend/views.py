from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from signage.models import Screen, Content
from signage.serializers import (
    ScreenSerializer,
    ScreenDetailSerializer,
    ContentDetailSerializer,
)


def handler404(request, exception):
    return render(request, "errors/404.html", status=404)


class HomePageView(APIView):
    def get(self, request):
        queryset = Screen.objects.filter(is_active=True)
        secreens_data = ScreenSerializer(queryset, many=True).data
        return render(request, "index.html", {"screens": secreens_data})


class ScreenDetailView(APIView):
    def get(self, request, pk):
        try:
            screen = Screen.objects.get(pk=pk)
        except Screen.DoesNotExist:
            return render(request, "errors/404.html", status=404)
        screen_data = ScreenDetailSerializer(screen).data
        return render(request, "screen.html", {"screen": screen_data})
