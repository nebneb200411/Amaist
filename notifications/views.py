# import model
from .models import Notifications

# library using in views
from django.views.generic import DetailView


class NotificationDetailView(DetailView):
    model = Notifications
    template_name = 'notifications/detail.html'
