from django.db import models
from gforce.players.models import Player

# Create your models here.

class Team(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	players = models.ForeignKey(Player, blank=True, null=True)

