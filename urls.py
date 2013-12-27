
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import django_twilio

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # Hello world program for Twilio
    url(r'^hello_world/$', 'django_twilio.views.say', {
        'text': 'Hello, world!'
    }),

    # main site for updating texts
    url(r'^main/$', 'mysite.views.main'),

    # send a text message
    url(r'^sms/', 'mysite.views.sms'),
)
