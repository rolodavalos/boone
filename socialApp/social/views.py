# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from social.forms import WhatForm
from social.models import Whabox, Conversation, Message
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from urllib.request import urlopen
import urllib
import json

# Create your views here.

def sendMessage(request):
  
  whabox_list=Whabox.objects.all()
  token='fdbd4dc698df7344218dd467936d0a585bc89b7c07135'
  uid='595991732060'
  custom_uid= get_random_string(length=15)
  if request.method=='POST':
    form=WhatForm(request.POST)
    if form.is_valid():
      to=form.cleaned_data.get("to")
      text=form.cleaned_data.get("text")
      data = urllib.urlencode({"token":token,"uid":uid,"to":to,"custom_uid":custom_uid,"text":text}) 
      req = urllib2.Request('https://www.waboxapp.com/api/send/chat', data) 
      response = urlopen.urlopen(req) 
      data=json.load(response)
      #result = response.read()
      message=data['success']
      print(message)
      return render(request,'social/send.html',{'message':message,'whabox_list':whabox_list})  
  else:
    form=WhatForm()
  return render(request,'social/send.html')  

@login_required
def hooks(request):
  if request.method=='POST':
    whabox= Whabox()
    whabox.event=request.POST.get("event")
    whabox.token=request.POST.get("token")
    whabox.contact_uid=request.POST.get("contact[uid]")
    whabox.contact_name=request.POST.get("contact[name]")
    whabox.contact_type=request.POST.get("contact[type]")
    whabox.message_dtm=request.POST.get("message[dtm]")
    whabox.message_uid=request.POST.get("message[uid]")
    whabox.message_cuid=request.POST.get("message[cuid]")
    whabox.message_dir=request.POST.get("message[dir]")
    whabox.message_type=request.POST.get("message[type]")
    whabox.message_text=request.POST.get("message[body][text]")
    whabox.message_ack=request.POST.get("message[ack]")
    whabox.save()
  
    conversations= Conversation.objects.filter(contact_uid=whabox.contact_uid)
  
    if conversations:
      message=Message()
      message.conversation=conversations.first()
      message.message_text=whabox.message_text
      message.estado=whabox.message_ack
      message.user=request.user
      message.save()
      
    else:
      #Crear nueva conversacion y adjuntar el mensaje
      conversation=Conversation()
      conversation.message_cuid=whabox.message_cuid
      conversation.contact_uid=whabox.contact_uid
      conversation.user=request.user
      conversation.estado=1
      conversation.tipo=2
      conversation.save()
      
      #Guardar mensaje
      message=Message()
      message.conversation=connversations[0]
      message.message_text=whabox.message_text
      message.estado=whabox.message_ack
      message.user=request.user
      message.save()
       
    print(whabox)
    return HttpResponse('pong')
  
def listMessages(request,id):
  contact_uid=id
  messages=Whabox.objects.filter(contact_uid=id)
  if request.method=='GET':
    return render (request,'social/mensajes.html',{'messages':messages,'contact_uid':contact_uid})
    
  
