# Generated by Django 3.0.5 on 2020-05-02 03:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('send_mail', '0004_auto_20200502_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='emaillist',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
