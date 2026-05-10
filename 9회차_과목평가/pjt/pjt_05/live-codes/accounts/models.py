from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 기존 필드들은 모두 상속받음
    pass
    # --- 우리가 추가하고 싶은 필드들 ---
    nickname = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)


# 프로필 모델 예시
class Profile(models.Model):
    age = models.PositiveIntegerField(blank=True, null=True, default=0)
    weekly_avg_reading_time = models.PositiveIntegerField(blank=True, null=True)
    # blank, null 옵션 가능
    # default 옵션으로 0 등 지정 가능