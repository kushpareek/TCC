# Generated by Django 5.0.7 on 2024-10-22 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champion', '0021_videoaccesstoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='reel',
            name='reel_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reels', to='champion.reelcategory'),
        ),
    ]
