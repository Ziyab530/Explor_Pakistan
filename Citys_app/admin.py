from django.contrib import admin
from .models import province,Division, District, City,RegionEvent,ReligiousFestival,CulturalFestival,FolkFestival,RegionalEvent,NationalEvent,GlobalEvent,AdventureEvent,EmergencyContact,PoliceStation,FireStation,MedicalEmergency

admin.site.register(province)
admin.site.register(Division)
admin.site.register(District)
admin.site.register(City)
admin.site.register(RegionEvent)
admin.site.register(ReligiousFestival)
admin.site.register(CulturalFestival)
admin.site.register(FolkFestival)
admin.site.register(RegionalEvent)
admin.site.register(NationalEvent)
admin.site.register(GlobalEvent)
admin.site.register(AdventureEvent)
admin.site.register(EmergencyContact)
admin.site.register(PoliceStation)
admin.site.register(FireStation)
admin.site.register(MedicalEmergency)

# Register your models here.
