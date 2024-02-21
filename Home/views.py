from django.shortcuts import render, HttpResponse
from Home.models import Contact
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        send_mail(
            'Contact Form',
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        
    return render(request, 'index.html')

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "services.html")