# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime


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

def demo(request):
  return render(request,'social/demo.html',{})  
  
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
    
    conversations= Conversation.objects.filter(contact_uid=whabox.contact_uid)
    if conversations:
      conversation=conversations.first()
      message=Message()
      message.conversation=conversation
      message.message_text=whabox.message_text
      message.estado=whabox.message_ack
      conversation.estado=1
      message.direction=1
      message.save() 
      conversation.save()    
    else:
      #Crear nueva conversacion y adjuntar el mensaje
      conversation=Conversation()
      conversation.message_cuid=whabox.message_cuid
      conversation.contact_uid=whabox.contact_uid
      conversation.estado=1
      conversation.red=2
      conversation.save()
      
      #Guardar mensaje
      message=Message()
      message.conversation=conversation
      message.message_text=whabox.message_text
      message.estado=whabox.message_ack
      message.direction=1
      message.save()
    
    return HttpResponse('pong')
  
def listMessages(request):
  conversations=Conversation.objects.order_by('-modified')
  conversation=None
  messages=None
  if conversations: 
    conversation=conversations[0]
    messages=Message.objects.filter(conversation__pk=conversation.pk)
  if request.method=='GET':
    return render (request,'social/mensajes.html',{'conversations':conversations,'conversation':conversation,'messages':messages})
    
def viewMessage(request):
  conversations=None
  conversation=None
  messages=None
  conversations=Conversation.objects.order_by('-modified','estado')
  if request.method=='POST':
    conversation= Conversation.objects.get(contact_uid=request.POST.get('customer_uid'))
    if conversation:
      messages= Message.objects.filter(conversation__pk=conversation.pk)
  else:
    conversation=conversations.first()
  return render (request,'social/mensajes.html',{'conversations':conversations,'messages':messages,'conversation':conversation})       
  
def displayMessage(request):
  return render (request,'social/messajes.html',{}) 
  
def listConversations(request):
  conversations=Conversation.objects.order_by('-modified')
  return render (request,'social/contacts_content.html',{'conversations':conversations})


def showContact(request):
  if request.method=='POST':
    conversation_id=request.POST.get('conversation_id')
    conversation= Conversation.objects.get(pk=conversation_id)
    if conversation:
      conversation.estado=2
      conversation.save()
      print(conversation.contact_uid)
    return render (request,'social/contact_profile.html',{'conversation':conversation})  

def displayMessages4Conversation(request):
  conversation=Conversation.objects.get(pk=request.POST.get('conversation_id'))
  messages= Message.objects.filter(conversation__pk=conversation.pk)
  return render (request,'social/messajes.html',{'messages':messages,'conversation':conversation})
  
  
      
                  
              
    
  
