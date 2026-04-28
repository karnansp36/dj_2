from django.urls import path
from .views import register, signin, home2, logout, view_post_form, create_post
from .post import CreatePostView, PostListView, PostDetailView, PostCreateView
urlpatterns = [
    path("register/", register, name="register"),
    path("signin/", signin, name="signin"),
    path("home2/", home2, name="home2"),
    path("logout/", logout, name="logout"),
    path("create_post/", create_post, name="create_post"),
    path("form/", view_post_form, name="view_post_form"),
    path("create_post_class/", CreatePostView.as_view(), name="create_post_class"),
    path("post_list/", PostListView.as_view(), name="post_list"),
    path("post_detail/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post_create/", PostCreateView.as_view(), name="post_create"),
    

]