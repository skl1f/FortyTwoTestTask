from django.test import TestCase
from .models import Contact
from django.contrib.auth.models import User
from django.test.client import Client


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

    def runTest(self):
        self.check_contact_info()


class CheckAdmin(TestCase):

    def create_admin(self):
        ""
        try:
            admin = User.objects.get(id=1)
        except:
            User.objects.create_superuser(
                u'admin', u'admin@example.com', u'admin')

        admin = self.check_login()
        assert(admin)

    def check_login(self):
        "Check admin default login and password"

        c = Client()
        login = c.login(username='admin', password='admin')
        return login

    def runTest(self):
        self.create_admin()
