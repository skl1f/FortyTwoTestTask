# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Contact.image'
        db.add_column(u'hello_contact', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contact.image_height'
        db.add_column(u'hello_contact', 'image_height',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default='200', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contact.image_width'
        db.add_column(u'hello_contact', 'image_width',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default='200', null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Contact.image'
        db.delete_column(u'hello_contact', 'image')

        # Deleting field 'Contact.image_height'
        db.delete_column(u'hello_contact', 'image_height')

        # Deleting field 'Contact.image_width'
        db.delete_column(u'hello_contact', 'image_width')


    models = {
        u'hello.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_height': ('django.db.models.fields.PositiveIntegerField', [], {'default': "'200'", 'null': 'True', 'blank': 'True'}),
            'image_width': ('django.db.models.fields.PositiveIntegerField', [], {'default': "'200'", 'null': 'True', 'blank': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'other_contact': ('django.db.models.fields.TextField', [], {}),
            'show': ('django.db.models.fields.BooleanField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'hello.requestcounter': {
            'Meta': {'object_name': 'RequestCounter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'hello.requestlog': {
            'Meta': {'object_name': 'RequestLog'},
            'full_path': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'http_accept_language': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'http_referer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'http_user_agent': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_addr': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'request_method': ('django.db.models.fields.CharField', [], {'max_length': '7'})
        }
    }

    complete_apps = ['hello']