from django.views.generic import ListView
from .models import Notification


class Notifications(ListView):
    model = Notification
    template_name = 'home.html'

    def get_queryset(self):
        return self.model.objects.filter(status='new').order_by('created')[:1]
