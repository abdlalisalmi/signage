from django.urls import path
from .views import ScreensList, ContentPreviw

app_name = "signage"

urlpatterns = [
    path("screens/", ScreensList.as_view({"get": "list"}), name="screens_list"),
    path(
        "screens/<int:pk>/",
        ScreensList.as_view({"get": "retrieve"}),
        name="screens_detail",
    ),
    path(
        "contents/<int:pk>/preview/",
        ContentPreviw.as_view({"get": "retrieve"}),
        name="content_preview",
    ),
]
