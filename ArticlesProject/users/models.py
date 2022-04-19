from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager):
    """Custom user manager model"""

    def create_user(self, email, role, password=None):
        user = self.model(email=email, role=role)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, role, password=None):
        user = self.create_user(email=email, role=role, password=password)
        user.is_staff = True
        user.us_superuser = True
        user.save()
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model"""
    email = models.EmailField(verbose_name='Адрес электронной почты', unique=True, max_length=64)
    user_roles = (
        (1, 'Подписчик'),
        (2, 'Автор'),
    )
    role = models.IntegerField(verbose_name='Роль', choices=user_roles)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return self.email
