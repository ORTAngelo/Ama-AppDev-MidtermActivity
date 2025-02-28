from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm, ProductForm
from .models import Product 

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect('login')
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == "POST": 
        form = SignUpForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, 'register.html', {"form": form})


def logout_user(request):
    logout(request)
    return redirect('login')

def product_list(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        return render(request, 'product.html', {'products': products})
    else:
        return redirect('home')
    
def add_product(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('product')
        else:
            form = ProductForm()
        return render(request, 'addProduct.html', {'form': form})
    return redirect('login')

def update_product(request, pk):
    if request.user.is_authenticated:
        curent_product = Product.objects.get(id=pk)
        form = ProductForm(request.POST or None, instance=curent_product)
        if form.is_valid():
            form.save()
            return redirect('product')
        return render(request, 'updateProduct.html', {'form':form})
    else:
        form = ProductForm(instance=Product)
    return redirect('login')

def delete_product(request, pk):
     if request.user.is_authenticated:
        delete_record = Product.objects.get(id=pk)
        delete_record.delete()
        return redirect("product")
     else:
        return redirect('login')
     
def confirm_delete(request, pk):
    if request.user.is_authenticated:
        product = Product.objects.get(id=pk)

        if request.method == 'POST':
            product.delete()
            messages.success(request, f'Product was successfully deleted!')
            return redirect('product') 

        return render(request, 'confirmDelete.html', {'product': product})
    else:
        return redirect('login')


             


