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
from django.urls import path
from django.contrib import admin
from social import views as social_views

urlpatterns = [
    path('admin/', admin.site.urls),
  #  path('mensajes/',social_views.listMessages,name='list_messages'),
    path('mensajes/',social_views.viewMessage,name='view_message'), 
   # path('messages/',social_views.displayMessage,name='display_message'),
  #  path('social/', social_views.sendMessage,name='send_message'),
    path('hooks',social_views.hooks,name='hooks'),
    path('contact/',social_views.showContact,name='show_contact'),
    path('conversations/',social_views.listConversations,name='list_conversations'),
    path('conversation/<str:id>',social_views.displayMessages4Conversation),
    
]
