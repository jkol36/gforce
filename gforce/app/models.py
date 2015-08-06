from django.db import models

# Create your models here.


class ImpactEvent(models.Model):
	ax = models.IntegerField(null=True, blank=True)
	ay = models.IntegerField(null=True, blank=True)
	az = models.IntegerField(null=True, blank=True)
	gx = models.IntegerField(null=True, blank=True)
	gy = models.IntegerField(null=True, blank=True)
	gz = models.IntegerField(null=True, blank=True)
	timestamp = models.ForeignKey('TimeStamp')


class TimeStamp(models.Model):
	time_counter = models.IntegerField(null=True, blank=True)
	time_accessed = models.DateTimeField()