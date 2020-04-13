from django.shortcuts import render

# Static Home pages
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

# Industries related pages
def automotive(request):
    return render(request, 'staticHome/industries/automotive.html')

def communication(request):
    return render(request, 'staticHome/industries/communication.html')

def lifescience(request):
    return render(request, 'staticHome/industries/lifescience.html')

def banking(request):
    return render(request, 'staticHome/industries/banking.html')

def consumer(request):
    return render(request, 'staticHome/industries/consumer.html')

def travel(request):
    return render(request, 'staticHome/industries/travel.html')

# Insights related pages
def artificial(request):
    return render(request, 'staticHome/insights/artificial.html')

def blockchain(request):
    return render(request, 'staticHome/insights/blockchain.html')

def iot(request):
    return render(request, 'staticHome/insights/iot.html')

def futureworkforce(request):
    return render(request, 'staticHome/insights/futureworkforce.html')

def cloudcomputing(request):
    return render(request, 'staticHome/insights/cloudcomputing.html')

def datascience(request):
    return render(request, 'staticHome/insights/datascience.html')

# Business related pages
def strategy(request):
    return render(request, 'staticHome/business/strategy.html')

def consulting(request):
    return render(request, 'staticHome/business/consulting.html')

def digital(request):
    return render(request, 'staticHome/business/digital.html')

def technology(request):
    return render(request, 'staticHome/business/technology.html')

def operations(request):
    return render(request, 'staticHome/business/operations.html')

def Application(request):
    return render(request, 'staticHome/business/Application.html')