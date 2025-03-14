from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import PopulationDetail,PopulationChildren,PopulationAdult,PopulationElderly,PopulationLiteracyRate,GenderRatio,GeographicalInformation,LocationInformation,GeoArea,ClimateDetail,HistoricalBackground,Economy,Farming,Handicrafts,Industries,CulturalInformation,LocalFestival,LanguageSpoken,Traditions
from .serializers import PopulationDetailSerializer,PopulationChildrenSerializer,PopulationAdultSerializer,PopulationElderlySerializer,PopulationLiteracyRateSerializer,GenderRatioSerializer,GeographicalInformationSerializer,LocationInformationSerializer,GeoAreaSerializer,ClimateDetailSerializer,HistoricalBackgroundSerializer,EconomySerializer,FarmingSerializer,HandicraftsSerializer,IndustriesSerializer,CulturalInformationSerializer,LocalFestivalSerializer,LanguageSpokenSerializer,TraditionsSerializer
from .filters import PopulationDetailFilter,PopulationChildrenFilter,PopulationAdultFilter,PopulationElderlyFilter,GenderRatioFilter,PopulationLiteracyRateFilter,GeographicalInformationFilter,LocationInformationFilter,GeoAreaFilter,ClimateDetailFilter,HistoricalBackgroundFilter,EconomyFilter,FarmingFilter,HandicraftsFilter,IndustriesFilter,CulturalInformationFilter,LocalFestivalFilter,LanguageSpokenFilter,TraditionsFilter
from .permissions import IsAuthenticatedOrReadOnlyWithAdminFullAccess
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class PopulationDetailViewSet(viewsets.ModelViewSet):
    queryset = PopulationDetail.objects.all()
    serializer_class = PopulationDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PopulationDetailFilter 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]


class PopulationChildrenViewSet(viewsets.ModelViewSet):
    queryset = PopulationChildren.objects.all()
    serializer_class = PopulationChildrenSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PopulationChildrenFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class PopulationAdultViewSet(viewsets.ModelViewSet):
    queryset = PopulationAdult.objects.all()
    serializer_class = PopulationAdultSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_class = PopulationAdultFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class PopulationElderlyViewSet(viewsets.ModelViewSet):
    queryset = PopulationElderly.objects.all()
    serializer_class = PopulationElderlySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PopulationElderlyFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]


class GenderRatioViewSet(viewsets.ModelViewSet):
    queryset = GenderRatio.objects.all()
    serializer_class = GenderRatioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GenderRatioFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class PopulationLiteracyRateViewSet(viewsets.ModelViewSet):
    queryset = PopulationLiteracyRate.objects.all()
    serializer_class = PopulationLiteracyRateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PopulationLiteracyRateFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class GeographicalInformationViewSet(viewsets.ModelViewSet):
    queryset = GeographicalInformation.objects.all()
    serializer_class = GeographicalInformationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GeographicalInformationFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class LocationInformationViewSet(viewsets.ModelViewSet):
    queryset = LocationInformation.objects.all()
    serializer_class = LocationInformationSerializer
    filter_backends = [DjangoFilterBackend]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]
    

class GeoAreaViewSet(viewsets.ModelViewSet):
    queryset = GeoArea.objects.all()
    serializer_class = GeoAreaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GeoAreaFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class ClimateDetailViewSet(viewsets.ModelViewSet):
    queryset = ClimateDetail.objects.all()
    serializer_class = ClimateDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClimateDetailFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class HistoricalBackgroundViewSet(viewsets.ModelViewSet):
    queryset = HistoricalBackground.objects.all()
    serializer_class = HistoricalBackgroundSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoricalBackgroundFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class EconomyViewSet(viewsets.ModelViewSet):
    queryset = Economy.objects.all()
    serializer_class = EconomySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EconomyFilter
    filter_backends = [DjangoFilterBackend]
    filterset_class = EconomyFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class FarmingViewSet(viewsets.ModelViewSet):
    queryset = Farming.objects.all()
    serializer_class = FarmingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FarmingFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class HandicraftsViewSet(viewsets.ModelViewSet):
    queryset = Handicrafts.objects.all()
    serializer_class = HandicraftsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HandicraftsFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class IndustriesViewSet(viewsets.ModelViewSet):
    queryset = Industries.objects.all()
    serializer_class = IndustriesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = IndustriesFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class CulturalInformationViewSet(viewsets.ModelViewSet):
    queryset = CulturalInformation.objects.all()
    serializer_class = CulturalInformationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CulturalInformationFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class LocalFestivalViewSet(viewsets.ModelViewSet):
    queryset = LocalFestival.objects.all()
    serializer_class = LocalFestivalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LocalFestivalFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class TraditionsViewSet(viewsets.ModelViewSet):
    queryset = Traditions.objects.all()
    serializer_class = TraditionsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TraditionsFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class LanguageSpokenViewSet(viewsets.ModelViewSet):
    queryset = LanguageSpoken.objects.all()
    serializer_class = LanguageSpokenSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LanguageSpokenFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]
