from django.contrib import admin
from .models import Contact, RequestLog, RequestCounter


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'lastname', 'email', 'jabber', 'skype', 'date_of_birth')


class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('full_path', 'request_method', 'http_referer')


class RequestCounterAdmin(admin.ModelAdmin):
    list_display = ('id', 'value',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(RequestLog, RequestLogAdmin)
admin.site.register(RequestCounter, RequestCounterAdmin)
