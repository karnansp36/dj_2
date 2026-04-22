from django.shortcuts import render, redirect
from .forms import UserSignupForm
from .models import User_signup
from django.contrib import messages
# Create your views here.
from .utils import hash_password, verify_password, login_required
def register(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = hash_password(form.cleaned_data["password"])

            if User_signup.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
            else:
                User_signup.objects.create(name=username, email=email, password=password)
                messages.success(request, "Registration successful.")
                # return render(request, "a_signup.html", {"form":UserSignupForm()})
        else:
            messages.error(request, "Invalid form submission.")
    return render(request, "a_signup.html", {"form":UserSignupForm()})


def signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User_signup.objects.get(email=email)
            if verify_password(password, user.password):
                request.session["user_id"] = user.id
                messages.success(request, "Login successful.")
                
            else:
                messages.error(request, "Invalid email or password.")
        except User_signup.DoesNotExist:
            messages.error(request, "Invalid email or password.")
    return render(request, "a_signin.html")


def logout(request):
    request.session.flush()
    messages.success(request, "You have been logged out.")
    return redirect("signin")


@login_required
def home2(request):
    # if "user_id" not in request.session:
    #     messages.error(request, "You must be logged in to view this page.")
    #     return redirect("signin")
    return render(request, "home2.html")