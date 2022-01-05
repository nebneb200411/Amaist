# import model
from .models import Notifications

# library using in views
from django.views.generic import DetailView, ListView


class NotificationDetailView(DetailView):
    model = Notifications
    template_name = 'notifications/detail.html'

class NoticeListView(ListView):
    model = Notifications
    template_name = "notifications/list.html"
    context_object_name = 'notifications'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Notifications.objects.filter().order_by('-created_at')
        return queryset
