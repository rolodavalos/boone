from django import forms
from social.models import Whabox
import json

class WhatForm(forms.Form):
	to=forms.CharField(max_length=100)
	text=forms.CharField(max_length=100)
	
class WhaboxForm(forms.ModelForm):
	jsonfield = forms.CharField(max_length=1024)
	def clean_jsonfield(self):
		jdata = self.cleaned_data['jsonfield']
         	json_data = json.loads(jdata) 
         	return jdata
	
	
