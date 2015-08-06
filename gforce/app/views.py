from django.shortcuts import render
from .models import ImpactEvent, TimeStamp
from rest_framework.decorators import list_route
from rest_framework.viewsets import ModelViewSet
from .serializers import ImpactEventSerializer, TimeStampSerializer

# Create your views here.

class ImpactEventViewSet(ModelViewSet):
	queryset = ImpactEvent.objects.all()
	serializer_class = ImpactEventSerializer


	def retrieve(self, request, pk=None):
		print "called"
		impactEvent = request.data
		serializer = ImpactEventSerializer(impactEvent)
		return Response(serializer.data)

	@list_route()
	def test(self, request):
		print "called"




def app(request):
	return render(request, 'app.html')
