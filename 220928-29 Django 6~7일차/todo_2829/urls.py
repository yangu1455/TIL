from django.urls import path
from . import views

# url namespace
# url을 앱별로 이름으로 분류하는 기능

app_name = "todo_2829"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("", views.read, name="read"),
    path("update/<int:pk_>", views.update, name="update"),
    path("delete/<int:todo_pk>", views.delete, name="delete"),
]
