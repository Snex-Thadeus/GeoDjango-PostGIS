from re import L
from django.contrib import admin
from .models import Counties, Incidences
from leaflet.admin import LeafletGeoAdmin


class IncidencesAdmin(LeafletGeoAdmin):

    list_display = ('name', 'location')

class CountiesAdmin(LeafletGeoAdmin):
    list_display = ('counties', 'codes')


admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Counties, CountiesAdmin)

# py manage.py ogrinspect reporter\data\counties.shp Counties --srid=4325 --mapping --multi