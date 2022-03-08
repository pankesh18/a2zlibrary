from django.db import models
from django.contrib.auth.models import User 
import datetime
# Create your models here.
class Book(models.Model):
    BookTitle = models.CharField(max_length=1000)
    Author = models.CharField(max_length=1000)
    Publisher = models.CharField(max_length=1000)
    Genre  = models.CharField(max_length=1000)
    Year = models.CharField(max_length=1000)
    Language = models.CharField(max_length=1000)
    Description = models.TextField()
    Tags  = models.CharField(max_length=1000)
    ISBN = models.CharField(max_length=1000)
    Image = models.ImageField(default='../media/book_images/default-movie.jpg',blank=True, upload_to='book_images')
    IssuedBy = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)



class MyBook(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    IssuedDate = models.DateField( default=datetime.date.today)  