from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
     path('profile_update/<uuid:pk>/', views.UserProfileUpdateView.as_view(),
          name='profile_update'),
     path('profile_detail/<uuid:pk>',
          views.profile_not_found, name='profile_detail'),
     path('profile_detail/<uuid:pk>/', views.UserProfileDetailView.as_view(),
          name='profile_detail'),
     path('profile_create/', views.UserProfileCreateView.as_view(),
          name='profile_create'),
     path('found_or_not_found/',
          views.profile_not_found, name='found_or_not_found'),
]

"""
path('follow_or_unfollow/', views.follow_unfollow_view,
     name='follow_unfollow_view'),
path('', views.ProfileListView.as_view(), name='profile_list'),
"""
"""
path('profile/<uuid:pk>/', views.OtherUserProfileView.as_view(),
     name='otheruser_profile'),
path('follower_list/<uuid:pk>/', views.FollowerListView.as_view(), name = "follower_list"), 
path('follwing_list/<uuid:pk>/', views.FollowingListView.as_view(), name = "following_list"), 
"""
