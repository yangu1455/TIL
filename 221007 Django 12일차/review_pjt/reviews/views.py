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
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 값 가져와서 검증하고, DB에 저장
        review_form = ReviewForm(request.POST, instance=review)
        # 유효성 검사
        if review_form.is_valid():
            # 유효하면 세이브
            review_form.save()
            # 유효성 검사 통과하면 상세보기 페이지로
            return redirect("reviews:detail", review.pk)

    # 유효성검사 통과하지 않으면 => context부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
        review_form = ReviewForm(instance=review)

    context = {
        "review_form": review_form,
    }
    return render(request, "reviews/update.html", context)


def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect('reviews:index')
