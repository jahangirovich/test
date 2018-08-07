# Generated by Django 2.1 on 2018-08-05 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20180805_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='answer',
            name='correct',
            field=models.BooleanField(default=False, help_text='Это правильный ответ?'),
        ),
    ]