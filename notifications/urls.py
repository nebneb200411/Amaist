from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('detail/<int:pk>', views.NotificationDetailView.as_view(), name="detail"),
]
