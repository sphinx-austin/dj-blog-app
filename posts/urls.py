from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("blog/", views.home, name='home'),
    path("blogs/", views.blog_page, name='blog'),
]
