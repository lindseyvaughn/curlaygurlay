from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

from django.core.paginator import Paginator


localCart = {
    'cart' : []
}
#################################################
#               LOGIN/REGISTRATION
#################################################
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

def logout(request):
    request.session.clear()
    return redirect ("/curlaygurlay")

#################################################
#                ACCOUNT PAGE
#################################################
def account_page(request):
    return render(request, 'first_app/account_page.html')


#################################################
#               ADMIN PAGE
#################################################
def admin (request):
    context = {
        "all_products" : Product.objects.all(), 
        "all_categories" : Category.objects.all()
    }
    return render(request, 'first_app/admin.html', context)

def create_product (request):
    new_product = Product.objects.create(
        product_name = request.POST["product_name"],
        description = request.POST["description"],
        price = request.POST["price"],
        hair_type = request.POST["hair_type"],
        img_url = request.POST["img_url"],
        product_category = Category.objects.get(id=request.POST["category"])
    )
    return redirect ("/admin")

#################################################
#               HOME PAGE
#################################################
def home_page(request):
    return render(request, 'first_app/home_page.html')

#################################################
#               BLOG PAGE
#################################################
def blog_page(request):
    return render(request, 'first_app/blog_page.html')

#################################################
#               ABOUT PAGE
#################################################
def about_page(request):
    return render(request, 'first_app/about_page.html')


#################################################
#               HAIR TYPES
#################################################
def loose_curl_page(request):
    products = Product.objects.filter(hair_type="Loose Curl")
    for product in products:
        print(product.img_url)
    print(products, "====================")
    context = {
        "products" : products
    }
    return render(request, 'first_app/loose_curl_page.html', context)

def kinky_curl_page(request):
    products = Product.objects.filter(hair_type="Kinky Curl")
    context = {
        "products" : products
    }
    return render(request, 'first_app/kinky_curl_page.html', context)

def tight_curl_page(request):
    products = Product.objects.filter(hair_type="Tight Curl")
    context = {
        "products" : products
    }
    return render(request, 'first_app/tight_curl_page.html', context)

#################################################
#               PRODUCTS PAGE
#################################################
def products_page(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)

    if "page" in request.GET:
        page = request.GET.get("page")
    else:
        page = 1
    products = paginator.page(page)


    return render(request, 'first_app/products_page.html', {'products' : products})

#################################################
#               SHOPPING CART PAGE
#################################################
def shopping_cart_page(request):
    print(localCart['cart'])
    context = {
        'prods' : localCart['cart']
    }
    return render (request, 'first_app/shopping_cart_page.html', context)
#################################################
#               ADD TO CART ROUTE
#################################################
def addToCart(request, product_id):
    if 'id' not in request.session:
        return redirect ("/curlaygurlay/login_register")

    if 'cart' not in request.session:
        print("Creating a cart")
        # cartObj ={
        #     'userid' : request.session['id'],
        #     'cart_items': []
        # }
        # cartObj = [
        #     {'cart' : []}
        # ]
        request.session['cart'] = []
    else :
        print("In adding to cart route")
        prod  = Product.objects.get(id= product_id)
        print(prod.product_name)
        print('*'*80)
        # cart = request.session['cart'][0]
        # print("Cart: ", cart)
        # cart['cart'].append(prod)
        # print("Updated_Cart: ", cart)

        # this gives non serializable error
        # request.session['cart'] = cart
        # print('*'*80)

        request.session['cart'].append(prod)
        print()
        print(request.session['cart'])
        # localCart['cart'].append(prod)
        # print(localCart)
    # print(request.session['cart'])

    return redirect("/curlaygurlay/loose_curl")

#################################################
#               Checkout Page
#################################################
def checkout_page(request):
    return render (request, 'first_app/checkout_page.html')

#################################################
#               Paypal Page
#################################################
def paypal_page(request):
    return render (request, 'first_app/paypal_page.html')

def signin(request):
    return render ( request, 'first_app/sign_in.html')

