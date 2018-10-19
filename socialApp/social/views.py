# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
form social.forms import WhatForm

# Create your views here.

def sendMessage(request):
  if request.method=='POST':
    form=WhatForm(request.POST)
  else:
    form=WhatForm()
  return render(request,'social/send.html')  
    
