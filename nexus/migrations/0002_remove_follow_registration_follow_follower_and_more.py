# Generated by Django 5.0.7 on 2024-11-13 06:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='registration',
        ),
        migrations.AddField(
            model_name='follow',
            name='follower',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='following', to='nexus.userprofile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='follow',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='follow',
            name='follows_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='nexus.userprofile'),
        ),
    ]
