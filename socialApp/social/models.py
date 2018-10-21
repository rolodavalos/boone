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
		return self.event+" "+self.token+" "+self.contact_uid+" "+self.contact_name+" "+self.contact_type+" "+self.contact_name+" "+self.message_dtm+" "+self.message_uid+" "+self.message_cuid+" "+self.message_dir+" "+self.message_type+" "+self.message_text+" "+self.message_ack
