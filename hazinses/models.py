from django.db import models
from django.conf import settings


class SNSMessage(models.Model):
    subject = models.TextField()
    message = models.TextField()

    def __unicode__(self):
        return self.subject


class SentMail(models.Model):
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL)
    subject = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    message_key = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return (self.receiver.username + "-" + self.subject)


class UserEmailProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    notsendmail = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.user.email


class BlackList(models.Model):
    email = models.EmailField()

    def __unicode__(self):
        return self.email
