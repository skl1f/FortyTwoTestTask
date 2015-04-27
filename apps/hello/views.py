import logging
import json
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from .forms import ContactForm
from .models import Contact, RequestCounter, RequestLog

logger = logging.getLogger('apps.hello.views')


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


@csrf_protect
def edit_contacts(request):
    contact = Contact.objects.get(show=True)
    form = ContactForm()
    content = {'form': form,
               'contact': contact}
    if request.method == 'GET':
        if settings.DEBUG is True:
            logger.debug(str(content))
        return render(request, 'edit_form.html', content,
                      content_type="text/html")
    elif request.method == 'POST' and request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('{"response": "OK"}')
        else:
            errors = form.errors
            return HttpResponseServerError(json.dumps(errors),
                                           content_type='application/json')
    else:
        return HttpResponse("BAD")
