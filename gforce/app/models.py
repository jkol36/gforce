from django.db import models
from gforce.profiles.models import Profile

# Create your models here.


class ImpactEvent(models.Model):
	ax = models.FloatField(null=True, blank=True)
	ay = models.FloatField(null=True, blank=True)
	az = models.FloatField(null=True, blank=True)
	gx = models.FloatField(null=True, blank=True)
	gy = models.FloatField(null=True, blank=True)
	gz = models.FloatField(null=True, blank=True)
	timestamp = models.ForeignKey('TimeStamp', null=True, blank=True)


class TimeStamp(models.Model):
	time_counter = models.IntegerField(null=True)
	time_accessed = models.DateTimeField(null=True, blank=True)


class MouthGuard(models.Model):
	mac_address = models.GenericIPAddressField(protocol="both")
	profile = models.ForeignKey(Profile, null=True, blank=True)
