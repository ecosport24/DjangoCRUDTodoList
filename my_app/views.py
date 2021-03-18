from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from django.db.models import Q

# Create your views here.


def home(request):
    todo_items = models.Todo.objects.all().order_by("-added_date")
    return render(request, "my_app/index.html", {'todo_items': todo_items})


def add_todo(request):
    todo_text = request.POST.get("todo_text")
    models.Todo.objects.create(text=todo_text)

    return HttpResponseRedirect('/')


def delete_todo(request, todo_id):
    models.Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')


def select_todo(request, todo_id):
    todo_items = models.Todo.objects.filter(~Q(id=todo_id)).order_by("-added_date")
    data = models.Todo.objects.filter(id=todo_id)[0]

    return render(request, "my_app/update.html", {'data': data, 'todo_items': todo_items})


def update_todo(request):
    # print(request.POST.get("todo_text"))
    # print(request.POST.get("todo_id"))
    todo_id = request.POST.get("todo_id")
    todo_text = request.POST.get("todo_text")
    models.Todo.objects.filter(id=todo_id).update(text=todo_text)
    return HttpResponseRedirect('/')
