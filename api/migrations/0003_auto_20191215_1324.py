# Generated by Django 2.2.5 on 2019-12-15 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_newslist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslist',
            name='img_url',
            field=models.CharField(max_length=50, verbose_name='标题图片'),
        ),
    ]
