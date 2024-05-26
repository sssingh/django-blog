from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

from django.forms import Form


def home(request):
    latest_posts = Post.objects.all().order_by("-created")[:3]
    return render(request, "home.html", {"latest_posts": latest_posts})


class BlogListView(ListView):
    model = Post
    template_name = "blog/browse_posts.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/detail_post.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "blog/create_post.html"
    fields = ["title", "author", "image_credit", "body"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog/edit_post.html"
    fields = ["title", "image_credit", "body"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    # If delete successful then go to this page
    success_url = reverse_lazy("list-posts")
