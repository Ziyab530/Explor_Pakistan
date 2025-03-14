from rest_framework import serializers
from .models import Village, VillageProfile, SignificantPeople,CommunityServices,Education,HealthCare_facilities,market,Transportations,Uitilites,Recreational_facilites,TouristAttraction,NaturalLandmark,CulturalHistoricalPlaces,LocalEvents,AdditionalElement,LandUseZoning,InfrastructureDevelopment,LocalBusinessEmployment,PublicServicesContact

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = '__all__'

class VillageProfileSerializer(serializers.ModelSerializer):  # Fixed from VillagePropileSerializer
    class Meta:
        model = VillageProfile
        fields = '__all__'

class SignificantPeopleSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField()
    class Meta:
        model = SignificantPeople
        fields = '__all__'
    def validate_age(self, value):
        """Field-level validation for age"""
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative.")
        if value > 120:
            raise serializers.ValidationError("Age must be realistic (0-120).")
        return value
class CommunityServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityServices
        fields = '__all__'  # Includes all fields

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class HealthCareFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCare_facilities
        fields = '__all__'

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = market
        fields = '__all__'

class TransportationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportations
        fields = '__all__'

class UtilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uitilites
        fields = '__all__'

class RecreationalFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recreational_facilites
        fields = '__all__'

class TouristAttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristAttraction
        fields = '__all__'

class NaturalLandmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaturalLandmark
        fields = '__all__'

class CulturalHistoricalPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CulturalHistoricalPlaces
        fields = '__all__'

class LocalEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalEvents
        fields = '__all__'

class AdditionalElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalElement
        fields = '__all__'

class LandUseZoningSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandUseZoning
        fields = '__all__'

class InfrastructureDevelopmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfrastructureDevelopment
        fields = '__all__'

class LocalBusinessEmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalBusinessEmployment
        fields = '__all__'

class PublicServicesContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicServicesContact
        fields = '__all__'
