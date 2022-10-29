from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

# 회원 목록 조회
def index(request):
    pass


# 회원 세부 정보 조회
def detail(request, pk):
    pass

# 회원 가입 폼
def signup(request):
    return render(request, 'signup.html')

# 로그인
def login(request):
    return render(request, 'login.html')

# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('main')
