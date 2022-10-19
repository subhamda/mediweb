from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,"about.html")
def client(request):
    return render(request,"client.html")
def contact(request):
    return render(request,"contact.html")
def index(request):
    return render(request,"index.html")
def product(request):
    return render(request,"product.html")