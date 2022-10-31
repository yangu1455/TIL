from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # 글 목록 조회
    path('', views.index, name='index'),
    # 새 글 쓰기 창 띄우기
    path('new/', views.new, name='new'),
    # 새로 쓴 글 저장
    path('create/', views.create, name='create'),
    # 글 세부
    path('detail/<int:pk>', views.detail, name='detail'),
    # 글 수정하기 창
    path('edit/<int:pk>', views.edit, name='edit'),
    # 글 수정 기능
    path('update/<int:pk>', views.update, name='update'),
    # 글 삭제 기능
    path('delete/<int:pk>', views.delete, name='delete'),
]