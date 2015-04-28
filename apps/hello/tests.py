import datetime
from django.test import TestCase
from .models import Contact, RequestLog, RequestCounter
from django.contrib.auth.models import User
from django.test.client import Client


class ContactTest(TestCase):

    """Tests for Contact Model"""

    def test_add_contacts(self):
        """Add another contact and check it on main page"""

        contact = Contact()
        contact.date_of_birth = datetime.date(1991, 4, 1)
        contact.skype = u'test'
        contact.jabber = u'test@jabber.me'
        contact.email = u'test@example.com'
        contact.name = u'TestName'
        contact.lastname = u'TestLastName'
        contact.bio = u'TestCase'
        contact.other_contact = u'https://github.com/test'
        contact.save()

    def test_contact_info(self):
        """Check that status_code is 200 and information in db"""

        ContactTest.test_add_contacts(self)
        contact = Contact.objects.get(id=1)
        assert(contact.date_of_birth == datetime.date(1991, 4, 1))
        assert(contact.skype == u'sklifeg')
        assert(contact.jabber == u'skl1f@jabber.me')
        assert(contact.email == u'skl1f@ukrgadget.com')
        assert(contact.name == u'Oleksii')
        assert(contact.lastname == u'Miroshnychenko')
        assert(contact.bio == u'Python Dev')
        assert(contact.other_contact == u'https://github.com/skl1f')


class AdminTest(TestCase):

    """Check admin login"""

    def test_login(self):
        """Check admin default login and password"""

        admin = User.objects.get(id=1)
        assert(admin)

        c = Client()
        login = c.login(username='admin', password='admin')
        assert(login)


class RequestLogTest(TestCase):

    """Check RequestLog in database after request"""

    def test_request(self):
        """Hit unexists url and check it in DB RequestLog"""

        c = Client()
        c.get('/missing_url')
        try:
            RequestLog.objects.get(full_path='/missing_url')
        except:
            assert(False)


class LogLineTest(TestCase):

    """Check that logline have all wxpedcted data"""

    def test_log_contact(self):
        excepted_string = ('Name: Oleksii, Lastname: Miroshnychenko,'
                           ' Date of birth: 1991-04-01,'
                           'Email: skl1f@ukrgadget.com,'
                           ' Jabber: skl1f@jabber.me, '
                           'Skype: sklifeg, Bio: Python Dev,'
                           'Other contact: https://github.com/skl1f')
        received_string = str(Contact.objects.get(id=1))
        assert(excepted_string == received_string)

    def test_log_requestlog(self):
        c = Client()
        c.get('/RequestLogTest')
        excepted_string = ('FULL_PATH: /RequestLogTest, '
                           'REQUEST_METHOD: GET, '
                           'REMOTE_ADDR: 127.0.0.1, '
                           'HTTP_USER_AGENT: , '
                           'HTTP_REFERER: , '
                           'HTTP_ACCEPT_LANGUAGE: ')
        received_string = str(
            RequestLog.objects.get(full_path='/RequestLogTest'))
        assert(excepted_string == received_string)

    def test_log_requestcounter(self):
        c = Client()
        c.get('/RequestLogTest')
        value = RequestCounter.objects.get(id=1)
        assert(str(value) == 'Number of requests 1')


class PagesTests(TestCase):

    """Connect to all pages and check status_code """

    URLS = ['/',
            '/edit/',
            '/admin/',
            '/requests/',
            '/api/requests/']
    c = Client()

    def test_pages(self):
        """ basic test """
        for url in self.URLS:
            page = self.c.get(url)
            assert(page.status_code == 200)
