from django.views.generic import ListView, DetailView
from .models import Notification


class Notifications(ListView):
    model = Notification
    template_name = 'home.html'

    def get_queryset(self):
        return self.model.objects.filter(status='new').order_by('created')[:1]

class Landing(ListView):
    model = Notification
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.filter(status='new').order_by('created')[:1]

class Services(ListView):
    model = Notification
    template_name = 'services.html'

    def get_queryset(self):
        return self.model.objects.filter(status='new').order_by('created')[:1]

class Folio(ListView):
    model = Notification
    template_name = 'folio.html'

    def get_queryset(self):
        return self.model.objects.filter(status='new').order_by('created')[:1]

class Blog(ListView):
    model = Notification
    template_name = 'blog.html'

    def get_queryset(self):
        return self.model.objects.filter(status='new').order_by('created')[:1]

class Contact(ListView):
    model = Notification
    template_name = 'contact.html'

    def get_queryset(self):
        return self.model.objects.filter(status='new').order_by('created')[:1]


