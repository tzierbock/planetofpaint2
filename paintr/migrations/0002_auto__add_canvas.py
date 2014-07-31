# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Canvas'
        db.create_table(u'paintr_canvas', (
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'paintr', ['Canvas'])


    def backwards(self, orm):
        # Deleting model 'Canvas'
        db.delete_table(u'paintr_canvas')


    models = {
        u'paintr.canvas': {
            'Meta': {'object_name': 'Canvas'},
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'})
        }
    }

    complete_apps = ['paintr']