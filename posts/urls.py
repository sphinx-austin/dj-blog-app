from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.blog_page, name='blog'),
    path("post/<str:pk>", views.post, name='post'),
]
