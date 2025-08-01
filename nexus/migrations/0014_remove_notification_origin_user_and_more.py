# Generated by Django 5.0.7 on 2025-02-10 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus', '0013_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='origin_user',
        ),
        migrations.AddField(
            model_name='notification',
            name='target_tweet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notifications', to='nexus.tweet'),
        ),
    ]
