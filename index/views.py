# import template view from django
from django.views.generic import ListView, TemplateView
# import model
from article.models import Article
from django.conf import settings
from django.db.models import Q

def key_to_value(dict_obj, key):
    value = dict_obj[key]
    return value

class IndexView(ListView):
    template_name = 'index.html'
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
        context["genres"] = settings.ARTICLE_GENRE_CHOICES
        return context
    


class TermsView(TemplateView):
    template_name = 'terms.html'

class AdministratorInformation(TemplateView):
    template_name = 'administrator_information.html'