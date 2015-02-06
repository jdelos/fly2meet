from django.db import models
from django.utils import timezone

# Create your models here.

#Create a trip class
class Trip(models.Model):
    dep_date      = models.DateField(blank=True, null=False)
    ret_date      = models.DateField(blank=True, null=False)
    n_psgrs       = models.IntegerField(default=0)
    n_orgs        = models.IntegerField(default=0)
    places     = models.ManyToManyField('Place')
    flights    = models.ManyToManyField('Flight')


class Place(models.Model):
    name         =  models.CharField(max_length=10)
    type         =  models.CharField(max_length=10)
    CountryName  =  models.CharField(max_length=50)
    CityName     =  models.CharField(max_length=50)
    #as_trip      =  models.ForeignKey('Trip',primary_key=False)
    n_people     =  models.IntegerField(default=0)
    def __str__(self):
        return(self.name)

class Flight(models.Model):
    n_flight    = models.CharField(max_length=10)
    n_cflight   = models.CharField(max_length=10)
    stations    = models.ManyToManyField('Place')
    #trip     = models.ForeignKey('Trip',primary_key=False)
    dep_time    = models.DateTimeField(blank=True, null=True)
    arr_time    = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return(self.n_flight)
        
class Search(models.Model):
    dep_date      = models.DateField(blank=True, null=False)
    ret_date      = models.DateField(blank=True, null=False)
    org_1         = models.CharField(null=False,max_length=20)
    org_2         = models.CharField(null=False,max_length=20)
    org_3         = models.CharField(null=False,max_length=20)
    org_4         = models.CharField(null=False,max_length=20)
    org_5         = models.CharField(null=False,max_length=20)
    org_6         = models.CharField(null=False,max_length=20)
    org_7         = models.CharField(null=False,max_length=20)
    org_8         = models.CharField(null=False,max_length=20)
    org_9         = models.CharField(null=False,max_length=20)
    org_10        = models.CharField(null=False,max_length=20)
