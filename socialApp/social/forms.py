from django import forms
from social.models import Whabox


class WhatForm(forms.Form):
	text=forms.CharField(max_length=100)
	
	
