from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager


class Incidences(models.Model):
    name = models.CharField(max_length=20, verbose_name='Incidences')
    location = models.PointField(srid=4326)
    objects = GeoManager()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Incidences"

# This is an auto-generated Django model module created by ogrinspect.
class Counties(models.Model):
    counties = models.CharField(max_length=25)
    codes = models.IntegerField()
    cty_code = models.CharField(max_length=24)
    dis = models.IntegerField(null=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.counties


    class Meta:
        verbose_name_plural = "Counties"