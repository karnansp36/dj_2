from django.urls import path
from .views import register, signin, home2, logout
urlpatterns = [
    path("register/", register, name="register"),
    path("signin/", signin, name="signin"),
    path("home2/", home2, name="home2"),
    path("logout/", logout, name="logout"),

]