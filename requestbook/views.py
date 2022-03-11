import json
import os
from pickle import TRUE
from telnetlib import STATUS
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import requests
from django.http import HttpResponse
import urllib3
from django.core.files import File
from Library.models import Book, MyBook
from library_management.settings import MEDIA_URL,MEDIA_ROOT
import logging

logger = logging.getLogger('warning')



@login_required
def reqbook(request):
    return render(request, 'requestbook/requestbook.html')



def addreqbook(request):
    try:
        if  MyBook.objects.filter(user=request.user).count()>=3:
            
            response = HttpResponse(json.dumps({'msg': f'You cant issue more books. Please return previous books'}), 
            content_type='application/json')
            response.status_code=400
            return response
        else:
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


            book = Book(BookTitle=BookTitle, Author=Author,Publisher=Publisher,Genre=Genre, Year=Year,Language= Language,Description= Description,Tags= Tags,ISBN=ISBN, IssuedBy=request.user, IsRequested=True, ImageURL=imgurl)

            book.save()

            oldbooks= MyBook.objects.filter(book=book)
            oldbooks.delete()

            mybk= MyBook(book=book,user=request.user)
            mybk.save()

            return HttpResponse(status=200)
    except Exception as err:
        logger.error(err)
        return redirect('error')





