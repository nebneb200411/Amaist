from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.ArticleFormCreateView.as_view(), name='CreateArticle'),
    path('index/', views.ArticleView.as_view(), name='article_list'),
]
