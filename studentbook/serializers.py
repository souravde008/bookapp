from rest_framework import serializers
from .models import Author,Book,Student

class StudentSerializer(serializers.ModelSerializer):
    def validate_age(self,value):
        if value < 1:
            return serializers.ValidationError("age can't be zer or nagetives")
        return value
    class Meta:
        model = Student
        fields = ["id","name","age","city","pin_code"]
        # fields ="__all__"


class BookSerializer(serializers.ModelSerializer):
    student_book = StudentSerializer(many=True,read_only=True)
    class Meta:
        model = Book
        # fields = "__all__" 
        fields = ["id", "book_name","book_title","student_book"] 



class AuthorSerializer(serializers.ModelSerializer):
    book_author = BookSerializer(many=True,read_only=True)
    class Meta:
        model = Author
        fields = ["id","name","book_author"]
    

    