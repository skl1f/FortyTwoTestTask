import apps.hello.utils as utils
from django.shortcuts import render
from .models import Contact, RequestCounter, RequestLog


def home(request):
    contact = Contact.objects.get(show=True)
    counter = RequestCounter.objects.get(id=1).value
    content = {'contact': contact,
               'counter': counter}
    utils.write_logline(request, content)
    return render(request, 'index.html', content,
                  content_type="text/html")


def requests(request):
    contact = Contact.objects.get(show=True)
    content = {'contact': contact}
    utils.write_logline(request, content)
    return render(request, 'requests.html', content,
                  content_type="text/html")


def api_requests(request):
    contact = Contact.objects.get(show=True)
    logs = list(RequestLog.objects.order_by('-id')[:10])
    content = {'contact': contact,
               'logs': logs}
    utils.write_logline(request, content)
    return render(request, 'api_requests.json', content,
                  content_type="application/json")
