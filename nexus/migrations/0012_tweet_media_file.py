# Generated by Django 5.0.7 on 2024-11-28 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus', '0011_remove_activitylog_actor_alter_activitylog_action_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='media_file',
            field=models.FileField(blank=True, null=True, upload_to='media_files/'),
        ),
    ]
