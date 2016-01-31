from django.conf.urls import patterns, include, url
from django.contrib import admin
from demo.views import Notifications, Landing, Services, Blog, Folio, Contact

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Landing.as_view(), name='home'),
    url(r'^services/$', Services.as_view(), name='services'),
    url(r'^blog/$', Blog.as_view(), name='blog'),
    url(r'^folio/$', Folio.as_view(), name='folio'),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    url(r'^contact/sent/$', 'demo.views.contactsent', name='contactsent'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

)

