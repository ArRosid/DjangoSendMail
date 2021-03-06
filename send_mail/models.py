from django.db import models


class EmailList(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    send = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)
    last_send = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email
