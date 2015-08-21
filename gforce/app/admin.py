from django.contrib import admin
from gforce.app.models import ImpactEvent, TimeStamp
from gforce.profiles.models import Profile
from gforce.teams.models import Team
from gforce.players.models import Player

# Register your models here.
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Profile)
admin.site.register(ImpactEvent)
admin.site.register(TimeStamp)
