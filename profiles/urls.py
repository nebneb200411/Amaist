from django.urls import path
from . import views
from article.views import ArticleListView

app_name = 'profiles'

urlpatterns = [
    path('profile_update/<int:pk>/', views.UserProfileUpdateView.as_view(),
         name='profile_update'),
    # path('profile_detail/<int:pk>/',
    # ArticleListView.as_view(), name='article_list'),
    path('profile_detail/<int:pk>/', views.UserProfileDetailView.as_view(),
         name='profile_detail'),
    path('follow_or_unfollow/', views.follow_unfollow_view,
         name='follow_unfollow_view'),
    path('', views.ProfileListView.as_view(), name='profile_list'),
    path('profile_create/', views.UserProfileCreateView.as_view(),
         name='profile_create'),
    path('found_or_not_found/',
         views.profile_not_found, name='found_or_not_found'),
]
