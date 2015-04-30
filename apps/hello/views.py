import logging
import json
from django.http import HttpResponse, HttpResponseServerError, \
    HttpResponseBadRequest
from django.shortcuts import render
from datetime import datetime
from django.views.decorators.csrf import csrf_protect
from .forms import ContactForm
from .models import Contact, RequestLog

logger = logging.getLogger('apps.hello.views')


def home(request):
    contact = Contact.objects.get(id=1)
    content = {'contact': contact}
    logger.debug(content)
    return render(request, 'index.html', content,
                  content_type="text/html")


def requests(request):
    contact = Contact.objects.get(id=1)
    content = {'contact': contact}
    logger.debug(content)
    return render(request, 'requests.html', content,
                  content_type="text/html")


def api_requests(request):
    contact = Contact.objects.get(id=1)
    logs = list(RequestLog.objects.order_by('-id')[:10])
    content = {'contact': contact,
               'logs': logs}
    logger.debug(content)
    return render(request, 'api_requests.json', content,
                  content_type="application/json")


@csrf_protect
def edit_contacts(request):
    contact = Contact.objects.get(id=1)
    if request.method == 'GET':
        form = ContactForm()
        contact.date_of_birth = contact.date_of_birth.strftime("%d/%m/%Y")
        content = {'form': form,
                   'contact': contact}
        logger.debug(content)
        return render(request, 'edit_form.html', content,
                      content_type="text/html")
    elif request.method == 'POST' and request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            contact.name = request.POST.getlist("name")[0]
            contact.lastname = request.POST.getlist("lastname")[0]
            contact.date_of_birth = datetime.strptime(
                request.POST.getlist("date_of_birth")[0], '%d/%m/%Y')
            contact.email = request.POST.getlist("email")[0]
            contact.jabber = request.POST.getlist("jabber")[0]
            contact.skype = request.POST.getlist("skype")[0]
            contact.bio = request.POST.getlist("bio")[0]
            contact.other_contact = request.POST.getlist("other_contact")[0]
            contact.save()
            return HttpResponse('{"response": "OK"}')
        else:
            errors = form.errors
            return HttpResponseServerError(json.dumps(errors),
                                           content_type='application/json')
    else:
        return HttpResponseBadRequest("Bad request")
