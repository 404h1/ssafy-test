# accounts/admin.py
# 관리자 페이지에서 세 모델을 모두 관리 할 수 있어야 한다.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)