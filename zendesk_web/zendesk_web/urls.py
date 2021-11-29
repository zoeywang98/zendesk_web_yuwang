"""zendesk_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.views import static


app_name = 'zendesk_tickets'
urlpatterns = [
    url('admin/', admin.site.urls),
    #get ticket list
    url('ticket/list', views.ticket_list, name='ticket_list'),
    #get ticket detail info
    url(r'^ticket/detail/(?P<id>[0-9]+)$', views.ticket_detail, name='ticket_detail'),
    #call static files, like js and css
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static')
]
