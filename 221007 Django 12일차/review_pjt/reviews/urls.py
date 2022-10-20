from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.main, name="main"),
    path("index/", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    # create에서는 제목, 내용, 영화 이름, 영화 평점을 입력받는다.
    path("create/", views.create, name="create"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
]
