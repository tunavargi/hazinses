import boto.ses
import celery
import datetime
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.conf import settings
from django.http import HttpResponse
from models import UserEmailProfile, SentMail


conn = boto.ses.connect_to_region(
    settings.AMAZON_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)


def get_response_id(response):
    response_id = None
    if 'SendEmailResponse' in response:
        response_id = (response['SendEmailResponse']
                       ['SendEmailResult']
                       ['MessageId'])
    elif 'SendRawEmailResponse' in response:
        response_id = (response['SendRawEmailResponse']
                       ['SendRawEmailResult']
                       ['MessageId'])
    return response_id


@celery.task
def send_email(subject, message, from_email, to_email):
    try:
        User = get_user_model()
        user = User.objects.get(email=to_email[0])
        useremail, created = UserEmailProfile.objects.get_or_create(user=user)

        if useremail.notsendmail:
            if useremail.notsendmail < datetime.now():
                useremail.notsendmail = None
                useremail.save()
                response = conn.send_raw_email(message, from_email, to_email)

                SentMail.objects.create(receiver=user, subject=subject,
                                        message_key=get_response_id(response))
                return HttpResponse("ok")
            else:
                return None
        else:
            response = conn.send_raw_email(message, from_email, to_email)
            SentMail.objects.create(receiver=user, subject=subject,
                                    message_key=get_response_id(response))
            return HttpResponse("ok")
    except (User.DoesNotExist, IntegrityError):
        response = conn.send_raw_email(message, from_email, to_email)
        return HttpResponse("ok")
