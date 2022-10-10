from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Counties, Incidences
from django.core import serializers

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'


def county_datasets(request):
    counties = serializers.serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type='json')


def point_datasets(request):
    points = serializers.serialize('geojson', Incidences.objects.all())
    return HttpResponse(points, content_type='json')
