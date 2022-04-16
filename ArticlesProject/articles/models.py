from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Article(models.Model):
    """Article model"""
    title = models.CharField(verbose_name='Заголовок', unique=True, max_length=64)
    body = models.TextField(verbose_name='Тело')
    article_types = (
        (1, 'Публичная'),
        (2, 'Закрытая'),
    )
    type = models.IntegerField(verbose_name='Тип', choices=article_types)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
