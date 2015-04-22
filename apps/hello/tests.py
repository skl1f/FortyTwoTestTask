from django.test import TestCase
from .models import Contact


class SomeTests(TestCase):
    def test_math(self):
        "Check if information is correct"
        contact = Contact.objects.get(id=1)
        assert(contact.name == u'Oleksii')
        assert(contact.lastname == u'Miroshnychenko')
        assert(contact.bio == u'Python Dev')
        assert(contact.other_contact == u'https://github.com/skl1f')
