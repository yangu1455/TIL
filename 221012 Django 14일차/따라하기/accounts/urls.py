from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # 회원가입 create
    # CustomUserCreationForm을 활용해서 회원가입 구현
    path('signup/', views.signup, name='signup'),
    # 회원 목록 조회 read
    path('', views.index, name='index'),
    # 회원 정보 조회 read
    path('<int:pk>/', views.detail, name='detail'),
    # 로그인
    path('login/', views.login, name='login'),
]


