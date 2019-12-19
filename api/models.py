from django.db import models

# Create your models here.
from django.utils import timezone


class lunbotu(models.Model):
    """商品类型模型类"""
    name = models.CharField(max_length=20, verbose_name='轮播名称')
    img = models.CharField(max_length=20, verbose_name='轮播图片')
    url = models.CharField(max_length=20, verbose_name='轮播url')

    class Meta:
        db_table = 'vue_lunbo'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class NewsList(models.Model):
    id = models.IntegerField(verbose_name='新闻id', primary_key=True)
    title = models.CharField(max_length=30, verbose_name='新闻标题')
    add_time = models.CharField(max_length=30, verbose_name='添加时间')
    zhaiyao = models.CharField(max_length=40, verbose_name='新闻摘要')
    click = models.IntegerField(verbose_name='点击次数')
    img_url = models.CharField(max_length=50, verbose_name='标题图片')
    content = models.TextField(verbose_name='新闻详情')

    class Meta:
        db_table = 'vue_news'
        verbose_name = '新闻列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class NewsComments(models.Model):
    user_name = models.CharField(max_length=20, verbose_name='评论人')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='评论时间')
    content = models.CharField(max_length=500, verbose_name='评论内容')
    n_id = models.ForeignKey(NewsList, on_delete=models.CASCADE, verbose_name='所属新闻')

    class Meta:
        db_table = 'vue_news_comments'
        verbose_name = '新闻评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class Picture_classification(models.Model):
    id = models.IntegerField(verbose_name='图片分类ID', primary_key=True)
    title = models.CharField(max_length=20, verbose_name='图片类别')

    class Meta:
        db_table = 'vue_classification'
        verbose_name = '图片分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class PictureList(models.Model):
    id = models.IntegerField(verbose_name='图片ID', primary_key=True)
    channel_id = models.IntegerField(verbose_name='频道ID')
    category_id = models.ForeignKey(Picture_classification, on_delete=models.CASCADE, verbose_name='所属类别')
    call_index = models.CharField(max_length=50)
    title = models.CharField(max_length=50, verbose_name='图片标题')
    link_url = models.CharField(max_length=50, verbose_name='跳转链接')
    img_url = models.CharField(max_length=150, verbose_name='展示图片')
    seo_title = models.CharField(max_length=50, verbose_name='推广标题')
    seo_keywords = models.CharField(max_length=50, verbose_name='推广关键字')
    seo_description = models.CharField(max_length=500, verbose_name='推广描述')
    tags = models.CharField(max_length=10, verbose_name='所属关键词')
    zhaiyao = models.CharField(max_length=500, verbose_name='摘要')
    content = models.TextField(verbose_name='详情')
    sort_id = models.CharField(max_length=10, verbose_name='排序ID')
    click = models.CharField(max_length=10, verbose_name='点击次数')
    status = models.BooleanField(default=0, verbose_name='状态')
    is_msg = models.BooleanField(default=0, verbose_name='图片识别标识')
    is_top = models.BooleanField(default=0, verbose_name='是否置顶')
    is_red = models.BooleanField(default=0, verbose_name='是否热门')
    is_slide = models.BooleanField(default=0, verbose_name='是否滑动')
    is_sys = models.BooleanField(default=0, verbose_name='是否公司')
    user_name = models.CharField(max_length=20, verbose_name='作者')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='上传时间')
    update_time = models.DateTimeField(default=timezone.now, verbose_name='修改时间')

    class Meta:
        db_table = 'vue_images'
        verbose_name = '图片库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ImageComments(models.Model):
    user_name = models.CharField(max_length=20, verbose_name='评论人')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='评论时间')
    content = models.CharField(max_length=500, verbose_name='评论内容')
    i_id = models.ForeignKey(PictureList, on_delete=models.CASCADE, verbose_name='所属图片')

    class Meta:
        db_table = 'vue_image_comments'
        verbose_name = '图片评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class ThumImages(models.Model):
    thumimages = models.CharField(max_length=500, verbose_name='图片缩略图')
    t_id = models.ForeignKey(PictureList, on_delete=models.CASCADE, verbose_name='所属图片')

    class Meta:
        db_table = 'vue_thumimages'
        verbose_name = '缩略图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.t_id


class GoodsSku(models.Model):
    id = models.IntegerField(verbose_name='商品ID', primary_key=True)
    title = models.CharField(max_length=100, verbose_name='商品标题')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')
    zhaiyao = models.CharField(max_length=100, verbose_name='商品摘要')
    click = models.CharField(max_length=10, verbose_name='点击次数')
    img_url = models.CharField(max_length=100, verbose_name='显示图片')
    sell_price = models.CharField(max_length=10, verbose_name='售卖价格')
    market_price = models.CharField(max_length=10, verbose_name='之前价格')
    stock_quantity = models.CharField(max_length=15, verbose_name='成交量')
    goods_no = models.CharField(max_length=20, verbose_name='商品编号')
    thum_img = models.CharField(max_length=200, verbose_name='缩略图')
    content = models.TextField(verbose_name='商品详情页面')

    class Meta:
        db_table = 'vue_goods'
        verbose_name = '商品列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class GoodsComment(models.Model):
    user_name = models.CharField(max_length=20, verbose_name='评论人')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='评论时间')
    content = models.CharField(max_length=500, verbose_name='评论内容')
    g_id = models.ForeignKey(GoodsSku, on_delete=models.CASCADE, verbose_name='所属商品')

    class Meta:
        db_table = 'vue_good_comments'
        verbose_name = '商品评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content





