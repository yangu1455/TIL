from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def index(request):
    users = get_user_model().objects.order_by('pk')
    context = {
        'users' : users,
    }
    return render(request, 'accounts/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            form.save()
            # 앱의 index - 회원목록
            # return redirect('accounts:index')
            # 아주 메인 - 버튼들 있는 것
            return render(request, 'index.html')
    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user' : user
    }
    return render(request, 'accounts/detail.html', context)

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

def logout(request):
    pass