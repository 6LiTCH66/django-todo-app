from django import forms
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["todo_text"]


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
        }