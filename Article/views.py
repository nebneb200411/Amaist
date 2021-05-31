from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .forms import ArticleForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Article, Comment
from django.contrib import messages
from profiles.models import Profile


class ArticleFormCreateView(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    template_name = "article/create_article.html"
    success_url = reverse_lazy('profiles:profile_list')
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
    pagenate_by = 20
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
        # pkの取得
        pk = self.kwargs.get('pk')
        context['pk'] = Article.objects.filter(pk=pk)
        # いいねの数
        article = Article.objects.get(pk=pk)
        evaluators = article.good_from.all()
        good_number = evaluators.count()
        context['good_number'] = good_number
        return context


class ArticleModifyView(UpdateView):
    template_name = 'article/modify.html'
    model = Article

# good_counter


def good_count(request):
    if request.method == 'POST':
        pk = request.POST.get('good_count')
        article = Article.objects.get(pk=pk)
        evaluator = request.user
        evaluators = article.good_from.all()
        if evaluator in evaluators:
            article.good_from.remove(evaluator)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            article.good_from.add(evaluator)
            return redirect(request.META.get('HTTP_REFERER'))
    return redirect('index')


# comment funvtion
def comment(request):
    if request.method == 'POST':
        # gain data
        article_pk = request.POST.get('article_pk')
        article = Article.objects.get(pk=article_pk)
        response_from = request.user
        comment_content = request.POST.get('comment')
        # check data
        if not comment_content:
            return redirect(request.META.get('HTTP_REFERER'))
        # save process
        comment = Comment()
        if request.POST.get('response_to').exists():
            response_to = request.POST.get('response_to')
            comment.response_to = response_to
        else:
            pass
        comment.comment_to = article
        comment.response_from = response_from
        comment.comment = comment_content
        comment.save()
        return redirect(request.META.get('HTTP_REFERER'))

    else:
        return redirect('index')
