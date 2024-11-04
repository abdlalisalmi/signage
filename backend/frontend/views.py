from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from signage.models import Screen, Content
from signage.serializers import (
    ScreenSerializer,
    ScreenDetailSerializer,
    ContentDetailSerializer,
)


class HomePageView(APIView):
    def get(self, request):
        queryset = Screen.objects.filter(is_active=True)
        secreens_data = ScreenSerializer(queryset, many=True).data
        return render(request, "index.html", {"screens": secreens_data})


class ScreenDetailView(APIView):
    def get(self, request, pk):
        screen = get_object_or_404(Screen, pk=pk)
        screen_data = ScreenDetailSerializer(screen).data
        return render(request, "screen.html", {"screen": screen_data})
