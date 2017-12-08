from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Article

# Create your views here.


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'description']


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'description']


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:list')
