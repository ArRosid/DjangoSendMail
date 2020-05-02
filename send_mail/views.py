from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from . import models
from . import utils

def home(request):
    email_list = models.EmailList.objects.all()
    context = {
        'email_list': email_list
    }
    return render(request, "send_mail/home.html", context)


def upload_email(request):
    if request.method == 'POST':
        email_file = request.FILES['email_file']
        utils.handle_upload_email(email_file)

    return render(request, 'send_mail/email_upload.html')
