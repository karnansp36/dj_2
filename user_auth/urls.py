from django.urls import path
from .views import signup, login, home, about


urlpatterns = [
    path("signup/", signup ),
    path("login/", login ),
    path("", home ),
    path("about/", about ),
]
