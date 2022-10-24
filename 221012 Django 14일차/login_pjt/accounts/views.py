from symbol import pass_stmt
from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    users = get_user_model().objects.order_by('pk')
    context = {
        'users' : users,
    }
    return render(request, 'accounts/index.html', context)

def signup(request):
    pass

def detail(request, pk):
    pass

def login(request):
    pass

def logout(request):
    pass