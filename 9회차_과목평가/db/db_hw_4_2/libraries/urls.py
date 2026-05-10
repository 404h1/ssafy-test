# libraries/urls.py
# 책 전체 목록을 확인 할 수 있는 페이지를 제공한다.
# 책 상세 정보를 확인 할 수 있는 페이지를 제공한다.

from django.urls import path
from . import views

app_name = 'libraries'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_pk>/', views.detail, name='detail'),
]