from django.utils.safestring import mark_safe
from django.db.models import Count
from signage.models import Content, Screen, Playlist


def get_signage_kpi():
    screens = Screen.objects.all()
    playlists = Playlist.objects.all()
    contents = Content.objects.all()
    return [
        {
            "title": "Number of Screens",
            "metric": screens.count(),
            "footer": mark_safe(
                f'<strong class="text-green-700 font-semibold dark:text-green-400">{screens.filter(is_active=True).count()}</strong>&nbsp;of them are active now'
            ),
        },
        {
            "title": "Number of Playlists",
            "metric": playlists.count(),
            "footer": mark_safe(
                f'<strong class="text-green-700 font-semibold dark:text-green-400">{playlists.filter(is_active=True).count()}</strong>&nbsp;of them are active now'
            ),
        },
        {
            "title": "Number of Contents",
            "metric": contents.count(),
            "footer": mark_safe(
                f'<strong class="text-green-700 font-semibold dark:text-green-400">{contents.filter(is_active=True).count()}</strong>&nbsp;of them are active now'
            ),
        },
    ]


def get_contents_progress():

    def get_content_icon(content_type, icon):
        return f'<div class="flex items-center"><span class="material-symbols-outlined mr-2">{icon.lower()}</span><p class="font-normal">{content_type}</p></div>'

    # Get counts for each content type
    content_counts = Content.objects.values("type").annotate(count=Count("id"))
    contents_progress = {item["type"]: item["count"] for item in content_counts}
    return [
        {
            "title": mark_safe(get_content_icon("Images", "image")),
            "description": contents_progress.get("image", 0),
            "value": contents_progress.get("image", 0),
        },
        {
            "title": mark_safe(get_content_icon("Videos", "movie")),
            "value": contents_progress.get("video", 0),
        },
        {
            "title": mark_safe(get_content_icon("Texts & Quotes", "text_snippet")),
            "value": contents_progress.get("text", 0),
        },
        {
            "title": mark_safe(get_content_icon("Embeds", "link")),
            "value": contents_progress.get("embed", 0),
        },
    ]
