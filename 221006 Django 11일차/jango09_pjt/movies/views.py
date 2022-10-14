from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


# Create your views here.
def index(request):
    movies = Movie.objects.order_by('pk')
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/detail.html', context)


def create(request):
    # 유효성 검사
    if request.method == "POST":
        # DB에 저장하는 로직
        movie_form = MovieForm(request.POST)
        # 유효성 검사
        if movie_form.is_valid():
            # 유효하면 세이브
            movie_form.save()
            return redirect("movies:index")
    else:
        movie_form = MovieForm()

    context = {
        "movie_form": movie_form,
    }
    return render(request, "movies/new.html", context=context)


def update(request):
    pass


def delete(request):
    pass
