import datetime
from django.test import TestCase
from .models import Contact, RequestLog
from django.contrib.auth.models import User
from django.test.client import Client


class ContactTest(TestCase):

    """Tests for Contact Model"""

    def test_contact_info(self):
        """Check that status_code is 200 and information in db is correct"""

        contact = Contact.objects.get(show=True)
        assert(contact.date_of_birth == datetime.date(1991, 4, 1))
        assert(contact.skype == u'sklifeg')
        assert(contact.jabber == u'skl1f@jabber.me')
        assert(contact.email == u'skl1f@ukrgadget.com')
        assert(contact.name == u'Oleksii')
        assert(contact.lastname == u'Miroshnychenko')
        assert(contact.bio == u'Python Dev')
        assert(contact.other_contact == u'https://github.com/skl1f')
        assert(contact.show is True)

    def test_many_contacts(TestCase):
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
        contact.show = True
        contact.save()
        contact_on_index = Contact.objects.get(show=True)
        assert(contact_on_index.date_of_birth == contact.date_of_birth)
        assert(contact_on_index.skype == contact.skype)
        assert(contact_on_index.jabber == contact.jabber)
        assert(contact_on_index.email == contact.email)
        assert(contact_on_index.name == contact.name)
        assert(contact_on_index.lastname == contact.lastname)
        assert(contact_on_index.bio == contact.bio)
        assert(contact_on_index.other_contact == contact.other_contact)
        assert(contact_on_index.show == contact.show)


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


class PagesTests(TestCase):

    """Connect to all pages and check status_code """

    URLS = ['/',
            '/edit/',
            '/requests/',
            '/api/requests/',
            '/api/contacts/']
    c = Client()

    def test_pages(self):
        """ basic test """
        for url in self.URLS:
            page = self.c.get(url)
            assert(page.status_code == 200)
