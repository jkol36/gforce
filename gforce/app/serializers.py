from rest_framework.serializers import ModelSerializer
from .models import ImpactEvent, TimeStamp
from rest_framework.response import Response
from gforce.app.management.commands.GyroData import GyroDataNamespace
from logging import Logger
from .push import Setup
import json

pusher = Setup()

class TimeStampSerializer(ModelSerializer):
	class Meta:
		model = TimeStamp


class ImpactEventSerializer(ModelSerializer):
	#TimeStamp = TimeStampSerializer(required=False)
	class Meta:
		model = ImpactEvent
		depth = 1
	
	def create(self, validated_data):

		print "called"
		try:
			new_event_object = self.context['request']._full_data['GFConnect']
		except Exception, e:
			print "error"
			print e
			new_event_object = None
		if new_event_object:
			print "new event object"
			Json = json.loads(new_event_object)
			ax =  Json['ax']
			az = Json['az']
			ay = Json["ay"]
			gx = Json['gx']
			gy = Json['gy']
			gz = Json['gz']
			TimeStamp = Json['TimeStamp']
			data = {
			"ax": ax, 
			"ay": ay, 
			"az": az,
			"TimeStamp": TimeStamp,
			"gx": gx, 
			"gz": gz,
			"gy": gy
			}
			pusher.trigger("impactData", "new_data", {"message":data})
		else:
			print "else"
			ax = validated_data.pop('ax')
			ay = validated_data.pop('ay')
			az = validated_data.pop('az')
			gx= validated_data.pop('gx')
			gy = validated_data.pop('gy')
			gz= validated_data.pop('gz')
			data = {"ax":ax, 
				"ay": ay, "az":az, "gx":gx, "gy": gy, "gz": gz}
			try:
				pusher.trigger("impactData", "new_data", {"message": data})
			except Exception, e:
				print "failed to trigger"
				print e
			print "triggered"
		impact_event = ImpactEvent.objects.create(ax=ax, ay=ay, az=az, gx=gx, gy=gy, gz=gz)
		impact_event.save()
		return Response('ok')
