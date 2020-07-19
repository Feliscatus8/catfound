from django import forms
from django.contrib.auth.forms import UserCreationForm

from volunteers.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name',
                  'last_name', 'district', 'skills', 'phone', 'availability']
