# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from social.forms import WhatForm
from django.utils.crypto import get_random_string
import urllib, urllib2

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
      data = urllib.urlencode({"token":token,"uid":uid,"to":to,"custom_uid":custom_uid,"text":text}) 
      req = urllib2.Request('https://www.waboxapp.com/api/send/chat', data) 
      response = urllib2.urlopen(req) 
      result = response.read()
  else:
    form=WhatForm()
  return render(request,'social/send.html',{'token':token,'uid':uid,'custom_uid':custom_uid})  
    
