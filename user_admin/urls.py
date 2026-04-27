from django.urls import path
from .views import register, signin, home2, logout, view_post_form, create_post
urlpatterns = [
    path("register/", register, name="register"),
    path("signin/", signin, name="signin"),
    path("home2/", home2, name="home2"),
    path("logout/", logout, name="logout"),
    path("create_post/", create_post, name="create_post"),
    path("form/", view_post_form, name="view_post_form"),

]