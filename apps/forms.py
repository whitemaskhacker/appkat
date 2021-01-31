from django import forms
from django.forms import fields
from .models import Sug

class SugForm(forms.ModelForm):
    class Meta(object):
        model = Sug
        fields = ("name" , "email" , "text")
