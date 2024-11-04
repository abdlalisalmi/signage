from django.db import models
from django.db.models.functions import Lower
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Screen(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Screen Name",
        help_text="Unique name for the screen to identify it.",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="Description of the screen to provide more information.",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Is Active",
        help_text="If the screen is not active, it will not be displayed.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "screen"
        ordering = ["-id"]
        verbose_name = "Screen"
        verbose_name_plural = "Screens"
        constraints = [
            models.UniqueConstraint(
                Lower("name"),
                name="unique screen name",
            )
        ]


class Playlist(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Playlist Name",
        help_text="Unique name for the playlist to identify it.",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Is Active",
        help_text="If the playlist is not active, it will not be displayed on the screens.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Screens
    screens = models.ManyToManyField("Screen", related_name="playlists", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "playlist"
        ordering = ["-id"]
        verbose_name = "Playlist"
        verbose_name_plural = "Playlists"
        constraints = [
            models.UniqueConstraint(
                Lower("name"),
                name="unique playlist name",
            )
        ]


class Content(models.Model):

    CONTENT_TYPES = (
        ("image", "Image"),
        # ("video", "Video"),
        ("text", "Text"),
        ("embed", "Embed"),
    )

    # Playlists
    playlists = models.ManyToManyField("Playlist", related_name="contents", blank=True)

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

    # Check for the required fields based on the content type
    def clean(self):
        super().clean()
        if self.type == "image" or self.type == "video":
            if not self.file:
                raise ValidationError(
                    {
                        "file": _(
                            "Image/Video file is required for image/video content type."
                        )
                    }
                )
        elif self.type == "text":
            if not self.text:
                raise ValidationError(
                    {"text": _("Text content is required for text content type.")}
                )
        elif self.type == "embed":
            if not self.url:
                raise ValidationError(
                    {"url": _("Embed URL is required for embed content type.")}
                )

    # delete the file when the object is deleted
    def delete(self, *args, **kwargs):
        try:
            if self.type in ["image", "video"] and self.file:
                self.file.delete()
        except Exception:
            pass
        super(Content, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "content"
        ordering = ["-id"]
        verbose_name = "Content"
        verbose_name_plural = "Contents"
