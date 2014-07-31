# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Point'
        db.create_table(u'paintr_point', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'paintr', ['Point'])


    def backwards(self, orm):
        # Deleting model 'Point'
        db.delete_table(u'paintr_point')


    models = {
        u'paintr.canvas': {
            'Meta': {'object_name': 'Canvas'},
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'})
        },
        u'paintr.point': {
            'Meta': {'object_name': 'Point'},
            'creation_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['paintr']