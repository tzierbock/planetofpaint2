# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Point.canvas'
        db.add_column(u'paintr_point', 'canvas',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['paintr.Canvas']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Point.canvas'
        db.delete_column(u'paintr_point', 'canvas_id')


    models = {
        u'paintr.canvas': {
            'Meta': {'object_name': 'Canvas'},
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'})
        },
        u'paintr.point': {
            'Meta': {'object_name': 'Point'},
            'canvas': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['paintr.Canvas']"}),
            'creation_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['paintr']