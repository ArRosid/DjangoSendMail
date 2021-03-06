# Generated by Django 3.0.5 on 2020-05-02 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('send', models.BooleanField(default=False)),
                ('last_send', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
