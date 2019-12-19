from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from api.models import GoodsSku


class GoodsInfoView(View):
    def get(self, request, id):
        sku = GoodsSku.objects.get(id=id)
        context = {
            'id': sku.id,
            'title': sku.title,
            'add_time': sku.add_time,
            'goods_no': sku.goods_no,
            'stock_quantity': sku.stock_quantity,
            'market_price': sku.market_price,
            'sell_price': sku.sell_price
        }
        message = [context]
        return JsonResponse({'status': 0, 'message': message})


class GoodsDescView(View):
    def get(self, request, id):
        sku = GoodsSku.objects.get(id=id)
        context = {
            'title': sku.title,
            'content': sku.content,
        }
        message = [context]
        return JsonResponse({'status': 0, 'message': message})


class ShopCarListView(View):
    def get(self, request, ids):
        id_s = ids.split(',')
        message = []
        for id in id_s:
            goods_sku = GoodsSku.objects.get(id=id)
            context = {
                'cou': 1,
                'id': goods_sku.id,
                'title': goods_sku.title,
                'sell_price': goods_sku.sell_price,
                'thumb_path': 'http://127.0.0.1:8000' + goods_sku.img_url
            }
            message.append(context)
        return JsonResponse({'status': 0, 'message': message})

