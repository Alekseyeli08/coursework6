# Generated by Django 4.2.2 on 2024-10-07 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('may_block_users', 'may block users'), ('can_view_list_of_users', 'can view list of users')], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
