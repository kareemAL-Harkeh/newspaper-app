from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.views.generic import ListView , DetailView
from django.views.generic.edit import UpdateView , DeleteView ,CreateView
from .models import Article ,Comment

class ArticleListView(LoginRequiredMixin, ListView) :

    model = Article
    template_name = 'article_list.html'
    login_url = 'login'

class ArticleDetailView(LoginRequiredMixin, DetailView) :

    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin ,UserPassesTestMixin ,UpdateView) :

    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'

    def test_func(self) -> bool | None:
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin , DeleteView): # new

    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self) -> bool | None:
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class CommentCreateView(LoginRequiredMixin, CreateView):
    
    model = Comment
    template_name = 'comment_new.html'
    success_url = reverse_lazy('article_list')
    fields = ('comment','article',)
    login_url = 'login'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
   