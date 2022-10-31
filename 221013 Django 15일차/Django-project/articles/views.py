from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    pass

def detail(request, pk):
    return render(request, 'articles/detail.html')

def edit(request, pk):
    return render(request, 'articles/edit.html')

def update(request, pk):
    pass

def delete(request, pk):
    pass
