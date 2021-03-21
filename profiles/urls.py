from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('profile_update/', views.UserProfileUpdateView.as_view(),
         name='ProfileUpdate'),
    path('', views.UserProfileView.as_view(), name='Profile')
]
