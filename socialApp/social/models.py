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
	message_body=models.CharField(max_length=255)
	ack=models.CharField(max_length=255)
