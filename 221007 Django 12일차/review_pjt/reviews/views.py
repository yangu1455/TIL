from django.shortcuts import render, redirect


def main(request):
    return render(request, "reviews/main.html")


def index(request):
    return render(request, "reviews/index.html")


def detail(request):
    pass


def create(request):
    pass


def update(request):
    pass


def delete(request):
    pass
