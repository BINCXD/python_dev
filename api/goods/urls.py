from django.urls import path

from api.goods import views

app_name = 'goods'

urlpatterns = [
    path('getinfo/<int:id>/', views.GoodsInfoView.as_view(), name='getinfo'),
    path('getdesc/<int:id>/', views.GoodsDescView.as_view(), name='getdesc'),
    path('getshopcarlist/<str:ids>/', views.ShopCarListView.as_view(), name='getshopcarlist'),
]