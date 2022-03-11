# from asyncio.windows_events import NULL
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book,MyBook
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import logging

logger = logging.getLogger('warning')

@login_required
def booklist(request):
    try:
        if request.method == 'POST':
            search_key=request.POST.get('search',None)
            if not search_key:
                books=Book.objects.all()
            else:
                books=Book.objects.filter(BookTitle__contains=search_key)
        else:
            books=Book.objects.all()


        paginator = Paginator(books, 9)
        page_number = request.GET.get('page',1)
        page_obj = paginator.get_page(page_number) 
        context ={
            'page_obj': page_obj
        }
        return render(request, 'Library/booklist.html', context)
    except Exception as err:
        logger.error(err)
        return redirect('error')




@login_required
def IssueBook(request):
    try:

        if  MyBook.objects.filter(user=request.user).count()>=1:
            
            response = HttpResponse(json.dumps({'msg': f'You cant issue more books. Please return previous books'}), 
            content_type='application/json')
            response.status_code=400
            return response
            
        else:

            book = request.POST.get("id",None)
            bk=Book.objects.get(pk=book)
            bk.IssuedBy = request.user
            bk.save()
            print("book saved")


            oldbooks= MyBook.objects.filter(book=bk)
            print(oldbooks)
            oldbooks.delete()

            mybk= MyBook(book=bk,user=request.user)
            mybk.save()
            print("My book saved")

            response = HttpResponse(json.dumps({'msg': f'Your book has been issued'}), 
            content_type='application/json')
            response.status_code=200    
            return response
    except Exception as err:
        logger.error(err)
        return redirect('error')




@login_required
def mybooks(request):
    try:
        context ={
            'mybooks':MyBook.objects.filter(user=request.user)
        }
        return render(request, 'Library/mybooks.html', context)
    except Exception as err:
        logger.error(err)
        return redirect('error')







@login_required
def returnBook(request):
    try:
        book = request.POST.get("id",None)
        bk=Book.objects.get(pk=book)
        bk.IssuedBy = None
        bk.save()
        print("book saved")


        oldbooks= MyBook.objects.filter(book=bk)
        print(oldbooks)
        oldbooks.delete()

        print("book returned")

        return HttpResponse(status=200)
    except Exception as err:
        logger.error(err)
        return redirect('error')




