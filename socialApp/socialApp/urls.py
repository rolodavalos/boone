"""socialApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from social import views as social_views
from braces.views import CsrfExemptMixin

class Object(CsrfExemptMixin, social_views):
    authentication_classes = []

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('social/', social_views.sendMessage,name='send_message'),
    url('social/hooks/',social_views.hooks,name='hooks'),
]
