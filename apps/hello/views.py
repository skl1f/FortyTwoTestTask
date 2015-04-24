from django.shortcuts import render
from .models import Contact, RequestCounter, RequestLog


def home(request):
    contact = Contact.objects.get(id=1)
    counter = RequestCounter.objects.get(id=1).value
    return render(request, 'index.html', {'contact': contact,
                                          'counter': counter},
                  content_type="text/html")


def requests(request):
    contact = Contact.objects.get(id=1)
    return render(request, 'requests.html', {'contact': contact},
                  content_type="text/html")


def api_requests(request):
    contact = Contact.objects.get(id=1)
    logs = list(RequestLog.objects.order_by('-id')[:10])
    return render(request, 'api_requests.html', {'contact': contact,
                                                 'logs': logs},
                  content_type="text/html")
