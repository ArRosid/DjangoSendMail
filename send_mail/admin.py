from django.contrib import admin

from . import models


class EmailListAdmin(admin.ModelAdmin):
    list_display = ('email', 'send', 'last_send')
    fields = ('email',)


admin.site.register(models.EmailList, EmailListAdmin)