from django.shortcuts import render, HttpResponse


def home_page(request):
    return render(request, 'first_app/home_page.html')

def loose_curl(request):
    return render(request, 'first_app/loose_curl.html')

def kinky_curl(request):
    return render(request, 'first_app/kinky_curl.html')

def tight_curl(request):
    return render(request, 'first_app/tight_curl.html')
