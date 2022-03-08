from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.booklist, name='home'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('issueBook', views.IssueBook, name='IssueBook'),
    path('returnBook', views.returnBook, name='ReturnBook')
]
