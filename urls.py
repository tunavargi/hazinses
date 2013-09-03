from django.conf.urls import patterns, include, url
from hazinses.views import SNSMessageView

sns_message = SNSMessageView

urlpatterns = patterns(
    '',
    url(r'^sns/$',
        sns_message.as_view(),
        name="sns_message")
)
