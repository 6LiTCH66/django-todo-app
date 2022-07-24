from django import forms
from .models import Todo
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["todo_text"]
