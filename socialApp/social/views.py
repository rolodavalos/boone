# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime
import urllib.request as urllib2
import urllib


#Custom imports
from social.forms import WhatForm
from social.models import Whabox, Conversation, Message, WhaboxSender


#JSON LIBRARY
import json

# Create your views here.

def demo(request):
  return render(request,'social/demo.html',{})  
  
def sendMessage(request):
  token='fdbd4dc698df7344218dd467936d0a585bc89b7c07135'
  uid='595991732060'
  url='https://www.waboxapp.com/api/send/chat'
  custom_uid= get_random_string(length=15)
  if request.method=='POST':
    form=WhatForm(request.POST)
    if form.is_valid():
      destino=form.cleaned_data.get("destino")
      text=form.cleaned_data.get("text")
      print(destino)
      print(text)
      data = urllib.parse.urlencode({"token":token,"uid":uid,"to":"595992647616","custom_uid":custom_uid,"text":text}).encode('utf-8') 
      req = urllib2.Request(url, data) 
      response = urllib2.urlopen(req)
      
      
      #data=json.load(response)
      #result = response.read()
      #message=data['success']
      #print(message)
      return render(request,'social/send.html',{})  
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
    
    conversations= Conversation.objects.filter(contact_uid=whabox.contact_uid).exclude(estado=3)
    if conversations:
      conversation=conversations.first()
    else:
      #Crear nueva conversacion y adjuntar el mensaje
      conversation=Conversation()
      conversation.contact_uid=whabox.contact_uid
      conversation.message_cuid=get_random_string(length=15)
      
      
      #Accionar a la nueva conversacion
      token='fdbd4dc698df7344218dd467936d0a585bc89b7c07135'
      uid='595991732060'
      url='https://www.waboxapp.com/api/send/chat'
      custom_uid= get_random_string(length=15)   
      wbs= WhaboxSender(token,uid,url,custom_uid)
      text="Usted se ha comunicado a Pytyvo. En breve será atendido"
      result= wbs.sendMessage(text,conversation.contact_uid)
      
      if result:
        print("Se ha enviado correctmente el mensaje")
      else:
        print("No se ha podido enviar el mensaje")
    
    #Trabajar por el mensaje
    message=Message()
    message.conversation=conversation
    message.message_text=whabox.message_text
    message.estado=whabox.message_ack
    message.direction=1
    conversation.estado=1
    conversation.red=2
    
    #Grabar
    conversation.save()
    message.save()
      
    return HttpResponse('pong')
  

def viewMessage(request):
  conversations=None
  conversations=Conversation.objects.order_by('-modified')
  conversation=conversations.first()
  if request.method=='POST':
    conversation= Conversation.objects.get(contact_uid=request.POST.get('customer_uid'))
  return render (request,'social/mensajes.html',{'conversations':conversations,'conversation':conversation})       
  
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
  return render (request,'social/messajes.html',{'conversation':conversation})
  
  
      
                  
              
    
  
