# Generated by Django 4.0.2 on 2022-03-02 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0006_mybook'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybook',
            name='IssuedDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]