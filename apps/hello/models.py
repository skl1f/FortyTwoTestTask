from __future__ import unicode_literals
from django.db import models
from PIL import Image


class ContactManager(models.Manager):

    def create_contact(self, name, lastname, skype, jabber, email,
                       date_of_birth, bio, other_contact):

        contact = self.create(name=name, lastname=lastname,
                              skype=skype, jabber=jabber, email=email, bio=bio,
                              other_contact=other_contact,
                              date_of_birth=date_of_birth,)
        return contact


class Contact(models.Model):

    """This object contain contact information from main page"""

    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    email = models.CharField(max_length=75)
    jabber = models.CharField(max_length=75)
    skype = models.CharField(max_length=200)
    bio = models.TextField()
    other_contact = models.TextField()
    image = models.ImageField(
        upload_to="profiles",
        null=True,
        blank=True,
        editable=True,
        help_text="Profile Picture",
        verbose_name="Profile Picture"
    )
    image_height = models.PositiveIntegerField(
        null=True, blank=True, editable=False, default="200")
    image_width = models.PositiveIntegerField(
        null=True, blank=True, editable=False, default="200")

    objects = ContactManager()

    def save(self, *args, **kwargs):
        if not self.image:
            return super(Contact, self).save(*args, **kwargs)

        image = Image.open(self.image)
        (width, height) = image.size
        size = (200, 200)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.image.path)
        super(Contact, self).save(*args, **kwargs)

    def __unicode__(self):
        return ('Name: {0}, Lastname: {1}, Date of birth: {2},'
                'Email: {3}, Jabber: {4}, Skype: {5}, Bio: {6},'
                'Other contact: {7}').format(self.name,
                                             self.lastname,
                                             self.date_of_birth,
                                             self.email,
                                             self.jabber,
                                             self.skype,
                                             self.bio,
                                             self.other_contact)


class RequestLog(models.Model):

    """This object contain iformation about HttpRequest"""

    full_path = models.CharField(max_length=200)
    request_method = models.CharField(max_length=7)
    remote_addr = models.GenericIPAddressField()
    http_user_agent = models.CharField(max_length=200)
    http_referer = models.CharField(max_length=200)
    http_accept_language = models.CharField(max_length=100)

    def save(self, arg):
        self.full_path = arg['FULL_PATH']
        self.request_method = arg['REQUEST_METHOD']
        self.remote_addr = arg['REMOTE_ADDR']
        self.http_user_agent = arg['HTTP_USER_AGENT']
        self.http_referer = arg['HTTP_REFERER']
        self.http_accept_language = arg['HTTP_ACCEPT_LANGUAGE']
        super(RequestLog, self).save(arg)

    def __str__(self):
        return ('FULL_PATH: {0}, REQUEST_METHOD: {1}, REMOTE_ADDR: {2}, '
                'HTTP_USER_AGENT: {3}, HTTP_REFERER: {4},'
                ' HTTP_ACCEPT_LANGUAGE: {5}').format(self.full_path,
                                                     self.request_method,
                                                     self.remote_addr,
                                                     self.http_user_agent,
                                                     self.http_referer,
                                                     self.http_accept_language)


class RequestCounter(models.Model):

    """Just counter of requests"""

    value = models.IntegerField()

    def increment(self):
        self.value += 1
        self.save()

    def reset(self):
        self.value = 0
        self.save()

    def __str__(self):
        return 'Number of requests {0}'.format(self.value)
