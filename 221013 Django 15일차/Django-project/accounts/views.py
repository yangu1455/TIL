from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# 회원 목록 조회

def index(request):
    users = get_user_model().objects.order_by('pk')
    context = {
        'users' : users,
    }
    return render(request, 'accounts/index.html', context)

# 회원 세부 정보 조회

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user' : user,
    }
    return render(request, 'accounts/detail.html', context)

# 회원 가입 폼
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 바로 로그인 시켜주는 경우
            # user = form.save()  # ModelForm의 save 메서드의 리턴값은 해당 모델의 인스턴스다!
            # auth_login(request, user)  # 로그인
        
            # 로그인 시켜주지 않고 로그인 창으로 보내는 경우
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

# 로그인
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 세션에 저장
            # login 함수는 request, user 객체를 인자로 받음
            # user 객체는 어디있어요? 바로 form에서 인증된 유저 정보를 받을 수 있음
            auth_login(request, form.get_user())
            # local~/accounts/login/?next=/articles/1/update/
            # request.GET.get('next') : /articles/1/update/

            # if request.GET.get('next'):
            #     return redirect(request.GET.get('next'))
            # else:
            #     return redirect('accounts:index')
            return redirect(request.GET.get('next') or 'main')
    else:
        form = AuthenticationForm()

    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('main')
