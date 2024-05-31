from django.db import models
from django import forms
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.http import HttpRequest
from django.utils import timezone
from unfold.admin import ModelAdmin
from unfold.decorators import display
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.contrib.filters.admin import (
    RangeDateFilter,
)


from .models import Screen, Playlist, Content


class ContentAdminForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if (
            not self.instance.pk
        ):  # Only set the initial value when creating a new instance
            self.fields["starts_at"].initial = timezone.now()


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
    form = ContentAdminForm
    readonly_fields = ["created_at", "updated_at"]
    list_display = [
        "display_name",
        "type",
        "display_status",
        "starts_at",
        "ends_at",
    ]
    list_filter = ["type"]
    search_fields = ["name"]

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }

    fieldsets = (
        (
            None,
            {"fields": (("name", "type"),)},
        ),
        (
            "Content (Fill one of the following)",
            {"fields": ("url", "file", "text")},
        ),
        (
            "Content Display Time",
            {"fields": ("duration", "starts_at", "ends_at", "is_active")},
        ),
        ("Important dates", {"fields": ("created_at", "updated_at")}),
    )

    @display(description="Content name")
    def display_name(self, obj):
        name = obj.name.capitalize()
        return name[:30] + "..." if len(name) > 30 else name

    @display(
        description="Status",
        label={
            "Scheduled": "info",
            "Active": "success",
            "Inactive": "danger",
            "Expired": "danger",
        },
    )
    def display_status(self, obj):
        if not obj.is_active:
            return "Inactive"

        if obj.starts_at > timezone.now():
            return "Scheduled"
        elif obj.ends_at and obj.ends_at < timezone.now():
            return "Expired"
        return "Active"


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    date_hierarchy = "action_time"
    readonly_fields = [
        "user",
        "content_type",
        "object_id",
        "object_repr",
        "action_flag",
        "change_message",
    ]
    list_display = [
        "action_time",
        "user",
        "display_content_type",
        "object_id",
        "display_object_repr",
        "action_flag",
        "display_change_message",
    ]
    list_filter = [
        "action_flag",
        # ("action_time", RangeDateFilter),
    ]
    search_fields = ["object_repr", "change_message"]
    ordering = ["-action_time"]
    actions = None
    list_per_page = 30
    list_select_related = True
    date_hierarchy = "action_time"
    # save_as = True
    # save_on_top = True
    preserve_filters = False
    # inlines = None

    fieldsets = (
        (
            "Log Entry Details",
            {
                "fields": (
                    ("user", "action_time"),
                    "content_type",
                    ("object_id", "action_flag"),
                    "object_repr",
                    "change_message",
                )
            },
        ),
    )

    @display(description="Object Representation")
    def display_object_repr(self, obj):
        st = str(obj.object_repr)
        return st[:20] + "..." if len(st) > 20 else st

    @display(description="Model")
    def display_content_type(self, obj):
        return obj.content_type.model.capitalize()

    @display(description="Change Message")
    def display_change_message(self, obj):
        st = str(obj.change_message)
        return st[:30] + "..." if len(st) > 30 else st
