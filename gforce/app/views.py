from django.shortcuts import render
from django.http import HttpResponse
from .models import ImpactEvent, TimeStamp
from gforce.players.models import Player
from gforce.players.serializers import PlayerSerializer
from gforce.teams.models import Team
from gforce.teams.serializers import TeamSerializer
from rest_framework.decorators import list_route
from rest_framework.viewsets import ModelViewSet
from .serializers import ImpactEventSerializer, TimeStampSerializer
from pusher import Pusher


# Create your views here.

class ImpactEventViewSet(ModelViewSet):
	queryset = ImpactEvent.objects.all()
	serializer_class = ImpactEventSerializer

	
		
		












class PlayerViewSet(ModelViewSet):
	queryset = Player.objects.all()
	serializer_class = PlayerSerializer

class TeamSerializer(ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer
	
def app(request):
	return render(request, 'app.html')


def socketio_view(request):
	print "called"
	p = Pusher(
	  app_id='135314',
	  key='92e6deea4ee5542dc495',
	  secret='712204ca7293ef75bd11',
	  ssl=True,
	  port=443
	)
	p.trigger('test_channel', 'my_event', {'message': 'hello world'})
	

