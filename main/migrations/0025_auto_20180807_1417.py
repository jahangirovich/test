# Generated by Django 2.1 on 2018-08-07 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_answer_q'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='false',
        ),
        migrations.RemoveField(
            model_name='response',
            name='question',
        ),
        migrations.RemoveField(
            model_name='response',
            name='right',
        ),
    ]
