

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champion', '0026_videocategory_alter_video_price_video_videocategory'),
        ('nexus', '0006_remove_activitylog_action_activitylog_actor_and_more'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='activitylog',
        #     name='actor',
        # ),
        # migrations.RemoveField(
        #     model_name='activitylog',
        #     name='event_type',
        # ),
        # migrations.RemoveField(
        #     model_name='activitylog',
        #     name='related_tweet',
        # ),
        # migrations.AddField(
        #     model_name='activitylog',
        #     name='action',
        #     field=models.CharField(default=0, max_length=100),
        #     preserve_default=False,
        # ),
        # migrations.AlterField(
        #     model_name='activitylog',
        #     name='registration',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='champion.registration'),
        # ),
    ]

