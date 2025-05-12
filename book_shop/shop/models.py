from django.db import models

# Create your models here.
class Books(models.Model):
    objects = None
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=2083)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50)

    def _str_(self):
        return self.first_name