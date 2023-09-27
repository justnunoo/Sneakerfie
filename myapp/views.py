from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import MainImage, Cart,  ShoeColor, ShoeSize
import random, time, os
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    boxee = MainImage.objects.all()
    boxes = list(boxee)
    random.seed(time.time())
    random.shuffle(boxes)
    
    return render(request, 'index.html', {'boxes' : boxes})

def adidas(request):

    boxes = []
    source = "static\\adidas"
    boxee = MainImage.objects.all()
    boxed = list(boxee)
    random.seed(time.time())
    random.shuffle(boxed)

    for i in boxed:
        img_path = os.path.join("static", i.img)  # Assuming the images are stored in the static folder
        dir_name = os.path.dirname(img_path)
        if dir_name == source:
            boxes.append(i)

    return render(request, 'adidas.html', {'boxes': boxes})

def nike(request):

    boxes = []
    source = "static\\nike"
    boxee = MainImage.objects.all()
    boxed = list(boxee)
    random.seed(time.time())
    random.shuffle(boxed)

    for i in boxed:
        img_path = os.path.join("static", i.img)  # Assuming the images are stored in the static folder
        dir_name = os.path.dirname(img_path)
        if dir_name == source:
            boxes.append(i)
            random.seed(time.time())
            random.shuffle(boxes)
    return render(request, 'nike.html', {'boxes': boxes})

def jordan(request):
    boxes = []
    source = "static\\jordan"
    boxee = MainImage.objects.all()
    boxed = list(boxee)
    random.seed(time.time())
    random.shuffle(boxed)

    for i in boxed:
        img_path = os.path.join("static", i.img)  # Assuming the images are stored in the static folder
        dir_name = os.path.dirname(img_path)
        if dir_name == source:
            boxes.append(i)

    return render(request, 'jordan.html', {'boxes': boxes})

def puma(request):

    boxes = []
    source = "static\\puma"
    boxee = MainImage.objects.all()
    boxed = list(boxee)
    random.seed(time.time())
    random.shuffle(boxed)

    for i in boxed:
        img_path = os.path.join("static", i.img)  # Assuming the images are stored in the static folder
        dir_name = os.path.dirname(img_path)
        if dir_name == source:
            boxes.append(i)

    return render(request, 'puma.html', {'boxes': boxes})

def new_balance(request):

    boxes = []
    source = "static\\new_balance"
    boxee = MainImage.objects.all()
    boxed = list(boxee)
    random.seed(time.time())
    random.shuffle(boxed)

    for i in boxed:
        img_path = os.path.join("static", i.img)  # Assuming the images are stored in the static folder
        dir_name = os.path.dirname(img_path)
        if dir_name == source:
            boxes.append(i)

    return render(request, 'new_balance.html', {'boxes': boxes})

def vans(request):

    boxes = []
    source = "static\\vans"
    boxee = MainImage.objects.all()
    boxed = list(boxee)
    random.seed(time.time())
    random.shuffle(boxed)

    for i in boxed:
        img_path = os.path.join("static", i.img)  # Assuming the images are stored in the static folder
        dir_name = os.path.dirname(img_path)
        if dir_name == source:
            boxes.append(i)

    return render(request, 'vans.html', {'boxes': boxes})

def reebok(request):

    boxes = []
    source = "static\\reebok"
    boxee = MainImage.objects.all()
    boxed = list(boxee)
    random.seed(time.time())
    random.shuffle(boxed)

    for i in boxed:
        img_path = os.path.join("static", i.img)  # Assuming the images are stored in the static folder
        dir_name = os.path.dirname(img_path)
        if dir_name == source:
            boxes.append(i)

    return render(request, 'reebok.html', {'boxes': boxes})

