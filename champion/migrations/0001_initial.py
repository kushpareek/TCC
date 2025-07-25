# Generated by Django 5.0.7 on 2024-08-30 08:45

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Coupon",
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
                ("code", models.CharField(max_length=50, unique=True)),
                ("discount", models.DecimalField(decimal_places=2, max_digits=5)),
                ("is_active", models.BooleanField(default=True)),
                ("expiration_date", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Video",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("video_file", models.FileField(upload_to="videos/")),
                ("preview_file", models.FileField(upload_to="videos/previews/")),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True, null=True, upload_to="videos/thumbnails/"
                    ),
                ),
                ("duration", models.DurationField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name="Blog",
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
                ("category", models.CharField(max_length=100)),
                ("content", ckeditor.fields.RichTextField()),
                ("slug", models.SlugField(blank=True, unique=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="blog_images/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Course",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("beginner", "Beginner"),
                            ("intermediate", "Intermediate"),
                            ("advanced", "Advanced"),
                        ],
                        default="beginner",
                        max_length=20,
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("image", models.ImageField(upload_to="course_images/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="champion.category",
                    ),
                ),
                (
                    "instructor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Enrollment",
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
                ("enrolled_at", models.DateTimeField(auto_now_add=True)),
                (
                    "progress",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="champion.course",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Registration",
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
                ("phone", models.CharField(max_length=15)),
                ("day", models.PositiveIntegerField()),
                ("month", models.PositiveIntegerField()),
                ("year", models.PositiveIntegerField()),
                ("joined_as", models.BooleanField(default=True)),
                ("champion_reason", models.TextField()),
                ("achievements", models.TextField()),
                ("unique_trait", models.TextField()),
                (
                    "approved",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "Pending"), (1, "Approved"), (2, "Rejected")],
                        default=0,
                    ),
                ),
                (
                    "verification_token",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("is_email_verified", models.BooleanField(default=False)),
                ("submission_date", models.DateTimeField(auto_now_add=True)),
                ("discord_id", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "telegram_username",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="profile_images/"
                    ),
                ),
                ("membership_paid", models.BooleanField(default=False)),
                ("paid_on", models.DateTimeField(blank=True, null=True)),
                (
                    "personality_traits",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("skills", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "designation",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("motivations", models.TextField(blank=True, null=True)),
                ("goals", models.TextField(blank=True, null=True)),
                ("bio", models.TextField(blank=True, null=True)),
                ("deactivated_at", models.DateTimeField(blank=True, null=True)),
                (
                    "address_line_1",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "address_line_2",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("state", models.CharField(blank=True, max_length=100, null=True)),
                ("postal_code", models.CharField(blank=True, max_length=20, null=True)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Section",
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
                ("title", models.CharField(max_length=255)),
                ("order", models.IntegerField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sections",
                        to="champion.course",
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="Lesson",
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
                ("title", models.CharField(max_length=255)),
                ("video", models.FileField(upload_to="lesson_videos/")),
                ("order", models.IntegerField()),
                ("description", models.TextField(blank=True, null=True)),
                ("transcript", models.TextField(blank=True, null=True)),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lessons",
                        to="champion.section",
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="SupportRequest",
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
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("billing", "Billing"),
                            ("technical", "Technical Support"),
                            ("general", "General Inquiry"),
                        ],
                        max_length=50,
                    ),
                ),
                ("subject", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(default="Open", max_length=50)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="support_requests",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserVideoStatus",
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
                ("last_watched_time", models.DurationField(default=0)),
                ("has_paid", models.BooleanField(default=False)),
                ("has_completed", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "video",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="champion.video"
                    ),
                ),
            ],
        ),
    ]
