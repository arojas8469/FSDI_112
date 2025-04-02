from django.shortcuts import render
from django.views.generic import (ListView,CreateView,DetailView)
from .models import Post
# Create your views here.

class PostListView(ListView):
    template_name = ""
    model = Post
