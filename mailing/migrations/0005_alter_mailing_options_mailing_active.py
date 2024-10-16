# Generated by Django 4.2.2 on 2024-10-07 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_mailing_next_time_mailing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'permissions': [('can_disable_mailing', 'can disable mailing'), ('can_view_any_mailing', 'can view any mailing lists')], 'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылки'},
        ),
        migrations.AddField(
            model_name='mailing',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активна рассылка или нет'),
        ),
    ]
