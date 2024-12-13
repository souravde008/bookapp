from django.shortcuts import render
from .models import Author,Book,Student
from .serializers import AuthorSerializer,BookSerializer,StudentSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer