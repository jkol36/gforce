from django.db import models

# Create your models here.

class Player(models.Model):
	height = models.FloatField(null=True, blank=True)
	weight = models.FloatField(null=True, blank=True)
	

