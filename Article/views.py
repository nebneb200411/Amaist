from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .forms import ArticleForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Article
from django.contrib import messages


class ArticleFormCreateView(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    template_name = "article/create_article.html"
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


class ArticleView(ListView):
    template_name = 'registration/index.html'
    model = Article
    order_by = '-created_at'


class ArticleListView(ListView, LoginRequiredMixin):
    model = Article
    pagenate_by = 5
    template_name = 'profiles/profile_detail.html'

    def get_queryset(self):
        articles = Article.objects.filter(
            author=self.request.user).order_by('-created_at')
        return articles


class ArticleDetailView(DetailView):
    template_name = 'article/detail.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = Article.objects.filter()(pk=self.kwargs.get('pk'))
        return context


class ArticleModifyView(UpdateView):
    template_name = 'article/modify.html'
    model = Article
