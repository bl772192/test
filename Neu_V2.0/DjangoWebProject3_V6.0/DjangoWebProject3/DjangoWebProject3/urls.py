"""
Definition of urls for DjangoWebProject3.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

from app import views
from rest_framework.urlpatterns import format_suffix_patterns

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact/', app.views.contact, name='contact'),
    url(r'^about/', app.views.about, name='about'),
    url(r'^login/',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/login/',
        },
        name='logout'),

    url(r'^admin/', admin.site.urls),

    url(r'^input/', views.Inputs.as_view()),

    url(r'^output/', views.Outputs.as_view()),
 
    #url(r'^IAS_Cloud/', app.views.IAS_Cloud, name='IAS_CLoud'),

    url(r'^account/', include('app.urls')),

    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^regelung/', app.views.regelung, name='regelung'),

    url(r'^monitoring/', app.views.monitoring, name='monitoring'),

    #url(r'^test/', app.views.test, name='test'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
]

"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #Stocks 
    url(r'^stocks/', views.StockList.as_view()),
]
"""

urlpatterns = format_suffix_patterns(urlpatterns)