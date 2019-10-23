from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

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





def home_page(request):
    return render(request, 'first_app/home_page.html')

def loose_curl_page(request):
    return render(request, 'first_app/loose_curl_page.html')

def kinky_curl_page(request):
    return render(request, 'first_app/kinky_curl_page.html')

def tight_curl_page(request):
    return render(request, 'first_app/tight_curl_page.html')

def about_page(request):
    return render(request, 'first_app/about_page.html')

def products_page(request):
    return render(request, 'first_app/products_page.html')

def blog_page(request):
    return render(request, 'first_app/blog_page.html')

def account_page(request):
    return render(request, 'first_app/account_page.html')

def shopping_cart_page(request):
    return render (request, 'first_app/shopping_cart_page.html')
