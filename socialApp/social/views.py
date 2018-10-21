# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from social.forms import WhatForm
from django.utils.crypto import get_random_string
from social.forms import WhaboxForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import urllib, urllib2
import json

# Create your views here.

def sendMessage(request):
  print("Ingreso a la funcion SendMessage")
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
      response = urllib2.urlopen(req) 
      data=json.load(response)
      #result = response.read()
      message=data['success']
      print(message)
      return render(request,'social/send.html',{'message':message})  
  else:
    form=WhatForm()
  return render(request,'social/send.html')  

@csrf_exempt
def hooks(request):
  if request.method=='POST':
    event=request.POST.get("event")
    print("El evento es: "+event)
    token=request.POST.get("token")
    print("El token es: "+token)
    contact_uid=request.POST.get("contact[uid]")
    print("El contacto es: "+contact_uid)
    contact_name=request.POST.get("contact[name]")
    print("El contacto es: "+contact_name)
    contact_type=request.POST.get("contact[type]")
    print("El tipo de contacto es: "+contact_type)
   
    message_dtm=request.POST.get("message[dtm]")
    print("El mensaje DTM es: "+message_dtm)
    message_uid=request.POST.get("message[uid]")
    print("El mensaje ID es: "+message_uid)
    message_cuid=request.POST.get("message[cuid]")
    print("El mensaje CUID es: "+message_cuid)
    message_dir=request.POST.get("message[dir]")
    print("El mensaje DIR es: "+message_dir)
    message_type=request.POST.get("message[type]")
    print("El mensaje TYPE es: "+message_type)
    message_body=request.POST.get("message[body]")
    print("El mensaje BODY es: "+message_body)
    message_text=request.POST.get("message[body][text]")
    print("El mensaje es: "+message_text)
    message_ack=request.POST.get("message[ack]")
    print("El ACK del mensaje es: "+message_ack)
    
    return HttpResponse('pong')
