# Generated by Django 2.1 on 2018-08-05 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_response_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='points',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='response',
            name='answer',
            field=models.IntegerField(),
        ),
    ]