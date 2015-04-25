import datetime
from django.test import TestCase
from .models import Contact, RequestLog
from django.contrib.auth.models import User
from django.test.client import Client


class ContactTest(TestCase):

    "Check that status_code is 200 and information in db is correct"

    def test_contact_info(self):

        c = Client()
        page = c.get('/')
        assert(page.status_code == 200)
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
        "Add another contact and check it on main page"

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


class CheckAdmin(TestCase):

    def test_admin(self):
        admin = User.objects.get(id=1)
        assert(admin)

    def test_login(self):
        "Check admin default login and password"

        c = Client()
        login = c.login(username='admin', password='admin')
        return login


class RequestLogTest(TestCase):

    """Check RequestLog in database after request"""

    def test_request(self):
        c = Client()
        c.get('/missing_url')
        try:
            RequestLog.objects.get(full_path='/missing_url')
        except:
            assert(False)
