from django.contrib import admin
from .models import PopulationDetail,PopulationAdult,PopulationChildren,PopulationElderly,PopulationLiteracyRate,GenderRatio,GeographicalInformation,GeoArea,ClimateDetail,HistoricalBackground,Economy,Farming,Handicrafts,Industries
@admin.register(PopulationDetail)
class PopulationDetailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PopulationDetail._meta.fields]
    list_filter = ['is_approved']
    readonly_fields = ['submitted_by']

@admin.register(PopulationChildren)
class PopulationChildren(admin.ModelAdmin):
    list_display = [field.name for field in PopulationChildren._meta.fields]
    list_filter = ['is_approved']
    readonly_fields = ['submitted_by']


@admin.register(PopulationAdult)
class PopulationAdult(admin.ModelAdmin):
    list_display = [field.name for field in PopulationAdult._meta.fields]
    list_filter = ['is_approved']
    readonly_fields = ['submitted_by']

@admin.register(PopulationElderly)
class PopulationElderly(admin.ModelAdmin):
    list_display = [field.name for field in PopulationElderly._meta.fields]
    list_filter = ['is_approved']
    readonly_fields = ['submitted_by']

@admin.register(PopulationLiteracyRate)
class PopulationLiteracyRate(admin.ModelAdmin):
    list_display = [field.name for field in PopulationLiteracyRate._meta.fields]
    list_filter = ['is_approved']
    readonly_fields = ['submitted_by']

@admin.register(GenderRatio)
class GenderRatio(admin.ModelAdmin):
    list_display = [field.name for field in GenderRatio._meta.fields]
    list_filter = ['is_approved']
    readonly_fields = ['submitted_by']

@admin.register(GeographicalInformation)
class GeographicalInformation(admin.ModelAdmin):
    list_display = [field.name for field in GeographicalInformation._meta.fields]
    list_filter = ['is_approved']
    readonly_fields = ['submitted_by']

@admin.register(GeoArea)
class GeoArea (admin.ModelAdmin):
    list_display = [field.name for field in GeoArea._meta.fields]
    list_filter = ['is_approved']
    readonly_fields = ['submitted_by']

@admin.register(ClimateDetail)
class ClimateDetail(admin.ModelAdmin):
    list_display = [field.name for field in ClimateDetail._meta.fields]
    list_filter = ['is_approved']
    readonly_fields = ['submitted_by']

@admin.register(HistoricalBackground)
class HistoricalBackground(admin.ModelAdmin):
    list_display = [field.name for field in HistoricalBackground._meta.fields]
    list_filter = ['is_approved']
    readonly_fields = ['submitted_by']

@admin.register(Economy)
class Economy(admin.ModelAdmin):
    list_display = [field.name for field in Economy._meta.fields]
    list_filter = ['is_approved']
    readonly_fields = ['submitted_by']

@admin.register(Farming)
class Farming(admin.ModelAdmin):
    list_display = [field.name for field in Farming._meta.fields]
    list_filter = ['is_approved']
    readonly_fields = ['submitted_by']

@admin.register(Handicrafts) 
class Handicrafts(admin.ModelAdmin):
    list_display = [field.name for field in Handicrafts._meta.fields]
    list_filter = ['is_approved']
    readonly_fields = ['submitted_by']

@admin.register(Industries)
class Industries(admin.ModelAdmin):
    list_display = [field.name for field in Industries._meta.fields]
    list_filter = ['is_approved']
    readonly_fields = ['submitted_by']


# Register your models here.
