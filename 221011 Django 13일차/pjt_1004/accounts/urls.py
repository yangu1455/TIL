from django.urls import path
from . import views

# app name 쓰는 이유?
# 우리는 기본적으로 URL을 모두 변수화해서 쓰고 있음
# Template, View에서 직접 '/accounts/' X
# app_name과 path 이름으로

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.detail, name='detail'),
]
