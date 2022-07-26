from django.shortcuts import redirect, get_object_or_404, render
from django.views import generic, View
from .models import Todo
from .forms import AddTodoForm
from django.contrib import messages
from .forms import UserSignUpForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'todo/index.html'

    context_object_name = "todo_list"

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by("-created_at")


def add_todo(request):
    if request.method == "POST":
        form = AddTodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, "Todo has been added successfully!")
        else:
            messages.error(request, "Field cannot be empty.")
            return redirect('todos:index')

    return redirect('todos:index')


def update_todo(request, todo_id):
    if request.method == "POST":
        todo = get_object_or_404(Todo, pk=todo_id)
        is_completed = request.POST.get('isCompleted', False)

        if is_completed == "on":
            is_completed = True

        todo.is_done = is_completed
        todo.save()
    return redirect('todos:index')


def delete_todo(request, todo_id):
    if request.method == "GET":
        todo = get_object_or_404(Todo, pk=todo_id)
        todo.delete()
    return redirect("todos:index")


def error_404(request, exception):
    return redirect("todos:index")


def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todos:index')
    else:
        form = UserSignUpForm()

    return render(request, 'registration/signup.html', {'form': form})