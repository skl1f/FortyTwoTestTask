from django.shortcuts import render
from django.conf import settings
from .utils import logger
from .models import Contact, RequestCounter, RequestLog


def home(request):
    contact = Contact.objects.get(show=True)
    counter = RequestCounter.objects.get(id=1).value
    content = {'contact': contact,
               'counter': counter}
    if settings.DEBUG is True:
        logger.debug(str(content))
    return render(request, 'index.html', content,
                  content_type="text/html")


def requests(request):
    contact = Contact.objects.get(show=True)
    content = {'contact': contact}
    if settings.DEBUG is True:
        logger.debug(str(content))
    return render(request, 'requests.html', content,
                  content_type="text/html")


def api_requests(request):
    contact = Contact.objects.get(show=True)
    logs = list(RequestLog.objects.order_by('-id')[:10])
    content = {'contact': contact,
               'logs': logs}
    if settings.DEBUG is True:
        logger.debug(str(content))
    return render(request, 'api_requests.json', content,
                  content_type="application/json")


def api_contacts(request):
    contact = Contact.objects.get(show=True)
    content = {'contact': contact}
    if settings.DEBUG is True:
        logger.debug(str(content))
    return render(request, 'api_contacts.json', content,
                  content_type="application/json")


def edit_contacts(request):
    return render(request, 'edit_contacts.html', {},
                  content_type="text/html")
