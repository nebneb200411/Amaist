from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name="list"),
    path('create/', views.ArticleFormCreateView.as_view(), name='CreateArticle'),
    path('article_detail/<int:pk>',
         views.ArticleDetailView.as_view(), name='article_detail'),
    path('good_count/', views.good_count, name='good_count'),
    path('comment/', views.comment, name='comment'),
]
