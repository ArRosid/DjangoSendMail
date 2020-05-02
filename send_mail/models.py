from django.db import models


class EmailList(models.Model):
    email = models.EmailField(max_length=100)
    send = models.BooleanField(default=False)
    last_send = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email

# todo import email dari csv