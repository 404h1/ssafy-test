# accounts/models.py
# accounts app을 생성한다.
# User Model을 정의한다. django의 기본 User 모델을 상속 받는다.

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass