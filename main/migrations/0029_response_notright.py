# Generated by Django 2.1 on 2018-08-07 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_test_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='notright',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]