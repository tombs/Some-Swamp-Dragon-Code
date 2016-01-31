from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Notification
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def contactsent(request, *args, **kwargs):
    from django.core.mail import send_mail
      
    if request.method == 'POST':
 
        name = request.POST.get('name','')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','') 
        message = request.POST.get('message','')    

        body = str(email) + "\n\n" + str(phone) + "\n\n\n\n" + str(message)
        title = 'DoubleSpace PH Contact Request from: ' + str(name)

        send_mail(title, body, settings.EMAIL_HOST_USER, settings.EMAIL_CONTACT_RECIPIENTS, fail_silently=False)        
        response_data = {}
        return HttpResponse(json.dumps(response_data),content_type="application/json")


    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
