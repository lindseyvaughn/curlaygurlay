from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

from django.core.paginator import Paginator


def login_register_page(request):
    return render (request, 'first_app/login_register_page.html')

def register_user(request):
    if request.method == "POST":
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/curlaygurlay/login_register")
        
        else:
            password = request.POST["password"]
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            
            user = User.objects.create(
                first_name = request.POST["first_name"], 
                last_name = request.POST["last_name"], 
                email = request.POST["email"], 
                password = pw_hash
            )

            request.session['id'] = user.id
            return redirect("/curlaygurlay")
def login_user(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/curlaygurlay/login_register")

        else:
            user = User.objects.get(email = request.POST["email"])
            request.session["id"] = user.id
            return redirect("/curlaygurlay")

def logout (request):
    request.session.clear()
    return redirect ("/curlaygurlay")


def admin (request):
    return render(request, 'first_app/admin.html')

def create_product (request):
    new_product = Product.objects.create(
        product_name = request.POST["product_name"],
        description = request.POST["description"],
        price = request.POST["price"],
        hair_type = request.POST["hair_type"],
        img_url = request.POST["img_url"]
    )
    all_products = Product.objects.all

    context = {
        "all_products" : all_products
    }
    return redirect ("/admin")


def home_page(request):
    return render(request, 'first_app/home_page.html')

def loose_curl_page(request):
    products = Product.objects.filter(hair_type="loose_curl")
    context = {
        "products" : products
    }
    return render(request, 'first_app/loose_curl_page.html', context)

def kinky_curl_page(request):
    products = Product.objects.filter(hair_type="loose_curl")
    context = {
        "products" : products
    }
    return render(request, 'first_app/kinky_curl_page.html')

def tight_curl_page(request):
    products = Product.objects.filter(hair_type="loose_curl")
    context = {
        "products" : products
    }
    return render(request, 'first_app/tight_curl_page.html')

def about_page(request):
    return render(request, 'first_app/about_page.html')

def products_page(request):
    products = Product.objects.all()
    paginator = Paginator(products, 3)

    if "page" in request.GET:
        page = request.GET.get("page")
    else:
        page = 1
    products = paginator.page(page)


    return render(request, 'first_app/products_page.html', {'products' : products})

def blog_page(request):
    return render(request, 'first_app/blog_page.html')

def account_page(request):
    return render(request, 'first_app/account_page.html')

def shopping_cart_page(request):
    return render (request, 'first_app/shopping_cart_page.html')

def addToCart(request, product_id):
    if 'cart' not in request.session:
        cartObj ={
            # 'userid' : request.session['user_id'],
            'cart_items': []
        }
        request.session['cart'] = cartObj
    else :
        prod  = Product.objects.get(id= product_id)
        cartObj = request.session['cart']
        cartObj['cart_items'].append(prod)
        print(cartObj['cart_items'])
        # request.session['cart'] = cartObj
        request.session['cart'] = "New cart"

    print(request.session['cart'])

    return redirect("/curlaygurlay/loose_curl")
