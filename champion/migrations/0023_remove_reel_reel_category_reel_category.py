# Generated by Django 5.0.7 on 2024-10-22 05:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champion', '0022_reelcategory_reel_reel_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reel',
            name='reel_category',
        ),
        migrations.AddField(
            model_name='reel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reels', to='champion.reelcategory'),
        ),
    ]
