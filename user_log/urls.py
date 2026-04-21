from django.urls import path
from .views import *
urlpatterns = [
    path("post/", user_post, name="user_post"),
    path("list/", user_list, name="user_list"),
    path("detail/<int:id>", user_detail, name="user_detail"),
    path("delete/<int:id>", user_delete, name="user_delete"),
    path("edit/<int:id>", user_edit, name="user_edit"),
]