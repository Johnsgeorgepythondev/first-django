from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['name', 'email', 'phone_number', 'date_of_birth']
