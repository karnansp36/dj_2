from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import  redirect

def hash_password(password):
    return make_password(password)

def verify_password(password, hashed_password):
    return check_password(password, hashed_password)

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if "user_id" not in request.session:
            return redirect("signin")
        return view_func(request, *args, **kwargs)
    return wrapper