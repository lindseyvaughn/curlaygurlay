from django.shortcuts import render, HttpResponse


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

