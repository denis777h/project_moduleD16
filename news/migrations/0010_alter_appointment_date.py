# Generated by Django 4.2.9 on 2024-01-16 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2024, 1, 16, 16, 42, 11, 24323)),
        ),
    ]