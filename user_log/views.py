from django.shortcuts import render, redirect
from .forms import UserPostForm
from .models import UserPost
# Create your views here.
def user_post(request):
    if request.method =="POST":
        form = UserPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, "user_post.html", {"forms":UserPostForm()} )


def user_list(request):
    post = UserPost.objects.all()
    return render(request, "user_list.html", {"posts":post})

def user_detail(request, id):
    post = UserPost.objects.get(id=id)
    return render(request, "user_detail.html", {"post":post})

def user_delete(request, id):
    post = UserPost.objects.get(id=id)
    post.delete()
    return redirect("user_list")

def user_edit(request, id):
    post = UserPost.objects.get(id=id)
    if request.method =="POST":
        form = UserPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("user_list")
    return render(request, "user_post.html", {"forms":UserPostForm(instance=post)} )