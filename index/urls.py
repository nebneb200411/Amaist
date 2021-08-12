from . import views
from django.urls import path

app_name = 'index'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('terms/', views.TermsView.as_view(), name="terms"),
]
