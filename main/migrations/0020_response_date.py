# Generated by Django 2.1 on 2018-08-06 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_remove_response_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='date',
            field=models.DateField(default=datetime.date(2018, 8, 6)),
        ),
    ]