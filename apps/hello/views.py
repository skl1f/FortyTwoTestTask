from django.shortcuts import render
from .models import Contact


def home(request):
    contact = Contact.objects.get(id=1)
    return render(request, 'index.html', {'contact': contact},
                  content_type="text/html")
