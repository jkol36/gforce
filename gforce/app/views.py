from django.shortcuts import render
from rest_framework.decorators import list_route
from rest_framework.ViewSets

# Create your views here.

def app(request):
	return render(request, 'app.html')
