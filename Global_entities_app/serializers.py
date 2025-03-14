from rest_framework import serializers
from .models import PopulationDetail,PopulationChildren,PopulationAdult,PopulationLiteracyRate,GenderRatio,PopulationElderly,GeographicalInformation,LocationInformation,GeoArea,ClimateDetail,HistoricalBackground,Economy,Farming,Handicrafts,Industries,CulturalInformation,LocalFestival,LanguageSpoken,Traditions

class PopulationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopulationDetail
        fields = '__all__'

class PopulationChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopulationChildren
        fields = '__all__'

class PopulationAdultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopulationAdult
        fields = '__all__'

class PopulationElderlySerializer(serializers.ModelSerializer):
    class Meta:
        model = PopulationElderly
        fields = '__all__'

class GenderRatioSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderRatio
        fields = '__all__'

class PopulationLiteracyRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopulationLiteracyRate
        fields = '__all__'

class GeographicalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeographicalInformation
        fields = '__all__'

class LocationInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationInformation
        fields = '__all__'

class GeoAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoArea
        fields = '__all__'

class ClimateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClimateDetail
        fields = '__all__'

class HistoricalBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalBackground
        fields = '__all__'

class EconomySerializer(serializers.ModelSerializer):
    class Meta:
        model = Economy
        fields = '__all__'

class FarmingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farming
        fields = '__all__'

class HandicraftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handicrafts
        fields = '__all__'

class IndustriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Industries
        fields = '__all__'
class CulturalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CulturalInformation
        fields = '__all__'

class LocalFestivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalFestival
        fields = '__all__'

class TraditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traditions
        fields = '__all__'

class LanguageSpokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageSpoken
        fields = '__all__'
