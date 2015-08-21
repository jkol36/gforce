from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db import models
from django.contrib.auth.models import AbstractUser
from gforce.players.models import Player
from gforce.teams.models import Team

# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(profile=instance)

class Profile(AbstractUser):
	profile_choices = (
		('parent', 1),
		('trainer', 2),
		('coach', 3),
		('athlete', 4),
	)
	profile_type = models.CharField(choices=profile_choices, 
		blank=True, null=True, max_length=100)
	players = models.ForeignKey(Player, null=True, blank=True)
	teams = models.ForeignKey(Team, null=True, blank=True)





