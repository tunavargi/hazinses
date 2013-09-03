import boto.ses
import celery
import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
from hazinses.models import UserEmailProfile, SentMail


conn = boto.ses.connect_to_region(
    settings.AMAZON_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)


@celery.task
def send_email(subject, message, from_email, to_email, mail_subject):
    user = User.objects.get(username=to_email)
    useremail, created = UserEmailProfile.objects.get_or_create(user=user)
    if useremail.notsendmail:
        if useremail.notsendmail < datetime.now():
            useremail.notsendmail = None
            useremail.save()
            response = conn.send_email(from_email, message, subject, [to_email])
            response_id = response['SendEmailResponse']['SendEmailResult']\
                ['MessageId']
            SentMail.objects.create(receiver=user, subject=mail_subject,
                                    message_key=response_id)
            return HttpResponse("ok")
        else:
            return None
    else:
        response = conn.send_email(from_email, message, subject, [to_email])
        response_id = response['SendEmailResponse']['SendEmailResult']\
            ['MessageId']
        SentMail.objects.create(receiver=user, subject=mail_subject,
                                message_key=response_id)
        return HttpResponse("ok")