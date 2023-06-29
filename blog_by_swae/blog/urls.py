from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts,name='posts'),
    path('newpost/',views.new_post_upload),
    path('posts/<str:id>',views.post,name='post_det'),
]