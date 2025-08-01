

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champion', '0026_videocategory_alter_video_price_video_videocategory'),
        ('nexus', '0010_remove_activitylog_event_type_and_more'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='activitylog',
        #     name='actor',
        # ),
        migrations.AlterField(
            model_name='activitylog',
            name='action',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='activitylog',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='activitylog',
            name='registration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='champion.registration'),
        ),
        migrations.AlterField(
            model_name='activitylog',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

