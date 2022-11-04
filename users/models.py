from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):

    """Custom User Manager"""

    def create_user(self, email, username=None, password=None):
        if not email:
            raise ValueError("이메일은 필수 항목입니다.")

        email = self.normalize_email(email)

        user = self.model(email=email, username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username=None, password=None):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):

    """유저 모델 정의"""

    email = models.EmailField(max_length=80, unique=True, verbose_name="이메일")
    username = models.CharField(max_length=150, verbose_name="유저명")

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
