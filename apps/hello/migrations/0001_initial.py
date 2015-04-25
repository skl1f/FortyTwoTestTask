# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'hello_contact')

        # Deleting model 'RequestLog'
        db.delete_table(u'hello_requestlog')

        # Deleting model 'RequestCounter'
        db.delete_table(u'hello_requestcounter')


    def backwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'hello_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('other_contact', self.gf('django.db.models.fields.TextField')()),
            ('show', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'hello', ['Contact'])

        # Adding model 'RequestLog'
        db.create_table(u'hello_requestlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_path', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('request_method', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('remote_addr', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('http_user_agent', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('http_referer', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('http_accept_language', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'hello', ['RequestLog'])

        # Adding model 'RequestCounter'
        db.create_table(u'hello_requestcounter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'hello', ['RequestCounter'])



    models = {
        u'hello.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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