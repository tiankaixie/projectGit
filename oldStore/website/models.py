from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class History(models.Model):
	"""docstring for History"""
	name = models.CharField(max_length = 20)
	summary = models.TextField()
	description = models.TextField()
	featurePicture = models.ImageField(upload_to='%Y%m%d',default = '#')
	def __unicode__(self):
		return self.name

class HistoryPeriod(models.Model):
	"""docstring for HistoryPeriod"""
	name = models.CharField(max_length = 20)
	summary = models.TextField(default='#')
	description = RichTextField()
	rangeFrom = models.IntegerField()
	rangeTo = models.IntegerField()
	region = models.CharField(max_length = 25)
	belongTo = models.ForeignKey(History,related_name= 'periods')
	featurePicture = models.ImageField(upload_to='%Y%m%d',max_length = 150,default = '#')
	def __unicode__(self):
		return self.name
