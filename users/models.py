from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    first_name = models.CharField(max_length=100, verbose_name='имя пользователя')
    last_name = models.CharField(**NULLABLE, max_length=100, verbose_name='фамилия')
    surname = models.CharField(**NULLABLE, max_length=100, verbose_name='отчество')

    token = models.CharField(**NULLABLE, max_length=100, verbose_name='токен')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = [
            ('may_block_users', 'may block users'),
            ('can_view_list_of_users', 'can view list of users')
        ]

    def __str__(self):
        return self.email
