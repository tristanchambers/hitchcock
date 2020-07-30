# Generated by Django 2.2.14 on 2020-07-30 21:30

from django.db import migrations, models
import django.db.models.deletion
import uploads.models
import uploads.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('identifier', models.CharField(help_text='barcode, ISBN, etc.', max_length=512)),
                ('form', models.CharField(choices=[('digitized', 'Digitized'), ('born_digital', 'Born Digital')], default='digitized', max_length=16)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('size', models.IntegerField(blank=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_uploads.upload_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('upload_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uploads.Upload')),
                ('upload', models.FileField(help_text='mp3 format only', max_length=1024, upload_to='av/audio/', validators=[uploads.validators.validate_audio])),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('uploads.upload',),
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('upload_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uploads.Upload')),
                ('upload', models.FileField(help_text='pdf format only', max_length=1024, upload_to=uploads.models.text_upload_path, validators=[uploads.validators.validate_text])),
                ('type', models.CharField(choices=[('article', 'Article'), ('book_excerpt', 'Book (excerpt)'), ('book_whole', 'Book (whole)'), ('other', 'Other')], default='article', max_length=16)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('uploads.upload',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('upload_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uploads.Upload')),
                ('upload', models.FileField(help_text='mp4 format only', max_length=1024, upload_to='av/video/', validators=[uploads.validators.validate_video])),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('uploads.upload',),
        ),
    ]
