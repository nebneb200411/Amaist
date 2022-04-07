# around sitemaps
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

# models
from article.models import Article
from question.models import Question
from data_library.models import DataLibrary

class ArticleSiteMaps(Sitemap):
    changefreq = "never"
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
        return obj.created_at
