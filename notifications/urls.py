from django.conf.urls import patterns, include, url
from django.contrib import admin
from demo.views import Notifications, Landing

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Landing.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
