import smtplib
from datetime import datetime, timedelta
import pytz
from mailing.models import Mailing, Log
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone


def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    mailings = Mailing.objects.filter(status='launched')

    for mailing in mailings:
        try:
            send_mail(
                subject=mailing.message.letter_theme,
                message=mailing.message.letter_body,
                from_email=settings.EMAIL_HOST_USER,
                fail_silently=False,
                recipient_list=[client.email for client in mailing.clients.all()]
            )
            log = Log.objects.create(
                mailing=mailing,
                status_log='successfully',
                server_response='сообщение успешно отправлено в ' + str(timezone.now()),
                owner=mailing.owner
            )
            log.save()
        except smtplib.SMTPException as e:
            log = Log.objects.create(
                mailing=mailing,
                status_log='not_successful',
                server_response='сообщение не отправлено в ' + str(e),
                owner=mailing.owner

            )
            log.save()
    mailing.status = 'launched'
    mailing.save()


def select_mailings():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    mailings = Mailing.objects.filter(start_time__lte=current_datetime).filter(status__in=['launched', 'created', 'completed'])
    for mailing in mailings:
        print(current_datetime)
        print(mailing.next_time_mailing)
        if current_datetime >= mailing.next_time_mailing:
            send_mailing()
            if mailing.periodicity == 'once_day':
                mailing.next_time_mailing += timedelta(days=1)
            elif mailing.periodicity == 'once_week':
                mailing.next_time_mailing += timedelta(days=7)
            elif mailing.periodicity == 'once_monthly':
                mailing.next_time_mailing += timedelta(month=1)
            mailing.save()

def mailing_save():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    mailings = Mailing.objects.filter(start_time__lte=current_datetime).filter(status__in=['launched', 'created', 'completed'])
    for mailing in mailings:
        if mailing.end_time < current_datetime:
            mailing.status = 'completed'
        else:
            if mailing.status == 'created' and mailing.start_time <= current_datetime:
                mailing.status = 'launched'
        mailing.save()


