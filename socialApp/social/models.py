# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
		return event+" "+token+" "+contact_uid+" "+contact_name+" "+contact_type+" "+contact_name+" "+message_dtm+" "+message_uid+" "+message_cuid+" "+message_dir+" "+message_type+" "+message_text+" "+message_ack
