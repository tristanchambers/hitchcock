# Generated by Django 2.2.14 on 2020-08-24 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0003_upload_queued_for_processing'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='panopto_session_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]