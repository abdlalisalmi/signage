# Generated by Django 5.0.6 on 2024-05-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signage', '0005_alter_content_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='contents',
        ),
        migrations.RemoveField(
            model_name='screen',
            name='playlists',
        ),
        migrations.AddField(
            model_name='content',
            name='playlists',
            field=models.ManyToManyField(blank=True, related_name='contents', to='signage.playlist'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='screens',
            field=models.ManyToManyField(blank=True, related_name='playlists', to='signage.screen'),
        ),
    ]
