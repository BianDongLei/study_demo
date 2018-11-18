from django.urls import path
from django.conf.urls import  url
import blog.views as dv

urlpatterns = [
    path('index/', dv.index),
    path('articles/', dv.main),
    url(r'^article/(?P<article_id>[0-9])/$', dv.article_page),
    url(r'^article/(?P<article_id>[0-9])/edit/$', dv.edit_page),
    url(r'^article/(?P<article_id>[0-9])/edit/action/$', dv.edit_action)
]