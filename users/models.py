from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.urls import reverse


class UserManager(BaseUserManager):
    # カスタムユーザマネージャ
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        # emailを必須にする
        if not email:
            raise ValueError('The given email must be set')
        # emailでuserモデルを作成
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    # カスタムユーザモデル
    initial_point = 50000
    email = models.EmailField('メールアドレス', unique=True)
    username = models.CharField(max_length=100, unique=True)
    point = models.PositiveIntegerField(default=initial_point)
    is_staff = models.BooleanField('is_staff', default=False)
    is_active = models.BooleanField('is_active', default=True)
    date_joined = models.DateTimeField('date_joined', default=timezone.now)
    date_posted = models.DateTimeField('date_posted', default=timezone.now)
    icon = models.ImageField(upload_to='icon/', blank=True, null=True)

    objects = UserManager()

    # 作成を成功したら'ginstagram:profile'と定義されているURLに飛ぶ
    def get_absolute_url(self):
        return reverse(
            'app:profile', kwargs={'username': self.username})

    USERNAME_FIELD = 'email'
    EMAL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
