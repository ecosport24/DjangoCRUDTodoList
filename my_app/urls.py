from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_todo', views.add_todo, name="add_todo"),
    path('delete_todo/<int:todo_id>', views.delete_todo, name="delete_todo"),
    path('select_todo/<int:todo_id>', views.select_todo, name="select_todo"),
    path('update_todo', views.update_todo, name="update_todo"),
]