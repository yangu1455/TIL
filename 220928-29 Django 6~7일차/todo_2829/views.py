from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    # 모든 글 목록을 보여준다
    # 1. DB에서 모든 글을 불러온다.
    todos = Todo.objects.all()

    # 2. template에 보내준다.
    context = {
        "todos": todos,
    }
    return render(request, "todo_2829/index.html", context)


def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")

    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    return redirect("todo_2829:index")


def read(request):
    todos = Todo.objects.all()
    context = {
        "todos": todos,
    }

    return render(request, "todo_2829/index.html", context)


def update(request, pk_):
    # update할 특정 데이터를 불러온다. -> pk_를 사용해서
    todo = Todo.objects.get(pk=pk_)

    # True -> False
    # False -> True
    todo.completed = not todo.completed

    # 데이터 수정한 것을 반영
    todo.save()

    return redirect("todo_2829:index")


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect("todo_2829:index")
