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
    event=request.POST.get("message[body]")
    print(event)
    return HttpResponse('pong')
