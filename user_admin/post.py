from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import Twitter_Post
class CreatePostView(View):
    template_name = "create_post.html"
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # Handle form submission and create a new post
        # You can access form data using request.POST
        # For example: title = request.POST.get("title")
        # Save the post to the database and redirect to the post list page
        return redirect("post_list")
    
class PostListView(ListView):
    model = Twitter_Post
    template_name = "post_list.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Twitter_Post
    template_name = "post_detail.html"
    context_object_name = "post"

class PostCreateView(CreateView):
    model = Twitter_Post
    template_name = "create_post.html"
    fields = ["title", "content"]
    success_url = "/post_list/"

    def form_valid(self, form):
        #logic
        title = form.cleaned_data["title"]
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Twitter_Post
    template_name = "create_post.html"
    fields = ["title", "content"]
    success_url = "/post_list/"

class PostDeleteView(DeleteView):
    model = Twitter_Post
    success_url = "/post_list/"