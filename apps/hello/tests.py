# encoding: utf-8
from __future__ import unicode_literals
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
        contact.id = 2
        contact.date_of_birth = datetime.date(1991, 4, 1)
        contact.skype = 'Тест'
        contact.jabber = 'test@jabber.me'
        contact.email = 'test@example.com'
        contact.name = 'Иван'
        contact.lastname = 'Иванович'
        contact.bio = 'Тестовий персонаж'
        contact.other_contact = u'https://github.com/test'
        contact.save()
        contact_from_db = Contact.objects.get(id=2)
        assert(contact_from_db.date_of_birth == datetime.date(1991, 4, 1))
        assert(contact_from_db.skype == 'Тест')
        assert(contact_from_db.jabber == 'test@jabber.me')
        assert(contact_from_db.email == 'test@example.com')
        assert(contact_from_db.name == 'Иван')
        assert(contact_from_db.lastname == 'Иванович')
        assert(contact_from_db.bio == 'Тестовий персонаж')
        assert(contact_from_db.other_contact == 'https://github.com/test')

    def test_contact_info(self):
        """Check that status_code is 200 and information in db"""

        ContactTest.test_add_contacts(self)
        contact = Contact.objects.get(id=1)
        assert(contact.date_of_birth == datetime.date(1991, 4, 1))
        assert(contact.skype == 'sklifeg')
        assert(contact.jabber == 'skl1f@jabber.me')
        assert(contact.email == 'skl1f@ukrgadget.com')
        assert(contact.name == 'Oleksii')
        assert(contact.lastname == 'Miroshnychenko')
        assert(contact.bio == 'Python Dev')
        assert(contact.other_contact == 'https://github.com/skl1f')

    def test_contacts_returned(self):
        """test that only one contact returned"""

        C = Contact.objects.get(id=1)
        assert(isinstance(C, Contact))


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

    """Check that logline have all expected data"""

    def test_log_contact(self):
        """check logging data from Contact model"""

        excepted_string = ('Name: Oleksii, Lastname: Miroshnychenko,'
                           ' Date of birth: 1991-04-01,'
                           'Email: skl1f@ukrgadget.com,'
                           ' Jabber: skl1f@jabber.me, '
                           'Skype: sklifeg, Bio: Python Dev,'
                           'Other contact: https://github.com/skl1f')
        received_string = str(Contact.objects.get(id=1))
        assert(excepted_string == received_string)

    def test_log_requestlog(self):
        """check logging data from RequestLog model"""

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
        """check logging data from RequestCounter model"""

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
