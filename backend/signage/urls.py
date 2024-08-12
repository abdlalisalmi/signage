from django.urls import path
from .views import ScreensList, ContentPreviw, TestView

urlpatterns = [
    path(
        "test/", TestView.as_view(), name="test"
    ),  # This is the only path that is not used in the frontend
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
