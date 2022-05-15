# around sitemaps
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

# models
from article.models import Article
from question.models import Question
from data_library.models import DataLibrary

class IndexSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1.0
    
    def items(self):
        return ['index:index']

    def location(self, item):
        return reverse(item)

class CreateViewsSiteMaps(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['article:CreateArticle', 'question:create', 'data_library:create']

    def location(self, item):
        return reverse(item)

class ListViewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    
    def items(self):
        return ['article:list', 'question:list', 'data_library:list']
    
    def location(self, item):
        return reverse(item)

class ArticlesSiteMaps(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        """
        warning!!
        we have to choose the articles which has already published...
        """
        return Article.objects.filter(is_published=True)

    def location(self, obj):
        """
        docstring
        """
        return reverse('article:article_detail', args=[obj.pk])

    def lastmod(self, obj):
        """
        docstring
        """
        return obj.updated_at

class QuetionsSiteMaps(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Question.objects.all()

    def location(self, obj):
        return reverse('question:detail', args=[obj.pk])

    def lastmod(self, obj):
        return obj.created_at

class DatasSiteMaps(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return DataLibrary.objects.all()

    def location(self, obj):
        return reverse('data_library:detail', args=[obj.pk])

    def lastmod(self, obj):
        return obj.created_at