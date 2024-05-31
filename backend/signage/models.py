from django.db import models
from django.core.validators import MinValueValidator


class Screen(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # playlists
    playlists = models.ManyToManyField("Playlist", related_name="screens", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name.strip().replace(" ", "-").lower()
        super(Screen, self).save(*args, **kwargs)

    class Meta:
        db_table = "screen"
        ordering = ["-id"]
        verbose_name = "Screen"
        verbose_name_plural = "Screens"


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # contents
    contents = models.ManyToManyField("Content", related_name="playlists", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "playlist"
        ordering = ["-id"]
        verbose_name = "Playlist"
        verbose_name_plural = "Playlists"


class Content(models.Model):

    CONTENT_TYPES = (
        ("image", "Image"),
        ("video", "Video"),
        ("text", "Text"),
        ("embed", "Embed"),
    )

    name = models.CharField(max_length=255, verbose_name="Content Name")
    type = models.CharField(
        max_length=255, choices=CONTENT_TYPES, verbose_name="Content Type"
    )
    # Content
    url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Embed URL",
        help_text='If the type is "embed", please provide the URL. Otherwise, leave this field blank.',
    )
    file = models.FileField(
        upload_to="content/files/",
        blank=True,
        null=True,
        verbose_name="Image/Video File",
        help_text='If the type is "image" or "video", please upload the file.',
    )
    text = models.TextField(
        blank=True,
        null=True,
        verbose_name="Text Content",
        help_text='If the type is "text", please provide the text content.',
    )
    duration = models.PositiveIntegerField(
        default=30,
        validators=[MinValueValidator(3)],
        verbose_name="Duration (in seconds)",
        help_text="Specify the duration of the content in seconds.",
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Is Active",
        help_text="If the content is not active, it will not be displayed on the screens.",
    )

    starts_at = models.DateTimeField(
        verbose_name="Starts At",
        help_text="Specify the start date and time for the content. If not specified, the content will be displayed immediately.",
    )
    ends_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Ends At",
        help_text="Specify the end date and time for the content. If not specified, the content will be displayed indefinitely.",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "content"
        ordering = ["-id"]
        verbose_name = "Content"
        verbose_name_plural = "Contents"
