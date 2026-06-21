from django.core.mail import send_mail
from django.http import HttpResponse
from datetime import datetime


def send_test_email(email):
    send_mail(
        subject="NajotForbes",
        message="Bizning najotForbes saytimizga xush kelibsiz",
        from_email="aigemini01072012a@gmail.com",       # Must match EMAIL_HOST_USER
        recipient_list=[f"{email}"],
        fail_silently=False,                     # Set to True to suppress SMTP exceptions
    )
    return True

def send_test_email_login(email):
    send_mail(
        subject="Yunibirich",
        message=f"Akkauntingizda login qilindi {datetime.now()} da Agar siz ro'yxatdan o'tgan bo'lsangiz",
        from_email="aigemini01072012a@gmail.com",       # Must match EMAIL_HOST_USER
        recipient_list=[f"{email}"],
        fail_silently=False,                     # Set to True to suppress SMTP exceptions
    )
    return True