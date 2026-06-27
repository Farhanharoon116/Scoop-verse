from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
def home(request):
    return render(request, 'scoop_app/home.html')

def products(request):
    return render(request, 'scoop_app/products.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create a new Contact object and save it to the database
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return render(request, 'scoop_app/contact.html', {'sent': True, 'name': name})

    return render(request, 'scoop_app/contact.html')

def about(request):
    return render(request, 'scoop_app/about.html')
