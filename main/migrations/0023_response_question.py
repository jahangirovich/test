# Generated by Django 2.1 on 2018-08-07 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20180807_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='question',
            field=models.TextField(blank=True),
        ),
    ]
