from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta: 
        model = User 
        fields = ("username", "email", "password1", "password2")


    def save(self, commit: bool = True) -> Any:
        user = super(UserForm, self).save(commit=False)
        user.email = self.changed_data['email']
        if commit: 
            user.save()
        return user