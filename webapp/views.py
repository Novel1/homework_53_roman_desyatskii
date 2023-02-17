from django.http import HttpResponseNotFound

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from webapp.models import ToDo


# Create your views here.
def index_view(request: WSGIRequest):
    return render(request, 'index.html')


def todolist_view(request: WSGIRequest):
    todo = ToDo.objects.all()
    context = {
        'todo': todo
    }
    return render(request, 'todolist.html', context=context)


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'add_todo.html')
    print(request.POST)
    context = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'created_at': request.POST.get('data')
    }
    todo = ToDo.objects.create(**context)
    return redirect(reverse('inform', kwargs={'pk': todo.pk}))


def info_view(request, pk):
    try:
        todo = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return HttpResponseNotFound('<h1>Not Found</h1>')
    return render(request, 'information.html', context={
        'todo': todo
    })
