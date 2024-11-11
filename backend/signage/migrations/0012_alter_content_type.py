# Generated by Django 5.0.6 on 2024-11-07 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signage', '0011_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='type',
            field=models.CharField(choices=[('image', 'Image'), ('video', 'Video'), ('text', 'Text'), ('embed', 'Embed')], max_length=255, verbose_name='Content Type'),
        ),
    ]