from django.urls import path, include

from api import views

app_name = 'api'

urlpatterns = [
    path('getlunbo/', views.GetlunboView.as_view(), name='getlunbo'),
    path('getnewslist/', views.NewsListView.as_view(), name='getnewslist'),
    path('getnew/<int:id>/', views.NewsInfoView.as_view(), name='getnew'),
    path('getcomments/<int:id>/', views.CommentsView.as_view(), name='getcomments'),
    path('postcomment/<int:id>/', views.AddCommentView.as_view(), name='postcomment'),
    path('getimgcategory/', views.PicClsView.as_view(), name='getimgcategory'),
    path('getimages/<int:id>/', views.ImagesListView.as_view(), name='getimages'),
    path('getimageInfo/<int:id>/', views.ImageInfoView.as_view(), name='getimageInfo'),
    path('getthumimages/<int:id>/', views.ThumImagesView.as_view(), name='getthumimages'),
    path('getgoods/', views.GoodsListView.as_view(), name='getgoods'),
    path('goods/', include('api.goods.urls')),
]