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


def new(request):
    # article_form = ArticleForm()
    # context = {"article_form": article_form}
    return render(request, "practice/new.html")


def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    Article.objects.create(title=title, content=content)
    return redirect("practice:index")

    # if request.method == 'POST':
    #     # DB에 저장하는 로직
    #     article_form = ArticleForm(request.POST)
    #     if article_form.is_valid():
    #         article_form.save()
    #         return redirect('practice:index')
    # else:
    #     article_form = ArticleForm()
    # context = {
    #     'article_form': article_form
    # }
    # return render(request, 'practice/new.html', context=context)
