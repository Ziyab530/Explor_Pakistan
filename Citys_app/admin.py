from django.contrib import admin
from .models import province,Division, District, City,RegionEvent,ReligiousFestival,CulturalFestival,FolkFestival,RegionalEvent,NationalEvent,GlobalEvent,AdventureEvent,EmergencyContact,PoliceStation,FireStation,MedicalEmergency

admin.site.register(province)
admin.site.register(Division)
admin.site.register(District)
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('City_name', 'District', 'is_approved', 'submitted_by')
    list_filter = ('is_approved', 'District', 'submitted_by')
    search_fields = ('City_name', 'District__District_name', 'submitted_by__email')
    actions = ['approve_selected']

    def approve_selected(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f"{updated} city(ies) approved.")
    approve_selected.short_description = "Approve selected cities"

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
