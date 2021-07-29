from . import views
from django.urls import path

app_name = 'index'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index")
]
