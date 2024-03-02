from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product
from main.form import ProductForm

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products' : products})

def seller_index(request):
    products = Product.objects.all()
    return render(request, 'seller_index.html', {'products' : products})

def customer_index(request):
    products = Product.objects.all()
    return render(request, 'customer_index.html', {'products' : products})

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product.html', {'product': product})

def avatarView(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            return redirect('/')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form' : form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.groups.filter(name='Seller').exists():
                # Logic for seller
                return redirect('/seller_index')
            elif request.user.groups.filter(name='Customer').exists():
                # Logic for customer
                return redirect('/customer_index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')

def seller_signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        # confirm_password = request.POST['confirm_passsword']
        
        data = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password,)
        data.save()
        return redirect('/')
    
    return render(request, 'signup_seller.html')

def customer_signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        data = User.objects.create_user(email=email, username=username, password=password,)
        data.save()
        return redirect('/')
    
    return render(request, 'signup_customer.html')

def logout_page(request):
    logout(request)
    return redirect('/')
