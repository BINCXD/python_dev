# Generated by Django 2.2.5 on 2019-12-12 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lunbotu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='轮播名称')),
                ('img', models.CharField(max_length=20, verbose_name='轮播图片')),
                ('url', models.CharField(max_length=20, verbose_name='轮播url')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
                'db_table': 'vue_lunbo',
            },
        ),
    ]
