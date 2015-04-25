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
    show = models.BooleanField()

    def __str__(self):
        return 'Name: {0}, Lastname: {1}, Date of birth: {2}, \
                Email: {3}, Jabber: {4}, Skype: {5}, Bio: {6}, \
                Other contact: {7}'.format(self.name,
                                           self.lastname,
                                           self.date_of_birth,
                                           self.email,
                                           self.jabber,
                                           self.skype,
                                           self.bio,
                                           self.other_contact)

    def save(self, *args, **kwargs):
        if self.show:
            try:
                temp = Contact.objects.get(show=True)
                if self != temp:
                    temp.show = False
                    temp.save()
            except Contact.DoesNotExist:
                pass
        super(Contact, self).save(*args, **kwargs)


class RequestLog(models.Model):

    """This object contain iformation about HttpRequest"""

    full_path = models.CharField(max_length=200)
    request_method = models.CharField(max_length=7)
    remote_addr = models.GenericIPAddressField()
    http_user_agent = models.CharField(max_length=200)
    http_referer = models.CharField(max_length=200)
    http_accept_language = models.CharField(max_length=100)

    def __str__(self):
        return 'Full path: {0}, Request method: {1}, Remore addr: {2}, \
                http user agent: {3}, http referer: {4}, \
                http accept language: {5}'.format(self.full_path,
                                                  self.request_method,
                                                  self.remote_addr,
                                                  self.http_user_agent,
                                                  self.http_referer,
                                                  self.http_accept_language)

    def save(self, arg):
        self.full_path = arg['FULL_PATH']
        self.request_method = arg['REQUEST_METHOD']
        self.remote_addr = arg['REMOTE_ADDR']
        self.http_user_agent = arg['HTTP_USER_AGENT']
        self.http_referer = arg['HTTP_REFERER']
        self.http_accept_language = arg['HTTP_ACCEPT_LANGUAGE']
        super(RequestLog, self).save(arg)


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
