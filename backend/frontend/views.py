from django.shortcuts import render
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.test import APIClient


class HomePageView(APIView):
    def get(self, request):
        # Reverse the URL of the ScreensList view
        url = reverse("signage:screens_list")
        # Make an internal GET request using APIClient
        client = APIClient()
        response = client.get(url)
        # Check if the request was successful

        if not response.status_code == 200:
            return render(request, "errors/error.html")
        screens_data = response.data

        return render(request, "index.html", {"screens": screens_data})


class ScreenDetailView(APIView):
    def get(self, request, pk):
        # Reverse the URL of the ScreensList view
        url = reverse("signage:screen_detail", args=[pk])
        # Make an internal GET request using APIClient
        client = APIClient()
        response = client.get(url)
        # Check if the request was successful

        if not response.status_code == 200:
            return render(request, "errors/error.html")
        screen_data = response.data

        print(screen_data, flush=True)

        return render(request, "screens/screen_detail.html", {"screen": screen_data})
