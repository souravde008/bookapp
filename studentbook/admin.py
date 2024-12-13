from django.contrib import admin

# Register your models here.
from .models import Author,Book,Student

admin.site.register([Author,Book,Student])