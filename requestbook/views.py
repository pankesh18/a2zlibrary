import json
from telnetlib import STATUS
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from django.http import HttpResponse

from Library.models import Book, MyBook
from library_management.settings import MEDIA_URL,MEDIA_ROOT

@login_required
def reqbook(request):
    return render(request, 'requestbook/requestbook.html')



def addreqbook(request):
  


    BookTitle = request.POST.get("book[BookTitle]",None)
    Author =    request.POST.get("book[Author]",None)
    Publisher = request.POST.get("book[Publisher]",None)
    Genre  = 'General'
    Year = request.POST.get("book[Year]",None)
    Language = request.POST.get("book[Language]",None)
    Description = request.POST.get("book[Description]",None)
    Tags  = 'N/A'
    ISBN = request.POST.get("book[ISBN]",None)


    imgurl=request.POST.get("book[ImageURL]",None)
    # print(imgurl)
    # with open(MEDIA_ROOT +"/book_images/" +request.POST.get("book[BookTitle]",None)+".jpg", 'wb') as handle:
    #     data = requests.get(imgurl, stream=True).content
    #     print(data)
    #     handle.write(data)


    book = Book(BookTitle=BookTitle, Author=Author,Publisher=Publisher,Genre=Genre, Year=Year,Language= Language,Description= Description,Tags= Tags,ISBN=ISBN, IssuedBy=request.user)

    book.save()

    oldbooks= MyBook.objects.filter(book=book)
    oldbooks.delete()

    mybk= MyBook(book=book,user=request.user)
    mybk.save()

    return HttpResponse(status=200)





