from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    email = models.CharField(max_length=75)
    jabber = models.CharField(max_length=75)
    skype = models.CharField(max_length=200)
    bio = models.TextField()
    other_contact = models.TextField()
