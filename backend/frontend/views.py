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
        return render(request, "errors/error.html")
        # if response.status_code == 200:
        #     screens_data = response.data
        # else:
        #     screens_data = []

        # # You can now use the screens_data in your response or further processing
        # return Response({"screens_data": screens_data})

        return render(request, "index.html")
