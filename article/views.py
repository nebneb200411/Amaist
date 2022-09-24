from locale import currency
from multiprocessing import context
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from .forms import ArticleForm, ArticleCommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .models import Article, Comment, Tag, Order
from django.contrib import messages
from profiles.models import Profile
from django.db.models import Q
from notifications.models import Notifications
from django.conf import settings
from django.shortcuts import render
import payjp


def key_to_value(dict_obj, key):
    value = dict_obj[key]
    return value


class ArticleFormCreateView(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    template_name = "article/create_article.html"
    success_url = reverse_lazy('article:list')
    model = Article

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().get(request, *args, **kwargs)
        else:
            return redirect('article:list')

    def get_context_data(self, **kawargs):
        context = super().get_context_data(**kawargs)
        return context

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        genre_selected = self.request.POST.getlist('genre')
        genre_selected = genre_selected[0]
        genre_choices = settings.ARTICLE_GENRE_CHOICES
        genre = genre_choices[genre_selected]
        article.genre = genre
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = settings.ARTICLE_GENRE_CHOICES
        return context
    

    def form_invalid(self, form):
        messages.error(self.request, '記事の作成に失敗しました')
        return super().form_invalid(form)


class ArticleListView(ListView):
    template_name = 'article/list.html'
    model = Article
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        article_keyword = self.request.GET.get('article_search')
        tag_keyword = self.request.GET.get('tag_search')
        genre_key = self.request.GET.get('genre_search')
        if (genre_key != None) and (genre_key != '選択肢'):
            genre = key_to_value(settings.ARTICLE_GENRE_CHOICES, genre_key)
        elif genre_key == "選択肢":
            genre = ""
        else:
            genre = ""

        if article_keyword:
            queryset = Article.objects.filter(is_published=True)
            queryset = queryset.filter(
                Q(title__icontains=article_keyword) | Q(content__icontains=article_keyword)).order_by(
                '-created_at'
            )

        elif tag_keyword:
            queryset = Article.objects.filter(is_published=True)
            queryset = Article.objects.filter(
                Q(tag__tag_name__icontains=tag_keyword)).order_by('-created_at')
        
        elif genre:
            queryset = Article.objects.filter(is_published=True)
            queryset = queryset.filter(genre=genre).order_by('-created_at')
            
        else:
            queryset = Article.objects.filter(is_published=True).order_by(
                '-created_at'
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notifications = Notifications.objects.all()
        context['notifications'] = notifications
        context["genres"] = settings.ARTICLE_GENRE_CHOICES
        return context

class ContentsView(DetailView):
    template_name = "article/contents.html"
    model = Article


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
        # get user profile model
        profile = Profile.objects.get(user=article.author)
        context['profile'] = profile

        # get CKEditor form from forms.py
        form = ArticleCommentForm()
        context['form'] = form

        # get new articles
        new_articles = Article.objects.filter(is_published=True).order_by('-created_at')
        if len(new_articles) < 5:
            new_articles = new_articles
        else:
            new_articles = new_articles[0:5]
        context['new_articles'] = new_articles

        # get related articles
        genre = article.genre
        relate_articles = Article.objects.filter(genre=genre, is_published=True).order_by('-created_at')
        if len(relate_articles) < 5:
            relate_articles = relate_articles
        else:
            relate_articles = relate_articles[0:5]
        context['relate_articles'] = relate_articles

        # add PV in here
        article.views += 1
        article.save()

        return context

    def post(self, request, pk):

        # import comment form
        form = ArticleCommentForm(request.POST)

        # saving process
        if form.is_valid():

            # save form at once
            created_comment = form.save(commit=False)

            # get the data going to save
            article_pk = request.POST.get('article_pk')
            article = Article.objects.get(pk=article_pk)
            response_from = self.request.user

            # add data to save
            created_comment.comment_to = article
            created_comment.response_from = response_from
            created_comment.save()
            return redirect(request.META.get('HTTP_REFERER'))


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'article/update.html'
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('article:list')

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        genre_selected = self.request.POST.getlist('genre')
        genre_selected = genre_selected[0]
        genre_choices = settings.ARTICLE_GENRE_CHOICES
        genre = genre_choices[genre_selected]
        article.genre = genre
        article.save()
        pk = article.pk
        created_article = Article.objects.get(pk=pk)
        """タグの作成"""
        tags = self.request.POST.getlist('tags')
        tags_updated = []
        for tag in tags:
            created_tag = Tag.objects.create(tag_name=tag)
            created_tag.save()
            tags_updated.append(created_tag)
        # 初めに更新記事のタグオブジェクトを全部削除
        created_article.tag.all().delete()
        for tag in tags_updated:
            created_article.tag.add(tag)
            created_article.save()
        messages.success(self.request, '記事を作成しました')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        editing_article = self.object
        context['genres'] = settings.ARTICLE_GENRE_CHOICES
        genre_selected = editing_article.genre
        if genre_selected != None:
            genre_dict = {}
            # define value(genre_selected_key) for use it in the outside of for roup process 
            genre_selected_key = '1'
            for k, v in settings.ARTICLE_GENRE_CHOICES.items():
                if v == genre_selected:
                    genre_selected_key = k
                    break
                else: 
                    pass
            genre_dict[genre_selected_key] = genre_selected
            context['genre_selected'] = genre_dict
        else:
            pass
        tags = editing_article.tag.all()
        tags = [tag.tag_name for tag in tags]
        context['tags'] = tags

        return context

class ArticleDeleteView(DeleteView):
    template_name = "article/delete.html"
    model = Article

    def get_success_url(self):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        pk = profile.pk
        return reverse_lazy('profiles:profile_detail', kwargs={'pk':pk})


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
    return redirect('article:list')


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
        return redirect('article:list')


class PaymentView(TemplateView, LoginRequiredMixin):
    template_name = "article/payment.html"
    def get(self, request, article_id):
        article = Article.objects.get(pk=article_id)
        is_payment = article.is_payment
        if is_payment:
            pass
        else:
            return redirect('article:list')
        return render(request, "article/payment.html", {"publick_key": settings.PUBLIC_KEY, "purchase_article":article, "article_id":article_id})
    
    def post(self, request, article_id):
        """
        return result to inform customer payment result
        """
        amount = request.POST.get("amount")
        payjp_token = request.POST.get("payjp-token")
        email = request.POST.get("customer-email")
        article_id = request.POST.get("article-id")

        is_purchased = self.check_purchase(user_id=self.request.user.id, article_id=article_id)
        
        if not is_purchased:
            # get customer token
            customer = payjp.Customer.create(email=email, card=payjp_token)

            # payment
            charge = payjp.Charge.create(
                amount=amount,
                currency="jpy",
                customer=customer.id,
                description="Django example charge",
            )

            if charge:
                article = Article.objects.get(pk=article_id)
                Order.objects.create(
                        user=self.request.user, 
                        customer_id=customer.id,
                        article_id=article,
                        token_id=payjp_token,
                    )
            else:
                return render(request, "article/payment_error.html")
        else:
            return render(request, "article/already_purchased.html")

        #context = {"amount": amount, "customer": customer, "charge": charge, "article_id":article_id}
        return render(request, "article/payment_done.html")
    
    def check_purchase(self, user_id, article_id):
        orders = Order.objects.filter(user_id=user_id, article_id=article_id)
        if orders:
            is_purchased = True
        else:
            is_purchased = False
        return is_purchased