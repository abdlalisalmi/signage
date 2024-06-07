from django.db import models
from django import forms
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from django.http import HttpRequest
from django.utils import timezone
from unfold.admin import ModelAdmin
from unfold.decorators import display
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.contrib.filters.admin import (
    RangeDateFilter,
)
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from .models import Screen, Playlist, Content


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = [
        "display_header",
        "display_groups",
        "is_active",
        "is_superuser",
        "is_staff",
        "date_joined",
    ]
    search_fields = ["username", "email", "first_name", "last_name"]
    list_per_page = 30
    list_select_related = True
    # save_as = True
    # save_on_top = True
    list_filter = ["is_staff", "is_superuser", "is_active"]
    list_filter_submit = True
    preserve_filters = False
    # inlines = None
    readonly_fields = ["last_login", "date_joined"]

    @display(description="User", header=True)
    def display_header(self, instance: User):
        first_name = instance.first_name.capitalize() if instance.first_name else "."
        last_name = instance.last_name.upper() if instance.last_name else "."
        initials = f"{first_name[0].upper()}{last_name[0].upper()}"
        return (
            f"{first_name} {last_name}",
            instance.username,
            initials,
        )

    @display(description="Groups")
    def display_groups(self, instance: User):
        groups = ", ".join([group.name for group in instance.groups.all()])
        return groups if groups else "-"


@admin.register(Group)
class GroupAdmin(ModelAdmin):
    list_display = ["name", "display_users", "display_permissions"]
    search_fields = ["name"]
    list_per_page = 30
    list_select_related = True
    # save_as = True
    # save_on_top = True
    list_filter = []
    list_filter_submit = True
    preserve_filters = False
    filter_horizontal = ["permissions"]
    # inlines = None

    @display(description="Users")
    def display_users(self, instance: Group):
        users_count = instance.user_set.count()
        return f"{users_count} " + ("users" if users_count > 1 else "user")

    @display(description="Permissions")
    def display_permissions(self, instance: Group):
        permissions_count = instance.permissions.count()
        return f"{permissions_count} " + (
            "permissions" if permissions_count > 1 else "permission"
        )


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

    readonly_fields = ["created_at", "updated_at"]
    list_display = [
        "display_name",
        "display_playlists",
        "created_at",
        "updated_at",
        "display_status",
    ]
    list_filter = ["is_active"]
    search_fields = ["name"]

    fieldsets = (
        (None, {"fields": ("name", "description", "is_active")}),
        (
            "Important dates",
            {"fields": (("created_at", "updated_at"),)},
        ),
    )

    @display(description="Screen name")
    def display_name(self, obj):
        return obj.name.capitalize()

    @display(description="Status", label={"Active": "success", "Inactive": "danger"})
    def display_status(self, obj):
        return "Active" if obj.is_active else "Inactive"

    @display(description="Playlists")
    def display_playlists(self, obj):
        playlists = obj.playlists.filter(is_active=True)
        if playlists.count() == 0:
            return "No playlists assigned"
        return ", ".join(
            [
                (
                    playlist.name.capitalize()
                    if len(playlist.name) < 20
                    else playlist.name.capitalize()[0:20] + "..."
                )
                for playlist in playlists
            ]
        )


@admin.register(Playlist)
class PlaylistAdminClass(ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_display = [
        "display_name",
        "display_contents",
        "created_at",
        "updated_at",
        "display_status",
    ]
    list_filter = ["is_active"]
    search_fields = ["name"]
    filter_horizontal = ["screens"]

    fieldsets = (
        (None, {"fields": ("name", "is_active")}),
        ("Screens to display on", {"fields": ("screens",)}),
        ("Important dates", {"fields": (("created_at", "updated_at"),)}),
    )

    @display(description="Playlist name")
    def display_name(self, obj):
        return obj.name.capitalize()

    @display(description="Status", label={"Active": "success", "Inactive": "danger"})
    def display_status(self, obj):
        return "Active" if obj.is_active else "Inactive"

    @display(description="Contents")
    def display_contents(self, obj):
        contents = obj.contents.filter(is_active=True)
        if contents.count() == 0:
            return "No contents assigned"
        count = contents.count()
        return f"{count} " + ("contents" if count > 1 else "content")


@admin.register(Content)
class ContentAdminClass(ModelAdmin):
    form = ContentAdminForm
    change_form_template = "signage/admin/content_change_form.html"

    # actions_row = ["content_preview"]
    # actions_submit_line = ["content_preview"]
    readonly_fields = ["created_at", "updated_at"]
    list_display = [
        "display_name",
        "type",
        "display_duration",
        "display_playlists",
        "starts_at",
        "ends_at",
        "display_status",
    ]
    list_filter = ["type"]
    search_fields = ["name"]
    filter_horizontal = ["playlists"]

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
        ("Playlists to display on", {"fields": ("playlists",)}),
        ("Important dates", {"fields": (("created_at", "updated_at"),)}),
    )

    @display(description="Content name")
    def display_name(self, obj):
        name = obj.name.capitalize()
        return name[:30] + "..." if len(name) > 30 else name

    @display(description="Duration")
    def display_duration(self, obj):
        return f"{obj.duration} seconds"

    @display(description="Playlists")
    def display_playlists(self, obj):
        playlists = obj.playlists.filter(is_active=True)
        if playlists.count() == 0:
            return "-"
        return ", ".join(
            [
                (
                    playlist.name.capitalize()
                    if len(playlist.name) < 20
                    else playlist.name.capitalize()[0:20] + "..."
                )
                for playlist in playlists
            ]
        )

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

    # @action(description="Preview", attrs={"target": "_blank"})
    # def content_preview(self, request: HttpRequest, obj: Content):
    #     return redirect(f"https://example.com/{obj.id}")

    # actions_detail = ["content_preview"]

    # @action(description="Preview", attrs={"target": "_blank"})
    # def content_preview(self, request: HttpRequest, object_id: int):
    #     return redirect(f"https://example.com/{object_id}")
