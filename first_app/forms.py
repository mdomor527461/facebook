from . import models
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = models.UserModel
        fields = ['contact', 'password']
        widgets = {
            'contact': forms.TextInput(attrs={'placeholder': 'Email or Phone Number'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }