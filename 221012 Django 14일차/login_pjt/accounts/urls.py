from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # 회원 목록 조회
    path('', views.index, name='index'),
    # 회원가입
    path('signup/', views.signup, name='signup'),
    # 회원 세부정보 조회
    path('<int:pk>/', views.detail, name='detail'), 
    # 로그인
    path('login/', views.login, name='login'),
    # 로그아웃
    path('logout/', views.logout, name='logout'),
]
