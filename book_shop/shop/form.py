from django import forms, models
from .models import Books, Student


# class Bookform(forms.ModelForm):
#     class Meta:
#         models = Books
#         fields = '__all__'

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class BookForm(forms.Form):
    name = models.CharField(label="Enter the Name of the Book", max_length=150)
    price = models.DecimalField(label="Enter the Price")
    stock = models.IntegerField()


class Bookform:
    def is_valid(self):
        pass