from django.test import TestCase
from .models import Contact
from django.test.client import Client


class BasicTest(TestCase):

    "Check admin login and password"

    def chek_login(self):
        c = Client()
        login = c.login(username='admin', password='admin')
        assert(login)


class ContactTest(TestCase):

    def check_contact_info(self):

        "Check that status_code is 200 and information in db is correct"

        c = Client()
        page = c.get('/')
        assert(page.status_code == 200)
        contact = Contact.objects.get(id=1)
        assert(contact.name == u'Oleksii')
        assert(contact.lastname == u'Miroshnychenko')
        assert(contact.bio == u'Python Dev')
        assert(contact.other_contact == u'https://github.com/skl1f')
