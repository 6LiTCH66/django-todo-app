from django import forms
from .models import Todo


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["todo_text"]
