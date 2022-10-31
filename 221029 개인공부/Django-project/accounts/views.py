from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm


# Create your views here.

# 회원 목록 조회
def index(request):
    pass


# 회원 세부 정보 조회
def detail(request, pk):
    pass

# 회원 가입 폼
def signup(request):
    return render(request, 'accounts/signup.html')

# 로그인
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('main')
