# Generated by Django 5.1 on 2024-10-03 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='заголовок')),
                ('content', models.TextField(blank=True, null=True, verbose_name='содержимое статьи')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/image', verbose_name='изображение')),
                ('count_views', models.IntegerField(default=0, verbose_name='просмотры')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('slug', models.CharField(max_length=100, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
