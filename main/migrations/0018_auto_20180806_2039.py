# Generated by Django 2.1 on 2018-08-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20180806_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='date',
            field=models.DateField(default=6),
        ),
    ]
