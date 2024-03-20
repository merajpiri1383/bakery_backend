from django.core.mail import EmailMultiAlternatives,send_mail
from django.conf import settings
from django.template.loader import render_to_string
from threading import Thread
def send_async_email(user): 
    html = render_to_string("user/email.html",{"code":user.otp_code})
    mail = EmailMultiAlternatives(
        subject="کد فعال سازی",
        body="کد تایید برای فعال سازی ایمیل...",
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email]
    )
    mail.attach_alternative(html,"text/html")
    mail.send()
def send_email(user):
    task = Thread(target=send_async_email,args=[user])
    task.start()