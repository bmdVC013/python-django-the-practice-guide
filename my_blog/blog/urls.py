from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("admin/", admin.site.urls),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
]
