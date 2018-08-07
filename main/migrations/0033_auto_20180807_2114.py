# Generated by Django 2.1 on 2018-08-07 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20180807_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Question'),
        ),
        migrations.AlterField(
            model_name='response',
            name='quiz',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.Variant'),
        ),
    ]
