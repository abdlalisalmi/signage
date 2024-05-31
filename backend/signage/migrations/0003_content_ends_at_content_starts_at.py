# Generated by Django 5.0.6 on 2024-05-30 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signage', '0002_alter_content_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='ends_at',
            field=models.DateTimeField(blank=True, help_text='Specify the end date and time for the content. If not specified, the content will be displayed indefinitely.', null=True, verbose_name='Ends At'),
        ),
        migrations.AddField(
            model_name='content',
            name='starts_at',
            field=models.DateTimeField(blank=True, help_text='Specify the start date and time for the content. If not specified, the content will be displayed immediately.', null=True, verbose_name='Starts At'),
        ),
    ]
