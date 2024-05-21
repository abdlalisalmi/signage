from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


def has_permission(request, app_label, model_name):
    return request.user.has_perm(f"{app_label}.view_{model_name}")


UNFOLD = {
    "SITE_TITLE": "Supervisor",
    "SITE_HEADER": "Signage",
    "SITE_URL": "/",
    # "SITE_ICON": lambda request: "https://res.cloudinary.com/djr3obtg6/image/upload/v1710331091/logo_avd7to.png",
    "SITE_SYMBOL": "cast",  # symbol from icon set
    # "LOGIN": {
    #     "image": lambda r: "https://i.imgur.com/aIkz2KI.png",
    # },
    "COLORS": {
        "primary": {
            "50": "236 254 255",
            "100": "207 250 254",
            "200": "165 243 252",
            "300": "103 232 249",
            "400": "34 211 238",
            "500": "6 182 212",
            "600": "8 145 178",
            "700": "14 116 144",
            "800": "21 94 117",
            "900": "22 78 99",
            "950": "8 51 68",
        }
    },
    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "show_all_applications": True,  # Dropdown with all applications and models
        "navigation": [
            {
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:index"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                ],
            },
            {
                "title": _("Users & Permissions"),
                "separator": True,  # Top border
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "person",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                        "permission": lambda request: has_permission(
                            request, "authentication", "user"
                        ),
                    },
                    {
                        "title": _("Groups"),
                        "icon": "group",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                        "permission": lambda request: has_permission(
                            request, "authentication", "group"
                        ),
                    },
                ],
            },
            {
                "title": _("Signage Management"),
                "separator": True,  # Top border
                "items": [
                    {
                        "title": _("Screens"),
                        "icon": "jamboard_kiosk",
                        "link": reverse_lazy("admin:signage_screen_changelist"),
                        "permission": lambda request: has_permission(
                            request, "signage", "screen"
                        ),
                    },
                    {
                        "title": _("Playlists"),
                        "icon": "list",
                        "link": reverse_lazy("admin:signage_playlist_changelist"),
                        "permission": lambda request: has_permission(
                            request, "signage", "playlist"
                        ),
                    },
                    {
                        "title": _("Contents"),
                        "icon": "newsmode",
                        "link": reverse_lazy("admin:signage_content_changelist"),
                        "permission": lambda request: has_permission(
                            request, "signage", "content"
                        ),
                    },
                ],
            },
        ],
    },
    # "TABS": [
    #     {
    #         "models": [
    #             "supervisor.privileges",
    #         ],
    #         "items": [
    #             {
    #                 "title": _("Students Privileges"),
    #                 "link": reverse_lazy("admin:supervisor_privileges_changelist"),
    #                 # "permission": "sample_app.permission_callback",
    #             },
    #             {
    #                 "title": _("Students Internships"),
    #                 "link": reverse_lazy("admin:supervisor_internship_changelist"),
    #                 # "permission": "sample_app.permission_callback",
    #             },
    #         ],
    #     },
    # ],
}
