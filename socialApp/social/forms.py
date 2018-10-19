from django import forms

class WhatForm(forms.Form):
	to=forms.CharField(max_length=100)
	text=forms.CharField(max_length=100)
