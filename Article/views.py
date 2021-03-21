from django.views.generic import CreateView
from .forms import ArticleForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Article
from django.contrib import messages


class ArticleFormCreateView(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    template_name = "Article/create_article.html"
    success_url = reverse_lazy('index')
    model = Article

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        article.save()
        messages.success(self.request, '記事を作成しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '記事の作成に失敗しました')
        return super().form_invalid(form)
