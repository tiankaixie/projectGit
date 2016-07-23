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
	rangeFrom = models.CharField(max_length = 20)
	rangeTo = models.CharField(max_length = 20)
	region = models.CharField(max_length = 25)
	belongTo = models.ForeignKey(History,related_name= 'periods')
	featurePicture = models.ImageField(upload_to='%Y%m%d',max_length = 150,default = '#')
	def __unicode__(self):
		return self.name

class Event(models.Model):
	"""docstring for Event"""
	name = models.CharField(max_length = 50)
	description = RichTextField()
	year = models.CharField(max_length = 20)
	location = models.CharField(max_length = 25)
	belongTo = models.ForeignKey(HistoryPeriod,related_name = 'events')
	def __unicode__(self):
		return self.name + "-----"+ self.year + "-----"+ self.location
