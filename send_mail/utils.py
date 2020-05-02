from . import models
from django.core.mail import send_mail


def handle_upload_email(file):
    for chunk in file.chunks():
        email_list = chunk.decode().splitlines()
        # print(email_list)
        for email in email_list:
            try:
                models.EmailList.objects.create(email=email)
            except:
                print("email already exists")


def send_email(number_of_email):
    email_list = models.EmailList.objects.filter(send=False).order_by('added_at')[:int(number_of_email)]
    subject = "Kursus Mikrotik, Cisco, Network Automation Termurah Terlengkap! Hanya 100rb-an"
    message = "serius ini murah banget bro, kursus cisco, mikrotik, network automation di udemy"
    from_ = 'ahmadrosid30121997@gmail.com'

    send_mail(
        subject,
        message,
        from_,
        email_list,
        fail_silently=False,
    )

# todo send email as important
# todo template email
# todo change from name
# todo update sent status and last sent after send email
