# libraries/admin.py
# 관리자 페이지에서 세 모델을 모두 관리 할 수 있어야 한다.

from django.contrib import admin
from .models import Book, Review

admin.site.register(Book)
admin.site.register(Review)