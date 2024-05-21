from django.urls import path
from .views import ScreensList

urlpatterns = [
    path("screens/", ScreensList.as_view({"get": "list"}), name="screens_list"),
    path(
        "screens/<int:pk>/",
        ScreensList.as_view({"get": "retrieve"}),
        name="screens_detail",
    ),
]
