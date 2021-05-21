from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('profile_update/<int:pk>/', views.UserProfileUpdateView.as_view(),
         name='profile_update'),
    path('profile_detail/<int:pk>/',
         views.ArticleListView.as_view(), name='article_list'),
    path('profile_detail/<int:pk>/', views.UserProfileDetailView.as_view(),
         name='profile_detail'),
]
