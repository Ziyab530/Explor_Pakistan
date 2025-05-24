from django.contrib import admin
from .models import Village, VillageProfile, SignificantPeople,CommunityServices,Education,HealthCare_facilities,market,Transportations,Uitilites,Recreational_facilites,TouristAttraction,NaturalLandmark,CulturalHistoricalPlaces,LocalEvents,AdditionalElement,LandUseZoning,InfrastructureDevelopment,LocalBusinessEmployment,PublicServicesContact

@admin.register(Village)
class LanguageSpokenAdmin(admin.ModelAdmin):
      list_display = [field.name for field in Village._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(VillageProfile)
class VillageProfileAdmin(admin.ModelAdmin):
      list_display = [field.name for field in VillageProfile._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(SignificantPeople)
class SignificantPeopleAdmin(admin.ModelAdmin):
      list_display = [field.name for field in SignificantPeople._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(CommunityServices)
class CommunityServicesAdmin(admin.ModelAdmin):
      list_display = [field.name for field in CommunityServices._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
      list_display = [field.name for field in Education._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(HealthCare_facilities)
class HealthCareFacilitiesAdmin(admin.ModelAdmin):
      list_display = [field.name for field in HealthCare_facilities._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(market)
class MarketAdmin(admin.ModelAdmin):
      list_display = [field.name for field in market._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(Transportations)
class TransportationAdmin(admin.ModelAdmin):
      list_display = [field.name for field in Transportations._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(Uitilites)
class UtilitiesAdmin(admin.ModelAdmin):
      list_display = [field.name for field in Uitilites._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(Recreational_facilites)
class RecreationalFacilitiesAdmin(admin.ModelAdmin):
      list_display = [field.name for field in Recreational_facilites._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(TouristAttraction)
class TouristAttractionAdmin(admin.ModelAdmin):
      list_display = [field.name for field in TouristAttraction._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(NaturalLandmark)
class NaturalLandmarkAdmin(admin.ModelAdmin):
      list_display = [field.name for field in NaturalLandmark._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(CulturalHistoricalPlaces)
class CulturalHistoricalPlacesAdmin(admin.ModelAdmin):
      list_display = [field.name for field in CulturalHistoricalPlaces._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(LocalEvents)
class LocalEventsAdmin(admin.ModelAdmin):
      list_display = [field.name for field in LocalEvents._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(AdditionalElement)
class AdditionalElementAdmin(admin.ModelAdmin):
      list_display = [field.name for field in AdditionalElement._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(LandUseZoning)  
class LandUseZoningAdmin(admin.ModelAdmin):
      list_display = [field.name for field in LandUseZoning._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(InfrastructureDevelopment)  
class InfrastructureDevelopmentAdmin(admin.ModelAdmin):
      list_display = [field.name for field in InfrastructureDevelopment._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

@admin.register(LocalBusinessEmployment)
class LocalBusinessEmploymentAdmin(admin.ModelAdmin):
      list_display = [field.name for field in LocalBusinessEmployment._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']
      
@admin.register(PublicServicesContact)
class PublicServicesContactAdmin(admin.ModelAdmin):
      list_display = [field.name for field in PublicServicesContact._meta.fields]
      list_filter = ['is_approved']
      search_fields = ['submitted_by']

# Register your models here.
