from django.db import models
from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget


from .models import Screen, Playlist, Content


@admin.register(Screen)
class ScreenAdminClass(ModelAdmin):

    readonly_fields = ["slug", "created_at", "updated_at"]
    list_display = [
        "display_name",
        "display_playlists",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active"]
    search_fields = ["name"]

    fieldsets = (
        (None, {"fields": ("name", "description", "is_active")}),
        ("Playlists", {"fields": ("playlists",)}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
    filter_horizontal = ["playlists"]

    @admin.display(description="Screen name")
    def display_name(self, obj):
        return obj.name.capitalize()

    @admin.display(description="Playlists")
    def display_playlists(self, obj):
        playlists = obj.playlists.filter(is_active=True)
        if playlists.count() == 0:
            return "No playlists"
        return ", ".join([playlist.name.capitalize() for playlist in playlists])


@admin.register(Playlist)
class PlaylistAdminClass(ModelAdmin):

    readonly_fields = ["created_at", "updated_at"]
    list_display = [
        "display_name",
        "display_contents",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active"]
    search_fields = ["name"]
    filter_horizontal = ["contents"]

    fieldsets = (
        (None, {"fields": ("name", "is_active")}),
        ("Contents", {"fields": ("contents",)}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    @admin.display(description="Playlist name")
    def display_name(self, obj):
        return obj.name.capitalize()

    @admin.display(description="Contents")
    def display_contents(self, obj):
        contents = obj.contents.filter(is_active=True)
        if contents.count() == 0:
            return "No contents"
        return f"{contents.count()} contents"


@admin.register(Content)
class ContentAdminClass(ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_display = ["display_name", "type", "is_active", "created_at", "updated_at"]
    list_filter = ["type"]
    search_fields = ["name"]

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }

    fieldsets = (
        (None, {"fields": ("name", "type", "is_active")}),
        ("Content", {"fields": ("url", "file", "text", "duration")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    @admin.display(description="Content name")
    def display_name(self, obj):
        return obj.name.capitalize()
