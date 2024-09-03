from django import forms
from django.urls import reverse, reverse_lazy

from . import models

   

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            'delivery_address', 
            'phone_number',
            'add_inform'
            ]


