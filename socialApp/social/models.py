# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

#Custom imports
import urllib.request as urllib2
import urllib
import json
import time

class Whabox(models.Model):
	event=models.CharField(max_length=255,null=True)
	token=models.CharField(max_length=255,null=True)
	contact_uid=models.CharField(max_length=255,null=True)
	contact_name=models.CharField(max_length=255,null=True)
	contact_type=models.CharField(max_length=255,null=True)
	message_dtm=models.CharField(max_length=255,null=True)
	message_uid=models.CharField(max_length=255,null=True)
	message_cuid=models.CharField(max_length=255,null=True)
	message_dir=models.CharField(max_length=255,null=True)
	message_type=models.CharField(max_length=255,null=True)
	message_text=models.CharField(max_length=255,null=True)
	message_ack=models.CharField(max_length=255,null=True)
	
	def __str__(self):
		return self.event+" "+self.token+" "+self.contact_uid+" "+self.contact_name+" "+self.contact_type+" "+self.contact_name+" "+self.message_dtm+" "+self.message_uid+" "+self.message_cuid+" "+self.message_dir+" "+self.message_type+" "+self.message_text+" "+self.message_ack

class Tipo(models.Model):
	title=models.CharField(max_length=50)
	description=models.CharField(max_length=255)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	created=models.DateTimeField(auto_now_add=True)
	modified=models.DateTimeField(auto_now=True)
	
class Conversation(models.Model):
	STATUS = (
    	(1, ("open")),
    	(2, ("process")),
    	(3, ("close"))
	)
	RED = (
    	(1, ("TW")),
    	(2, ("WA")),
    	(3, ("FB")),
	(4, ("IG"))
	)
	
	message_cuid=models.CharField(max_length=255)
	contact_uid=models.CharField(max_length=255)
	created=models.DateTimeField(auto_now_add=True)
	modified=models.DateTimeField(auto_now=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	estado= models.IntegerField(choices=STATUS)
	red=models.IntegerField(choices=RED)
	tipo=models.ForeignKey(Tipo,on_delete=models.CASCADE,null=True)
	
	def __str__(self):
		return self.message_cuid+" "+self.contact_uid

	
class Message(models.Model):
	STATUS = (
    	(0, ("NOT SEND")),
    	(1, ("SEND")),
    	(2, ("DELIVERED")),
	(3, ("READ")),
	)
	DIR = (
    	(1, ("I")),
    	(2, ("O"))
	)
	conversation=models.ForeignKey(Conversation,on_delete=models.CASCADE)
	message_text=models.CharField(max_length=255)
	direction= models.IntegerField(choices=DIR)
	estado=models.IntegerField(choices=STATUS)
	created=models.DateTimeField(auto_now_add=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	
class WhaboxSender:
  def __init__(self, token, uid, url, custom_uid):
    self.token = token
    self.uid = uid
    self.url = url
    self.custom_uid = custom_uid
          
  def sendMessage(self, message, to):	
    data = urllib.parse.urlencode({"token":self.token,"uid":self.uid,"to":to,"custom_uid":self.custom_uid,"text":message}).encode('utf-8') 
    req = urllib2.Request(self.url,data)
    response = urllib2.urlopen(req)
    result = response.read().decode('utf-8')
    #Obtener el resultado JSON
    obj=json.loads(result)
    message=obj['success']
    return message
                	
class Agente(models.Model):
	STATUS = (
    (1, ("En linea")),
    (2, ("Ocupado")),
    (3, ("Receso")),
    (4, ("Baño"))
	)
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	created=models.DateTimeField(auto_now_add=True)
	modified=models.DateTimeField(auto_now=True)
	estado= models.IntegerField(choices=STATUS)
	
	def __str__(self):
		return self.user.username
	
	
	
	
	

	
