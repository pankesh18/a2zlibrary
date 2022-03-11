# Generated by Django 4.0.2 on 2022-03-11 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0009_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ImageURL',
            field=models.URLField(default=b'N'),
        ),
        migrations.AddField(
            model_name='book',
            name='IsRequested',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='Image',
            field=models.ImageField(blank=True, default='../media/book_images/default.jpg', upload_to='book_images'),
        ),
    ]