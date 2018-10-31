# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Whabox(models.Model):
	event=models.CharField(max_length=255)
	token=models.CharField(max_length=255)
	contact_uid=models.CharField(max_length=255)
	contact_name=models.CharField(max_length=255)
	contact_type=models.CharField(max_length=255)
	message_dtm=models.CharField(max_length=255)
	message_uid=models.CharField(max_length=255)
	message_cuid=models.CharField(max_length=255)
	message_dir=models.CharField(max_length=255)
	message_type=models.CharField(max_length=255)
	message_text=models.CharField(max_length=255)
	message_ack=models.CharField(max_length=255)
	
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
	
class wabox_message:
	class Meta:
    		managed = False
	token=models.CharField(max_length=255)
	uid=models.CharField(max_length=255)
	url=models.CharField(max_length=255)
	to=models.CharField(max_length=255)
	
	
	
	
	

	
