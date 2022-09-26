"""todaypjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from practices import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path(주문서, 어디서 index를 핸들링해야하는지! views 안의 index라는 함수!)
    path("index/", views.index),
    path("ping/", views.ping),
    path("pong/", views.pong),
    path("is-odd-even/<int:number_>", views.is_odd_even),
    path("calculate/<int:number1>/<int:number2>", views.calculate),
    path("input/", views.input),
    path("output/", views.output),
    path("lorem/", views.lorem),
]
