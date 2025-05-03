from rest_framework import serializers
from .models import Village, VillageProfile, SignificantPeople,CommunityServices,Education,HealthCare_facilities,market,Transportations,Uitilites,Recreational_facilites,TouristAttraction,NaturalLandmark,CulturalHistoricalPlaces,LocalEvents,AdditionalElement,LandUseZoning,InfrastructureDevelopment,LocalBusinessEmployment,PublicServicesContact

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it

class VillageProfileSerializer(serializers.ModelSerializer):  # Fixed from VillagePropileSerializer
    class Meta:
        model = VillageProfile
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it

class SignificantPeopleSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField()
    class Meta:
        model = SignificantPeople
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it
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
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it
        

class HealthCareFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCare_facilities
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = market
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it

class TransportationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportations
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it

class UtilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uitilites
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it

class RecreationalFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recreational_facilites
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it

class TouristAttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristAttraction
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it

class NaturalLandmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaturalLandmark
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it

class CulturalHistoricalPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CulturalHistoricalPlaces
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it

class LocalEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalEvents
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by']

class AdditionalElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalElement
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it

class LandUseZoningSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandUseZoning
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it

class InfrastructureDevelopmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfrastructureDevelopment
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it

class LocalBusinessEmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalBusinessEmployment
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by'] # prevent users from manually setting it

class PublicServicesContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicServicesContact
        fields = '__all__'
        read_only_fields = ['is_approved', 'submitted_by']
