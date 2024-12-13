from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Author(BaseModel):
    name = models.CharField(max_length=300,default='Not Specified')

    def __str__(self):
        return str(self.name)

class Book(BaseModel):
    book_name = models.CharField(max_length=300,default='No Name')
    book_title= models.TextField(max_length=500,default='No Title')
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name = 'book_author',null = True,blank=True)

    def __str__(self):
        return str(self.book_name)

class Student(BaseModel):
    name = models.CharField(max_length=300,default='unknown')
    age = models.IntegerField(default=1, null=True, blank=True)
    pin_code = models.IntegerField(default=0)
    city= models.TextField(max_length=500,default='unknown')
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name = 'student_book',null = True,blank=True)

    def __str__(self):
        return str(self.name)
