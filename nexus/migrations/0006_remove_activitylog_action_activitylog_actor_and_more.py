

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus', '0005_remove_activitylog_actor_and_more'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='activitylog',
        #     name='action',
        # ),
        # migrations.AddField(
        #     model_name='activitylog',
        #     name='actor',
        #     field=models.ForeignKey(default='Follow', on_delete=django.db.models.deletion.CASCADE, related_name='activity_actor', to='nexus.userprofile'),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='activitylog',
        #     name='event_type',
        #     field=models.CharField(choices=[('FOLLOW', 'Follow'), ('LIKE', 'Like'), ('RETWEET', 'Retweet'), ('REPLY', 'Reply')], default=0, max_length=10),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='activitylog',
        #     name='related_tweet',
        #     field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nexus.tweet'),
        # ),
        # migrations.AlterField(
        #     model_name='activitylog',
        #     name='registration',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus.userprofile'),
        # ),
    ]
