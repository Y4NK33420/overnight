# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Registration Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Add a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# Login Form (optional customization)
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
