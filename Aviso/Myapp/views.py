from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Product

def home(request, slug_c=None):
    page_c = None 
    if slug_c:
        page_c = get_object_or_404(Category, slug=slug_c)
        products = Product.objects.filter(category=page_c, available=True)
    else:
        products = Product.objects.filter(available=True)

    return render(request, 'home.html', {'category': page_c, 'products': products})


def product_detail(request,slug_c,slug_p):
    try: 
        product=Product.objects.get(category__slug=slug_c,slug=slug_p )
    except Exception as e:
        raise e
    return render(request,'products.html',{'products':product})


def signup(request):

    if request.method=="POST":
        username=request. POST['username']
        fname=request. POST['fname']
        lname=request. POST['lname']
        email = request. POST['email']
        password1=request. POST['password1']
        password2=request. POST['password2']
        myuser=User.objects.create_user(username, email, password1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        return redirect('signin')
    return render(request, 'signup.html')


def signin(request):
    
    if request.method=="POST":
        username=request. POST['username']
        password1=request.POST['password1']
        user=authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            fname=user.first_name
            return render(request, 'display.html', {'fname': fname})

        else:
            messages.error(request, "Invalid Credentials")
            return redirect('home')
    return render(request, 'signin.html')
    

def signout(request):
    return render(request,"signout.html")

def payment(request):
    return render(request,"payment.html")

def cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    products = [product]
    total_price = product.price
    context = {'products': products, 'total_price': total_price}
    return render(request, "cart.html", context)


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
