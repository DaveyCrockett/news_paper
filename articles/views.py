from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from accounts.models import CustomUser
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here.
class ArticleListView(ListView):
    template_name = "article_list.html"
    model = Article

class ArticleDetailView(DetailView):
    template_name = "article_detail.html"
    model = Article

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "new_article.html"
    model = Article
    fields = ["title", "body", "author"]

class ArticleUpdateView(LoginRequiredMixin , UserPassesTestMixin, UpdateView):
    template_name = "edit_article.html"
    model = Article
    fields = ["title", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeletView(LoginRequiredMixin , UserPassesTestMixin,DeleteView):
    template_name = "delete_article.html"
    model = Article
    success_url = reverse_lazy('articles')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
