from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404

from .models import Category, Product


# Create your views here.
def home(request, slug_c=None):
    page_c = None
    if slug_c !=None :
        page_c = get_object_or_404(Category, slug=slug_c)
        product = Product.objects.all().filter(category=page_c, available=True)
    else:
        product = Product.objects.all().filter(available=True)
    return render(request, 'home.html', {'category': page_c, 'product': product})


def contact(request):
    return render(request, 'contact.html')
