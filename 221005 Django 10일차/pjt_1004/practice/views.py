from django.shortcuts import render, redirect
from practice.models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    article = Article.objects.order_by("-pk")
    context = {
        "article": article,
    }
    return render(request, "practice/index.html", context)


# def new(request):
#     article_form = ArticleForm()
#     context = {
#         "article_form": article_form,
#     }
#     return render(request, "practice/new.html", context=context)


def create(request):
    # title = request.POST.get("title")
    # content = request.POST.get("content")
    # Article.objects.create(title=title, content=content)
    # return redirect("practice:index")

    if request.method == "POST":
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST)
        # 유효성 검사
        if article_form.is_valid():
            # 유효하면 세이브
            article_form.save()
            return redirect("practice:index")
    else:
        article_form = ArticleForm()

    context = {
        "article_form": article_form,
    }
    return render(request, "practice/new.html", context=context)


def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    context = {
        "article": article,
    }
    return render(request, "practice/detail.html", context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 값 가져와서 검증하고, DB에 저장
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 상세보기 페이지로
            article_form.save()
            return redirect("practice:detail", article.pk)
        # 유효성검사 통과하지 않으면 => context부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
        article_form = ArticleForm(instance=article)
    context = {
        "article_form": article_form,
    }
    return render(request, "practice/update.html", context)
