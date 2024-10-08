from django.db import models
from config import settings
NULLABLE = {'blank': True, 'null': True}

class Client(models.Model):
    email = models.EmailField(verbose_name="почта", unique=True)
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    father_name = models.CharField(**NULLABLE, max_length=100, verbose_name='отчество')
    comment = models.TextField(**NULLABLE, verbose_name='коментарии')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец')
    #владелец(foreigngkey)

    def __str__(self):
        return f'{self.first_name}({self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Mailing(models.Model):
    PERIODICITY_CHOICES = (('once_day', 'раз в день'), ('once_week', 'раз в неделю'), ('once_monthly', 'раз в месяц'))
    STATUS_CHOICES = (('completed', 'завершена'), ('created', 'создана'), ('launched', 'запущена'))
    start_time = models.DateTimeField(**NULLABLE, verbose_name='начало рассылки')
    end_time = models.DateTimeField(**NULLABLE, verbose_name='окончание рассылки')
    periodicity = models.CharField(**NULLABLE, max_length=20, choices=PERIODICITY_CHOICES, verbose_name='периодичность')
    status = models.CharField(**NULLABLE, max_length=20, choices=STATUS_CHOICES, verbose_name='статус рассылки')
    message = models.ForeignKey("Message", on_delete=models.CASCADE, verbose_name='сообщение')
    clients = models.ManyToManyField(Client,verbose_name='клиенты')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец')
    next_time_mailing = models.DateTimeField(**NULLABLE,verbose_name='следующее время расслыки')
    active = models.BooleanField(default=True, verbose_name='Активна рассылка или нет')


    def __str__(self):
        return f'{self.message}'


    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        permissions = [
            ('can_disable_mailing', 'can disable mailing'),
            ('can_view_any_mailing', 'can view any mailing lists')
        ]


#1время старта (datatimefield)
#2время окончания (datatimefield)
#3период(chardfield(чойзес 3 варианта))
#4статус(chardfield(чойзес 3 варианта))
#5сообщение(forenkey:сообщение)
#6клиенты(manytomanyfield:клиенты)
#7владелец(foreignkey:владелец)

class Message(models.Model):
    letter_theme = models.CharField(max_length=100, verbose_name='тема письма')
    letter_body = models.TextField(verbose_name='тело письма')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец')

    def __str__(self):
        return f'{self.letter_theme}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщение'



class Log(models.Model):
    STATUS_CHOICES = (('successfully', 'Успешно'), ('not_successful', 'не успешно'))
    log_time = models.DateTimeField(**NULLABLE, auto_now=True, verbose_name='дата и время последней рассылки')
    status_log = models.CharField(**NULLABLE, max_length=20, choices=STATUS_CHOICES, verbose_name='статус попытки')
    server_response = models.TextField(**NULLABLE, max_length=255, verbose_name='ответ сервера')
    mailing = models.ForeignKey(Mailing, **NULLABLE, on_delete=models.CASCADE, verbose_name='рассылка')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец')

    def __str__(self):
        return self.server_response

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'

#Жата и время(datetimefield)
#статус(charfiekd(успешко ошибка))
#Ответ сервера(Textfield)(опцианально)
#расылка(foreignkey:рассылка)
#Владелец(foreignkey:владелец)


#crud для всех кроме логов