from . import models

def handle_upload_email(file):
    for chunk in file.chunks():
        email_list = chunk.decode().splitlines()
        # print(email_list)
        for email in email_list:
            try:
                models.EmailList.objects.create(email=email)
            except:
                print("email already exists")