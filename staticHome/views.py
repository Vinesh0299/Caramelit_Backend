from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'staticHome/index.html')

def aboutus(request):
    return render(request, 'staticHome/aboutus.html')

def contactform(request):
    return render(request, 'staticHome/contactform.html')

def consortium(request):
    return render(request, 'staticHome/consortium.html')

def academy(request):
    return render(request, 'staticHome/academy.html')

def products(request):
    return render(request, 'staticHome/products.html')