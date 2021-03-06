# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TestResult'
        db.create_table(u'onlinejudge_testresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('submission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onlinejudge.Submission'])),
            ('test_case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onlinejudge.TestCase'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='PD', max_length=2)),
            ('memory', self.gf('django.db.models.fields.IntegerField')()),
            ('cputime', self.gf('django.db.models.fields.IntegerField')()),
            ('result', self.gf('django.db.models.fields.CharField')(default='PD', max_length=2)),
        ))
        db.send_create_signal(u'onlinejudge', ['TestResult'])

        # Deleting field 'Submission.result'
        db.delete_column(u'onlinejudge_submission', 'result')

        # Adding field 'Submission.status'
        db.add_column(u'onlinejudge_submission', 'status',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Challenge.submission_template'
        db.add_column(u'onlinejudge_challenge', 'submission_template',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'TestResult'
        db.delete_table(u'onlinejudge_testresult')


        # User chose to not deal with backwards NULL issues for 'Submission.result'
        raise RuntimeError("Cannot reverse this migration. 'Submission.result' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Submission.result'
        db.add_column(u'onlinejudge_submission', 'result',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)

        # Deleting field 'Submission.status'
        db.delete_column(u'onlinejudge_submission', 'status')

        # Deleting field 'Challenge.submission_template'
        db.delete_column(u'onlinejudge_challenge', 'submission_template')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'onlinejudge.challenge': {
            'Meta': {'object_name': 'Challenge'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'problem': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'submission_template': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'onlinejudge.submission': {
            'Meta': {'unique_together': "(('author', 'challenge'),)", 'object_name': 'Submission'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'challenge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onlinejudge.Challenge']"}),
            'code': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'test_results': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['onlinejudge.TestCase']", 'through': u"orm['onlinejudge.TestResult']", 'symmetrical': 'False'})
        },
        u'onlinejudge.testcase': {
            'Meta': {'object_name': 'TestCase'},
            'challenge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onlinejudge.Challenge']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'input': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'output': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'onlinejudge.testresult': {
            'Meta': {'object_name': 'TestResult'},
            'cputime': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memory': ('django.db.models.fields.IntegerField', [], {}),
            'result': ('django.db.models.fields.CharField', [], {'default': "'PD'", 'max_length': '2'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'PD'", 'max_length': '2'}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onlinejudge.Submission']"}),
            'test_case': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onlinejudge.TestCase']"})
        }
    }

    complete_apps = ['onlinejudge']