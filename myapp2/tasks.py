from celery import shared_task
from django.core.mail import send_mail
from redismail import settings

@shared_task(bind=True)
def send_ad_mails(self, message):
    recipient_list = ["xxxxx@gmail.com"]
    mail_subject = "You are on your luck day!"
    send_mail(
        subject = mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list,
        fail_silently=False,
        )
    return "Done"
    