def balenciaga(request):

    boxes = []
    source = "static\\balenciaga"
    boxee = MainImage.objects.all()
    boxed = list(boxee)
    random.seed(time.time())
    random.shuffle(boxed)

    for i in boxed:
        img_path = os.path.join("static", i.img)  # Assuming the images are stored in the static folder
        dir_name = os.path.dirname(img_path)
        if dir_name == source:
            boxes.append(i)

    return render(request, 'balenciaga.html', {'boxes': boxes})

#this function handles the registration
def register(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            username = request.POST['username']
            email = request.POST['email']
            number = request.POST['user_number']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            # Check if passwords match
            if password1 != password2:
                messages.error(request, 'Passwords do not match. Please try again.')
                return redirect('register')

            # Check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')

            # Check if email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('register')

            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, 'You are now registered and can log in')
            return redirect('login')

    else:
        return render(request, 'register.html')

#this function handles the login request   
def login(request):

    if 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            # Authenticate login credentials
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('register')
    else:
        return render(request, 'login.html') # Render the login page

#this function handles the search request
def logout(request):
    auth.logout(request)
    return redirect('/')

def search(request):
    query = request.GET.get('query')
    if query:
        products = MainImage.objects.filter(name__icontains=query) | MainImage.objects.filter(price__icontains=query)
    else:
        products = MainImage.objects.all()
    context = {
        'products': products,
        'query' : query
    }
    return render(request, 'search.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(MainImage, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

#this handles the cart page
def cart(request):
    user = request.user
    items = Cart.objects.filter(user=user)
    context = {'items': items}
    return render(request, 'cart.html', context)

# #this handles the additon of products to cart
# @login_required
# def add_to_cart(request, product_id):
#     user = request.user
#     product = get_object_or_404(MainImage, id=product_id)
#     quantity = int(request.POST['quantity'])
#     size = int(request.POST['size'])
#     color = str(request.POST['color'])
#     item = Cart.objects.filter(product=product, user=user)
#     if item.exists():
#         item = item.first()
#         item.quantity += quantity
#         item.save()
#     else:
#         new_item = Cart.objects.create(product=product, user=user, quantity=quantity, size=size, color=color)
#         new_item.save()
#     return redirect('cart')

# @login_required
# def add_to_cart(request, product_id):
#     user = request.user
#     product = get_object_or_404(MainImage, id=product_id)
#     quantity = int(request.POST['quantity'])
#     size_id = int(request.POST['size'])
#     size = get_object_or_404(ShoeSize, id=size_id)
#     color = request.POST['color']
#     item = Cart.objects.filter(product=product, user=user)
#     if item.exists():
#         item = item.first()
#         item.quantity += quantity
#         item.save()
#     else:
#         new_item = Cart.objects.create(product=product, user=user, quantity=quantity, size=size, color=color)
#         new_item.save()
#     return redirect('cart')

@login_required
def add_to_cart(request, product_id):
    user = request.user
    product = get_object_or_404(MainImage, id=product_id)
    quantity = int(request.POST['quantity'])
    size_id = int(request.POST['size'])
    size = get_object_or_404(ShoeSize, id=size_id)
    color_id = int(request.POST['color'])
    color = get_object_or_404(ShoeColor, id=color_id)
    item = Cart.objects.filter(product=product, user=user)
    if item.exists():
        item = item.first()
        item.quantity += quantity
        item.save()
    else:
        new_item = Cart.objects.create(product=product, user=user, quantity=quantity, size=size, color=color)
        new_item.save()
    return redirect('cart')


#this handles the removal of products from cart 
def remove_from_cart(request, product_id):
    item = Cart.objects.get(id=product_id)
    item.delete()
    return redirect('cart')

#this handles the removal of all products from cart 
def empty_cart(request):
    item = Cart.objects.all()
    item.delete()
    return redirect('cart')

#this function updates the cart
def update_cart(request, product_id):
    cart = Cart(request)
    product = MainImage.objects.get(id=product_id)
    quantity = int(request.POST.get('quantity'))
    cart.update(product=product, quantity=quantity)
    messages.success(request, f"{product.name} has been updated in your cart.")
    return redirect('cart')