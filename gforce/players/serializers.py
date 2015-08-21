from rest_framework.serializers import ModelSerializer
from .models import Player



class PlayerSerializer(ModelSerializer):
	class Meta:
		model = Player

	def create(self, request):
		team = request.data.get('team')
		height = request.data.get('height')
		weight = request.data.get('weight')
		player = Player.objects.create(team=team, height=height, weight=weight )