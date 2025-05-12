from os import name

from django.http import HttpResponse
from django.shortcuts import render

from shop.form import Bookform, BookForm
from .form import StudentRegistrationForm
from shop.models import Books


# Create your views here.
def home(request):
    books = Books.objects.all()
    print(books)
    return render(request, 'home.html', {'books': books})


def cart(request):
    return render(request, 'cart.html')


def book_register(request):
    if request.method == "POST":
        form = Bookform()

        if form.is_valid():
            form.save()
        return HttpResponse("Successfully registered the book")
    form = Bookform()
    return render(request, 'book_register.html', {'form': form})


def register_student(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Successfully registered the Student")  # Redirect to a success page
    else:
        form = StudentRegistrationForm()
    return render(request, 'registration_form.html', {'form': form})


def book_stock(request, book_stock=None):
    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            book_name=form.cleaned_data['name']
            book_price=form.cleaned_data['price']
            book_stock=form.cleaned_data['stock']
            book=Books.objects.create[name]=book_name,price=book_price,stock=book]
            book.save():

