from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Products, Cart


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        else:
            User.objects.create_user(username=name, email=email, password=password)
            messages.success(request, "Account created successfully!")
            return redirect('login')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip()
        password = request.POST.get('password')

        users = User.objects.filter(email=email)
        if users.exists():
            username = users.first().username
            user = authenticate(request, username=username, password=password)
        else:
            user = None

        if user:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'login.html')


@login_required()
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')


def headphones_view(request):
    products = Products.objects.filter(category="headphones")
    return render(request, 'headphones.html', {'products': products})


def watch(request):
    products = Products.objects.filter(category="watch")
    return render(request, 'watch.html', {'products': products})


def backpack(request):
    products = Products.objects.filter(category="backpack")
    return render(request, 'backpack.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def cart(request, pk=None):
    current_user = request.user

    # If user is not logged in, don't fetch cart items
    if not current_user.is_authenticated:
        return render(request, 'cart.html', {'cart_items': []})

    if pk:
        product = get_object_or_404(Products, product_id=pk)
        product_exists = Cart.objects.filter(product=product, user=current_user).exists()
        if product_exists:
            messages.info(request, "Product already in cart")
            return redirect('cart')
        Cart.objects.create(product=product, user=current_user)

    cart_items = Cart.objects.filter(user=current_user)
    return render(request, 'cart.html', {'cart_items': cart_items})


@login_required()
def delete_cart(request, pk):
    current_user = request.user
    product = get_object_or_404(Products, pk=pk)
    Cart.objects.filter(product=product, user=current_user).delete()
    messages.success(request, f"{product.product_name} removed from your cart.")
    return redirect('cart')
