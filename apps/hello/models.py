from django.db import models


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


class RequestLog(models.Model):

    """This object contain iformation about HttpRequest"""

    def save(self, arg):
        self.full_path = arg['FULL_PATH']
        self.request_method = arg['REQUEST_METHOD']
        self.remote_addr = arg['REMOTE_ADDR']
        self.http_user_agent = arg['HTTP_USER_AGENT']
        self.http_referer = arg['HTTP_REFERER']
        self.http_accept_language = arg['HTTP_ACCEPT_LANGUAGE']
        super(RequestLog, self).save(arg)

    full_path = models.CharField(max_length=200)
    request_method = models.CharField(max_length=7)
    remote_addr = models.GenericIPAddressField()
    http_user_agent = models.CharField(max_length=200)
    http_referer = models.CharField(max_length=200)
    http_accept_language = models.CharField(max_length=100)


class RequestCounter(models.Model):

    """Just counter of requests"""

    value = models.IntegerField()

    def increment(self):
        self.value += 1
        self.save()

    def reset(self):
        self.value = 0
        self.save()
