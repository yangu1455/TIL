from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from accounts.forms import CustomUserCreationForm

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
        if form.is_vaild():
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
    return render(request, 'accounts/detail.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    pass