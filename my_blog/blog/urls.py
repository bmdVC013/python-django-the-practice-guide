from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:blog_name>", views.blog_detail, name="blog-detail")
]
