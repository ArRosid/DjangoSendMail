from django.shortcuts import render
from . import models


def home(request):
    email_list = models.EmailList.objects.all()
    context = {
        'email_list': email_list
    }
    return render(request, "send_mail/home.html", context)