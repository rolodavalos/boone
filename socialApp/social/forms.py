from django import forms
from social.models import Whabox


class WhatForm(forms.Form):
	to=forms.CharField(max_length=100)
	text=forms.CharField(max_length=100)
	
	
