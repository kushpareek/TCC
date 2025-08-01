# Generated by Django 5.0.7 on 2024-10-04 07:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("champion", "0014_reel_compressed_video_reel_compression_error_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsArticle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField(max_length=280)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="news_images/"),
                ),
                (
                    "video",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="news_videos/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["mp4", "mov", "avi"]
                            )
                        ],
                    ),
                ),
                ("publish_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-publish_date"],
            },
        ),
    ]
