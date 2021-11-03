from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_delete, post_save


def user_avatar_directory_path(instance, filename):
    return f'users/avatars/user_{instance.username}/{filename}'


class User(AbstractUser):
    avatar = models.FileField(upload_to=user_avatar_directory_path, verbose_name='Аватар', blank=True)

    class Meta(AbstractUser.Meta):
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
