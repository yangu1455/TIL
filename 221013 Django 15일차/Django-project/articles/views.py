from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review' : review,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    Review.objects.create(title=title, content=content)

    # context = {
    #     'title' : title,
    #     'content' : content,
    # }

    return redirect('articles:index')
    # return render(request, 'article:index', context)

def edit(request, pk):
    review = Review.objects.get(pk=pk)

    context = {
        'review' : review,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    review = Review.objects.get(pk=pk)

    title = request.GET.get('title')
    content = request.GET.get('content')

    review.title = title
    review.content = content

    review.save()
    return redirect('articles:detail', review.pk)

def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect('articles:index')
