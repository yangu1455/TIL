from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # 회원 목록 조회
    path('', views.index, name='index'),
]