# Generated by Django 2.2.5 on 2019-12-16 09:36

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20191215_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture_classification',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='图片分类ID')),
                ('title', models.CharField(max_length=20, verbose_name='图片类别')),
            ],
            options={
                'verbose_name': '图片分类',
                'verbose_name_plural': '图片分类',
                'db_table': 'vue_classification',
            },
        ),
        migrations.CreateModel(
            name='PictureList',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='图片ID')),
                ('channel_id', models.IntegerField(verbose_name='频道ID')),
                ('call_index', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50, verbose_name='图片标题')),
                ('link_url', models.CharField(max_length=50, verbose_name='跳转链接')),
                ('img_url', models.CharField(max_length=50, verbose_name='展示图片')),
                ('seo_title', models.CharField(max_length=50, verbose_name='推广标题')),
                ('seo_keywords', models.CharField(max_length=50, verbose_name='推广关键字')),
                ('seo_description', models.CharField(max_length=100, verbose_name='推广描述')),
                ('tags', models.CharField(max_length=10, verbose_name='所属关键词')),
                ('zhaiyao', models.CharField(max_length=100, verbose_name='摘要')),
                ('content', models.TextField(verbose_name='详情')),
                ('sort_id', models.CharField(max_length=10, verbose_name='排序ID')),
                ('click', models.CharField(max_length=10, verbose_name='点击次数')),
                ('status', models.BooleanField(default=0, verbose_name='状态')),
                ('is_msg', models.BooleanField(default=0, verbose_name='图片识别标识')),
                ('is_top', models.BooleanField(default=0, verbose_name='是否置顶')),
                ('is_red', models.BooleanField(default=0, verbose_name='是否热门')),
                ('is_slide', models.BooleanField(default=0, verbose_name='是否滑动')),
                ('is_sys', models.BooleanField(default=0, verbose_name='是否公司')),
                ('user_name', models.CharField(max_length=20, verbose_name='作者')),
                ('add_time', models.DateTimeField(default=datetime.datetime(2019, 12, 16, 9, 36, 55, 414460, tzinfo=utc), verbose_name='上传时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime(2019, 12, 16, 9, 36, 55, 414460, tzinfo=utc), verbose_name='修改时间')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Picture_classification', verbose_name='所属类别')),
            ],
            options={
                'verbose_name': '图片库',
                'verbose_name_plural': '图片库',
                'db_table': 'vue_images',
            },
        ),
        migrations.CreateModel(
            name='ThumImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumimages', models.CharField(max_length=500, verbose_name='图片缩略图')),
                ('t_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PictureList', verbose_name='所属图片')),
            ],
            options={
                'verbose_name': '缩略图',
                'verbose_name_plural': '缩略图',
                'db_table': 'vue_thumimages',
            },
        ),
        migrations.CreateModel(
            name='ImageComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, verbose_name='评论人')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='评论时间')),
                ('content', models.CharField(max_length=500, verbose_name='评论内容')),
                ('i_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PictureList', verbose_name='所属图片')),
            ],
            options={
                'verbose_name': '图片评论',
                'verbose_name_plural': '图片评论',
                'db_table': 'vue_image_comments',
            },
        ),
    ]
