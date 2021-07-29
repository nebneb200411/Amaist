# import template view from django
from django.views.generic import ListView
# import model
from article.models import Article


class IndexView(ListView):
    template_name = 'index.html'
    model = Article

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Article.objects.all().order_by('-created_at')
        return queryset
