# Generated by Django 2.1 on 2018-08-06 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20180805_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='right',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='right',
            name='false',
        ),
        migrations.AddField(
            model_name='right',
            name='false',
            field=models.ManyToManyField(related_name='false', to='main.Answer'),
        ),
        migrations.RemoveField(
            model_name='right',
            name='right',
        ),
        migrations.AddField(
            model_name='right',
            name='right',
            field=models.ManyToManyField(related_name='right', to='main.Answer'),
        ),
    ]
