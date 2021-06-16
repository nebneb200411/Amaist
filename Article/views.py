from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .forms import ArticleForm  # TagInlineFormSet
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Article, Comment, Tag
from django.contrib import messages
from profiles.models import Profile
from django.db.models import Q


class ArticleFormCreateView(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    template_name = "article/create_article.html"
    success_url = reverse_lazy('profiles:profile_list')
    model = Article

    def get_context_data(self, **kawargs):
        context = super().get_context_data(**kawargs)
        return context

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        article.save()
        pk = article.pk
        created_article = Article.objects.get(pk=pk)
        """タグの作成"""
        tags = self.request.POST.getlist('tags')
        tag_created = []
        for tag in tags:
            created_tag = Tag.objects.create(tag_name=tag)
            created_tag.save()
            tag_created.append(created_tag)
        for tags in tag_created:
            created_article.tag.add(tags)
            created_article.save()
        messages.success(self.request, '記事を作成しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '記事の作成に失敗しました')
        return super().form_invalid(form)


class ArticleListView(ListView):
    template_name = 'article/index.html'
    model = Article
    order_by = '-created_at'

    def get_queryset(self):
        queryset = super().get_queryset()
        article_keyword = self.request.GET.get('article_search')
        tag_keyword = self.request.GET.get('tag_search')
        if article_keyword:
            queryset = Article.objects.filter(
                Q(title__icontains=article_keyword) | Q(content__icontains=article_keyword))

        elif tag_keyword:
            queryset = Article.objects.filter(
                Q(tag__tag_name__icontains=tag_keyword))
        else:
            queryset = Article.objects.all()
        return queryset


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
        # コメントの表示
        comment_objects = Comment.objects.filter(comment_to=article)
        context['comment_objects'] = comment_objects
        # Tagの取得
        tags = article.tag.all()
        context['tags'] = tags
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
        if 'User' in request.POST.get('response_to'):
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
