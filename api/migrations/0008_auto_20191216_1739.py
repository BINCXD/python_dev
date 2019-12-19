# Generated by Django 2.2.5 on 2019-12-16 09:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_imagecomments_picture_classification_picturelist_thumimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturelist',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='picturelist',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间'),
        ),
    ]
