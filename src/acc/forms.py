from django import forms
from typing import Any
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ValidationError

from . import models


class ProfileCreateForm(forms.ModelForm):
    delivery_address = forms.CharField(
         max_length=500,
         required=True, 
         label="Delivery adress",
         widget=forms.Textarea
         )
    phone_number = forms.CharField(
          max_length=15,
          required=True, 
          label="Phone number",
          widget=forms.TextInput
          )
    add_inform = forms.CharField(
          max_length=300,
          required=False,
          label="Additional information",
          widget=forms.Textarea 
          )
    class Meta:       
        model = models.CustomerProfile          
        fields = ['delivery_address', 'phone_number']
    # phone_number = forms.CharField(
    #      max_length=15,
    #      required=True, 
    #      label="Phone number",
    #      widget=forms.TextInput
    #      )
    # add_inform = forms.Textarea(
    #      max_length=300,
    #      required=False,
    #      label="Additional information",
    #      widget=forms.Textarea 
    #      )
 
    
# class DummiItemCreateForm(forms.ModelForm):
#     class Meta:
#          newfield with my parametrs = describe new field
#          model = models.DummiItem
#          fields = ['title', 'cover', 'newfield with my parametrs']


# class BasicForm(forms.Form):
#     name = forms.CharField(
#         max_length=123,
#         min_length=1,
#         required=True,
#         label="Enter your name!",
#         )

