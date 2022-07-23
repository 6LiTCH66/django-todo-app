from django.urls import path
from . import views


app_name = "todos"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.add_todo, name='add'),
    path("<int:todo_id>/update", views.update_todo, name='update'),
    path("<int:todo_id>/delete", views.delete_todo, name='delete')

]