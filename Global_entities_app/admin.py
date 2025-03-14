from django.contrib import admin
from .models import PopulationDetail,PopulationAdult,PopulationChildren,PopulationElderly,PopulationLiteracyRate,GenderRatio,GeographicalInformation,GeoArea,ClimateDetail,HistoricalBackground,Economy,Farming,Handicrafts,Industries
admin.site.register(PopulationDetail)
admin.site.register(PopulationChildren)
admin.site.register(PopulationAdult)
admin.site.register(PopulationElderly)
admin.site.register(PopulationLiteracyRate)
admin.site.register(GenderRatio)
admin.site.register(GeographicalInformation)
admin.site.register(GeoArea)
admin.site.register(ClimateDetail)
admin.site.register(HistoricalBackground)
admin.site.register(Economy)
admin.site.register(Farming)
admin.site.register(Handicrafts)
admin.site.register(Industries)
# Register your models here.
