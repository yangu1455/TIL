from multiprocessing import context
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    # 유효성 검사
    if request.method == "POST":
        # DB에 저장하는 로직
        form = CustomUserCreationForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            # 유효하면 세이브
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()

    context = {
        "form": form,
    }
    return render(request, 'accounts/signup.html', context)


def index(request):
    users = get_user_model().objects.order_by('pk')
    context = {
        'users' : users,
    }
    return render(request, 'accounts/index.html', context)

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user' : user
    }
    return render(request, 'accounts/detail.html', context)