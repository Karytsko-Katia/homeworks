from django import forms
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ValidationError

from . import models


def dennis_validator(value):
    if value[0:6] != "Dennis":
        raise ValidationError("Name must start with Dennis!")
    
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _
# def validate_even(value):
#     if value % 2 != 0:
#         raise ValidationError(
#             _("%(value)s is not an even number"),
#             params={"value": value},
#         )


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=123,
        min_length=1,
        required=True,
        label="Enter your name!",
        )
    message = forms.CharField(
        widget=forms.Textarea,
        required=True,
        label="Leave your message!"
        )
    def clean(self, *args, **kwargs):
        cleaned_data = super().clean(*args, **kwargs)
        name = cleaned_data["name"]
        message = cleaned_data["message"]
        if name[0:6] == "Dennis" and message[0:5] != "Hello":
                raise ValidationError("If the name is Dennis, message must start with Hello!")
        return cleaned_data
 
        
#    subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)

# можно вписать валидар прямо в модель или форму(класс)
# здесь выполняется проверка поля 'recipients':
# def clean_recipients(self):
#         data = self.cleaned_data["recipients"]
#         if "fred@example.com" not in data:
#             raise ValidationError("You have forgotten about Fred!")

#         # Always return a value to use as the new cleaned data, even if
#         # this method didn't change it.
#         return data


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