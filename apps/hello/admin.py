from django.contrib import admin
from .models import Contact, RequestLog


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'lastname', 'email', 'jabber', 'skype', 'date_of_birth')


class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('full_path', 'request_method', 'http_referer')

admin.site.register(Contact, ContactAdmin)
admin.site.register(RequestLog, RequestLogAdmin)
