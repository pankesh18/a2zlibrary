# Generated by Django 4.0.2 on 2022-03-01 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Library', '0004_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='IssuedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
