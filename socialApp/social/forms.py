from django import forms
from social.models import Whabox


class WhatForm(forms.Form):
	cid=forms.CharField(max_length=100)
	destino=forms.CharField(max_length=100)
	text=forms.CharField(max_length=100)
	
	
