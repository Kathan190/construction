from django.shortcuts import render, HttpResponse
from Home.models import Contact
from Home.models import Information
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, "Your message has been sent succesfully")
        
    return render(request, 'index.html')

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "services.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        information = Information(name=name, email=email, phone=phone, message=message)
        information.save()
    return render(request, 'contact.html')

def project(request):
    return render(request, 'projects.html')