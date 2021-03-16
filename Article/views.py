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

    def save(self, form):
        article = form.save(commit=False)
        article.user = self.request.user
        article.save()
        messages.success(self.request, '記事を作成しました')
        return super().save(form)

    def save_fail(self, form):
        messages.error(self.request, '記事の作成に失敗しました')
