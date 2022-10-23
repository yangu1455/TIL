from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login

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

def login(request):
    if request.method == 'POST':
        # AuthenticationForm은 ModelForm이 아님!
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 세션에 저장
            # login 함수는 request, user 객체를 인자로 받는다.
            # user 객체는 어디있어요? 바로 form에서 인증된 유저 정보를 받을 수 있음
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)