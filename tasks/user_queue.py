from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from celery import shared_task

@shared_task
def send_mail(template, context, email, subject):
    try:
        html_raw = get_template(template)
        html_content = html_raw.render(context)

        msg = EmailMultiAlternatives(subject, 'Game Chats', "Info <%s>" % settings.DEFAULT_FROM_EMAIL, email)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    except Exception as e:
        logger.error(e.message)