from django.db import models


class EmailList(models.Model):
    email = models.EmailField(max_length=100)
    send = models.BooleanField(default=False)
    last_send = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
