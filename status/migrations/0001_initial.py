# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Status'
        db.create_table('status_status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('msid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('accsid', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('from_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('to_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('status', ['Status'])

        # Adding model 'Subscrption'
        db.create_table('status_subscrption', (
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('is_subscribed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('status', ['Subscrption'])


    def backwards(self, orm):
        # Deleting model 'Status'
        db.delete_table('status_status')

        # Deleting model 'Subscrption'
        db.delete_table('status_subscrption')


    models = {
        'status.status': {
            'Meta': {'object_name': 'Status'},
            'accsid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'from_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'msid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'to_number': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'status.subscrption': {
            'Meta': {'object_name': 'Subscrption'},
            'is_subscribed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'})
        }
    }

    complete_apps = ['status']