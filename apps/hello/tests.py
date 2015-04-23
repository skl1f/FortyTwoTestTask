from django.test import TestCase
from .models import Contact, RequestLog
from django.contrib.auth.models import User
from django.test.client import Client


class ContactTest(TestCase):

    "Check that status_code is 200 and information in db is correct"

    def check_contact_info(self):

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

    def check_if_exists_admin(self):
        admin = User.objects.get(id=1)
        assert(admin)

    def check_login(self):
        "Check admin default login and password"

        c = Client()
        login = c.login(username='admin', password='admin')
        return login

    def runTest(self):
        self.check_if_exists_admin()
        self.check_login()


class RequestLogTest(TestCase):

    """Check RequestLog in database after request"""

    def made_request(self):
        c = Client()
        c.get('/missing_url')
        try:
            RequestLog.objects.get(full_path='/missing_url')
        except:
            assert(False)

    def runTest(self):
        self.made_request()
