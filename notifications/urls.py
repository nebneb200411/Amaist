from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('detail/<uuid:pk>', views.NotificationDetailView.as_view(), name="detail"),
]
