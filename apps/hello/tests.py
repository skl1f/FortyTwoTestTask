# encoding: utf-8
from __future__ import unicode_literals
from datetime import date
from django.test import TestCase
from .models import Contact, RequestLog, RequestCounter
from django.contrib.auth.models import User
from django.test.client import Client


class ContactTest(TestCase):

    """Tests for Contact Model"""

    def setUp(self):
        """Add new contact to database"""

        self.client = Client()
        self.contact = Contact.objects.create_contact(
            'Иван',
            'Иванович',
            'Тест',
            'test@jabber.me',
            'test@example.com',
            date(1991, 4, 1),
            'Тестовий персонаж',
            'https://github.com/test',)

    def test_contact_on_index(self):
        """Get main page and check contact information"""

        main = self.client.get("/")
        contact = Contact.objects.get(id=1)
        assert(contact.name in main.content)
        assert(contact.lastname in main.content)
        assert(contact.skype in main.content)
        assert(contact.jabber in main.content)
        assert(contact.bio in main.content)
        assert(contact.other_contact in main.content)
        assert(contact.date_of_birth.strftime("%B %-d, %Y") in main.content)


class AdminTest(TestCase):

    """Check admin login"""

    def setUp(self):
        self.client = Client()

    def test_login(self):
        """Check admin default login and password"""

        admin = User.objects.get(id=1)
        assert(admin)
        login = self.client.login(username='admin', password='admin')
        assert(login)


class RequestLogTest(TestCase):

    """Check RequestLog in database after request"""

    def setUp(self):
        self.client = Client()

    def test_request(self):
        """Hit unexists url and check it in DB RequestLog"""

        self.client.get('/missing_url')
        try:
            RequestLog.objects.get(full_path='/missing_url')
        except:
            assert(False)


class LogLineTest(TestCase):

    """Check that logline have all expected data"""

    def setUp(self):
        self.client = Client()

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

        self.client.get('/RequestLogTest')
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

        self.client.get('/RequestLogTest')
        value = RequestCounter.objects.get(id=1)
        assert(str(value) == 'Number of requests 1')


class PagesTests(TestCase):

    """Connect to all pages and check status_code """

    def setUp(self):
        self.client = Client()
        self.URLS = ['/',
                     '/edit/',
                     '/admin/',
                     '/requests/',
                     '/api/requests/']

    def test_pages(self):
        """ basic test """
        for url in self.URLS:
            page = self.client.get(url)
            assert(page.status_code == 200)
