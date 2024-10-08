from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=20, verbose_name='заголовок')
    content = models.TextField(**NULLABLE, verbose_name='содержимое статьи')
    image = models.ImageField(**NULLABLE, upload_to='blog/image', verbose_name='изображение')
    count_views = models.IntegerField(default=0, verbose_name='просмотры')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    slug = models.CharField(max_length=100, verbose_name="slug")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
