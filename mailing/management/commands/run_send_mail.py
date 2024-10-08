from django.core.management.base import BaseCommand
from mailing.services import send_mailing
from mailing.models import Client

class Command(BaseCommand):
    def handle(self, *args, **options):
        for client in Client.objects.all():
            send_mailing()
