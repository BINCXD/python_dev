from django.core import serializers
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
import requests
import json

from api.models import lunbotu, NewsList, NewsComments, PictureList, Picture_classification, ThumImages, GoodsSku, \
    GoodsComment, ImageComments


class GetlunboView(View):
    def get(self, request):
        lunbolist = lunbotu.objects.all()
        message = []
        for lunbo in lunbolist:
            message.append({'id': lunbo.id, 'url': lunbo.url, 'img': 'http://127.0.0.1:8000' + lunbo.img})
        return JsonResponse({'status': 0, 'message': message})


class NewsListView(View):
    def get(self, request):
        newslist = NewsList.objects.all()
        message = []
        for news in newslist:
            context = {
                'id': news.id,
                'title': news.title,
                'add_time': news.add_time,
                'zhaiyao': news.zhaiyao,
                'click': news.click,
                'img_url': 'http://127.0.0.1:8000' + news.img_url,
            }
            message.append(context)
        return JsonResponse({'status': 0, 'message': message})


class NewsInfoView(View):
    def get(self, request, id):
        newsinfo = NewsList.objects.get(id=id)
        message = []
        context = {
            'id': newsinfo.id,
            'title': newsinfo.title,
            'add_time': newsinfo.add_time,
            'click': newsinfo.click,
            'content': newsinfo.content
        }
        message.append(context)
        return JsonResponse({'status': 0, 'message': message})


class CommentsView(View):
    def get(self, request, id):
        pageindex = request.GET.get('pageindex')
        news = [13, 14, 15, 16, 19, 20, 21, 22, 23, 24]
        images = [x for x in range(37,54)]
        goods = [x for x in range(87,102)]
        comments = {}
        if id in news:
            res = NewsComments.objects.filter(n_id=id).order_by('-add_time')
            comments = res
        elif id in images:
            res = ImageComments.objects.filter(i_id=id).order_by('-add_time')
            comments = res
        elif id in goods:
            res = GoodsComment.objects.filter(g_id=id).order_by('-add_time')
            comments = res
        # 对数据进行分页
        paginator = Paginator(comments, 10)
        # 获取第page页的Page实例对象
        skus_page = paginator.page(pageindex)
        message = []
        for sku in skus_page:
            context = {
                'username': sku.user_name,
                'add_time': sku.add_time,
                'content': sku.content
            }
            message.append(context)
        return JsonResponse({'status': 0, 'message': message})


class AddCommentView(View):
    def post(self, requests, id):
        news = [13, 14, 15, 16, 19, 20, 21, 22, 23, 24]
        images = [x for x in range(37, 54)]
        goods = [x for x in range(87, 102)]
        msg = requests.POST.get('content')
        if id in news:
            news = NewsList.objects.get(id=id)
            user_name = '匿名用户'
            comment = NewsComments()
            comment.content = msg
            comment.user_name = user_name
            comment.n_id = news
            comment.save()
        elif id in images:
            img = PictureList.objects.get(id=id)
            user_name = '匿名用户'
            comment = ImageComments()
            comment.content = msg
            comment.user_name = user_name
            comment.i_id = img
            comment.save()
        elif id in goods:
            god = GoodsSku.objects.get(id=id)
            user_name = '匿名用户'
            comment = GoodsComment()
            comment.content = msg
            comment.user_name = user_name
            comment.g_id = god
            comment.save()
        return JsonResponse({'status': 0})


class PicClsView(View):
    def get(self, request):
        cls_list = Picture_classification.objects.all()
        message = []
        for cls in cls_list:
            context = {
                'id': cls.id,
                'title': cls.title,
            }
            message.append(context)
        return JsonResponse({'status': 0, 'message': message})


class ImagesListView(View):
    def get(self, request, id):
        if id == 0:
            image_list = PictureList.objects.all()
            message = []
            for image in image_list:
                context = {
                    'id': image.id,
                    'title': image.title,
                    'zhaiyao': image.zhaiyao,
                    'img_url': 'http://127.0.0.1:8000' + image.img_url
                }
                message.append(context)
            return JsonResponse({'status': 0, 'message': message})
        else:
            cls = Picture_classification.objects.get(id=id)
            image_list = PictureList.objects.filter(category_id=cls)
            message = []
            for image in image_list:
                context = {
                    'id': image.id,
                    'title': image.title,
                    'zhaiyao': image.zhaiyao,
                    'img_url': 'http://127.0.0.1:8000' + image.img_url
                }
                message.append(context)
            return JsonResponse({'status': 0, 'message': message})


class ImageInfoView(View):
    def get(self, request, id):
        image = PictureList.objects.get(id=id)
        context = {
            'id': image.id,
            'title': image.title,
            'click': image.click,
            'add_time': image.add_time,
            'content': image.content
        }
        message = [context]
        return JsonResponse({'status': 0, 'message': message})


class ThumImagesView(View):
    def get(self, request, id):
        imgs = [x for x in range(37,54)]
        gods = [x for x in range(87,102)]
        if id in imgs:
            pic = PictureList.objects.get(id=id)
            thum_imgs = ThumImages.objects.get(t_id=pic)
            thum_list = thum_imgs.thumimages.split('|')
            message = []
            for thum in thum_list:
                context = {
                    'src': 'http://127.0.0.1:8000' + thum
                }
                message.append(context)
            return JsonResponse({'status': 0, 'message': message})
        elif id in gods:
            pic = GoodsSku.objects.get(id=id)
            thum_list = pic.thum_img.split('|')
            message = []
            for thum in thum_list:
                context = {
                    'src': 'http://127.0.0.1:8000' + thum
                }
                message.append(context)
            return JsonResponse({'status': 0, 'message': message})



class GoodsListView(View):
    def get(self, request):
        pageindex = request.GET.get('pageindex')
        goodslist = GoodsSku.objects.all().order_by()
        # 对数据进行分页
        paginator = Paginator(goodslist, 10)
        # 获取第page页的Page实例对象
        skus_page = paginator.page(pageindex)
        message = []
        for sku in skus_page:
            context = {
                'id': sku.id,
                'title': sku.title,
                'add_time': sku.add_time,
                'zhaiyao': sku.zhaiyao,
                'click': sku.click,
                'img_url': 'http://127.0.0.1:8000' + sku.img_url,
                'sell_price': sku.sell_price,
                'market_price': sku.market_price,
                'stock_quantity': sku.stock_quantity
            }
            message.append(context)
        return JsonResponse({'status': 0, 'message': message})








