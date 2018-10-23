# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


#Custom imports
from social.forms import WhatForm
from social.models import Whabox, Conversation, Message


#URL LIBRARY
from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import urlencode

#JSON LIBRARY
import json

# Create your views here.

def sendMessage(request):
  token='fdbd4dc698df7344218dd467936d0a585bc89b7c07135'
  uid='595991732060'
  custom_uid= get_random_string(length=15)
  if request.method=='POST':
    form=WhatForm(request.POST)
    if form.is_valid():
      to=form.cleaned_data.get("to")
      text=form.cleaned_data.get("text")
      data = urlencode({"token":token,"uid":uid,"to":to,"custom_uid":custom_uid,"text":text}) 
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
    
    conversation= Conversation.objects.get(contact_uid=whabox.contact_uid)
    if conversation:
      message=Message()
      conversation.modified=datetime.date.now()
      message.conversation=conversations.first()
      message.message_text=whabox.message_text
      message.estado=whabox.message_ack
      message.save() 
      conversation.update()    
    else:
      #Crear nueva conversacion y adjuntar el mensaje
      conversation=Conversation()
      conversation.message_cuid=whabox.message_cuid
      conversation.contact_uid=whabox.contact_uid
      conversation.estado=1
      conversation.tipo=2
      conversation.save()
      
      #Guardar mensaje
      message=Message()
      message.conversation=conversation
      message.message_text=whabox.message_text
      message.estado=whabox.message_ack
      message.save()
    
    return HttpResponse('pong')
  
def listMessages(request):
  conversations=Conversation.objects.order_by('-modified')
  if conversations: 
    conversation=conversations[0]
    messages=Message.objects.filter(conversation__pk=conversation.pk)
  if request.method=='GET':
    return render (request,'social/mensajes.html',{'conversations':conversations,'conversation':conversation,'messages':messages})
    
def viewMessage(request,id):
  if request.method=='POST':
    token='fdbd4dc698df7344218dd467936d0a585bc89b7c07135'
    uid='595991732060'
    custom_uid= get_random_string(length=15)
    form=WhatForm(request.POST)
    if form.is_valid():
      conversations= Conversation.objects.filter(contact_uid=id)
      conversation= Conversation.objects.get(contact_uid=id)
      to=form.cleaned_data.get("to")
      text=form.cleaned_data.get("text")
          
      #Comprobe messages
      if conversations:
        message=Message()
        message.conversation=conversations.first()
        message.message_text=text
        message.estado=3
        message.save() 
      else:
        #Crear nueva conversacion y adjuntar el mensaje
        conversation=Conversation()
        conversation.message_cuid=custom_uid
        conversation.contact_uid=to
        conversation.estado=1
        conversation.tipo=2
        conversation.save()
      
        #Guardar mensaje
        message=Message()
        message.conversation=conversation
        message.message_text=whabox.message_text
        message.estado=whabox.message_ack
        message.save()
          
      #TO WHABOX
      data = urlencode({"token":token,"uid":uid,"to":to,"custom_uid":custom_uid,"text":text})
      req = Request('https://www.waboxapp.com/api/send/chat', data.encode()) 
      response= urlopen(req) 
      data=json.load(response)
      message=data['success']
      print(message)
      
    
  ###MOTRAR LOS MENSAJES CARAJO###
  conversations=Conversation.objects.all()
  conversation= Conversation.objects.get(contact_uid=id)
  messages= Message.objects.filter(conversation__pk=conversation.pk)   
  return render (request,'social/mensajes.html',{'conversations':conversations,'messages':messages,'conversation':conversation})       
      
          
          
              
    
  
