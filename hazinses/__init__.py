from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.message import sanitize_address
from .tasks import send_email


class EmailBackend(BaseEmailBackend):

    def send_messages(self, email_messages):
        for email_message in email_messages:
            from_email = sanitize_address(email_message.from_email,
                                          email_message.encoding)
            recipients = [sanitize_address(addr, email_message.encoding)
                          for addr in email_message.recipients()]
            try:
                send_email(email_message.subject.title(),
                           email_message.message().as_string(),
                           from_email,
                           recipients)
            except:
                if not self.fail_silently:
                    raise
