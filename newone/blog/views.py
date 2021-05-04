from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views import generic
from .models import Post

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'Home.html'




class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'



class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = {'title', 'author', 'body'}


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'