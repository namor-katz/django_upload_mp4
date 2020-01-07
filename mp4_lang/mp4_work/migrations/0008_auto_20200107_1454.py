# Generated by Django 3.0.2 on 2020-01-07 14:54

from django.db import migrations, models
import mp4_work.models


class Migration(migrations.Migration):

    dependencies = [
        ('mp4_work', '0007_auto_20200107_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='mp4',
            name='file_convert',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mp4',
            name='file_path',
            field=models.FileField(max_length=500, upload_to='archives/%Y/%m/%d/', validators=[mp4_work.models.validate_video], verbose_name='загрузить файл!'),
        ),
    ]