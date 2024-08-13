from django.urls import path
from .views import HomePageView, ScreenDetailView

app_name = "frontend"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("screens/", HomePageView.as_view(), name="screens_list"),
    path("screens/<int:pk>/", ScreenDetailView.as_view(), name="screen_detail"),
]
