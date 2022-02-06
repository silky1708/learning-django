from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<str:page_id>', views.posts, name='posts')
]