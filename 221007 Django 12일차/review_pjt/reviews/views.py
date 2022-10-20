from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


def main(request):
    return render(request, "reviews/main.html")


def index(request):
    reviews = Review.objects.order_by('pk')
    context = {
        'reviews' : reviews 
    }
    return render(request, "reviews/index.html",context)


def detail(request, pk):
    # 특정 글을 가져온다.
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)


def create(request):
        if request.method == "POST":
        # DB에 저장하는 로직
            review_form = ReviewForm(request.POST)
            # 유효성 검사
            if review_form.is_valid():
                # 유효하면 세이브
                review_form.save()
                return redirect("reviews:index")
        else:
            review_form = ReviewForm()

        context = {
            "review_form": review_form,
        }
        return render(request, "reviews/create.html", context=context)


def update(request, pk):
    pass


def delete(request, pk):
    pass
