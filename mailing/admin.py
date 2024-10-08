from django.contrib import admin
from mailing.models import Mailing, Client, Message, Log


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'status', 'message', 'owner')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'owner')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('letter_theme', 'letter_body', 'owner')


@admin.register(Log)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('status_log', 'server_response', 'mailing', 'owner')