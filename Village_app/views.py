from django.shortcuts import render
from rest_framework import viewsets
from .models import Village, VillageProfile, SignificantPeople,CommunityServices,Education,HealthCare_facilities,market,Transportations,Uitilites,Recreational_facilites,TouristAttraction,NaturalLandmark,CulturalHistoricalPlaces,LocalEvents,AdditionalElement,LandUseZoning,InfrastructureDevelopment,LocalBusinessEmployment,PublicServicesContact
from .serializers import VillageSerializer, VillageProfileSerializer, SignificantPeopleSerializer,CommunityServicesSerializer,EducationSerializer,HealthCareFacilitiesSerializer,MarketSerializer,TransportationSerializer,UtilitiesSerializer,RecreationalFacilitiesSerializer,TouristAttractionSerializer,NaturalLandmarkSerializer,CulturalHistoricalPlacesSerializer,LocalEventsSerializer,AdditionalElementSerializer,LandUseZoningSerializer,InfrastructureDevelopmentSerializer,LocalBusinessEmploymentSerializer,PublicServicesContactSerializer
from .filters import VillageFilter , VillageProfileFilter, SignificantPeopleFilter,CommunityServicesFilter,EducationFilter,HealthCareFacilitiesFilter,MarketFilter,TransportationsFilter,UtilitiesFilter,RecreationalFacilitiesFilter,TouristAttractionFilter,NaturalLandmarkFilter,CulturalHistoricalPlacesFilter,LocalEventsFilter,AdditionalElementFilter,LandUseZoningFilter,InfrastructureDevelopmentFilter,LocalBusinessEmploymentFilter,PublicServicesContactFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAuthenticatedOrReadOnlyWithAdminFullAccess
class VillageViewSet(viewsets.ModelViewSet):

    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = VillageFilter
    ordering_fields = ['village_id']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class VillageProfileViewSet(viewsets.ModelViewSet):
    queryset = VillageProfile.objects.all()
    serializer_class = VillageProfileSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = VillageProfileFilter
    ordering_fields = ['village_name', 'population', 'area']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class SignificantPeopleViewSet(viewsets.ModelViewSet):
    queryset = SignificantPeople.objects.all()
    serializer_class = SignificantPeopleSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = SignificantPeopleFilter
    ordering_fields = ['name', 'age', 'historic_period']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]



class CommunityServicesViewSet(viewsets.ModelViewSet):
    queryset = CommunityServices.objects.all()
    serializer_class = CommunityServicesSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = CommunityServicesFilter
    ordering_fields = ['community_id']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = EducationFilter
    ordering_fields = ['school', 'collage', 'university']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class HealthCareFacilitiesViewSet(viewsets.ModelViewSet):
    queryset = HealthCare_facilities.objects.all()
    serializer_class = HealthCareFacilitiesSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = HealthCareFacilitiesFilter
    ordering_fields = ['hospital', 'clinic', 'pharmacy']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]


class MarketViewSet(viewsets.ModelViewSet):
    queryset = market.objects.all()
    serializer_class = MarketSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MarketFilter
    ordering_fields = ['details_local_market', 'Availibality_essential_goods']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess] 

class TransportationViewSet(viewsets.ModelViewSet):
    queryset = Transportations.objects.all()
    serializer_class = TransportationSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = TransportationsFilter
    ordering_fields = ['Buses', 'Rickshaw', 'Suzuki']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class UtilitiesViewSet(viewsets.ModelViewSet):
    queryset =Uitilites.objects.all()
    serializer_class = UtilitiesSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = UtilitiesFilter
    ordering_fields = ['Electricity', 'Water', 'Gas']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class RecreationalFacilitiesViewSet(viewsets.ModelViewSet):
    queryset = Recreational_facilites.objects.all()
    serializer_class = RecreationalFacilitiesSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = RecreationalFacilitiesFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]
   

class TouristAttractionViewSet(viewsets.ModelViewSet):
    queryset = TouristAttraction.objects.all()
    serializer_class = TouristAttractionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = TouristAttractionFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]


class NaturalLandmarkViewSet(viewsets.ModelViewSet):
    queryset = NaturalLandmark.objects.all()
    serializer_class = NaturalLandmarkSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = NaturalLandmarkFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class CulturalHistoricalPlacesViewSet(viewsets.ModelViewSet):
    queryset = CulturalHistoricalPlaces.objects.all()
    serializer_class = CulturalHistoricalPlacesSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = CulturalHistoricalPlacesFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class LocalEventsViewSet(viewsets.ModelViewSet):
    queryset = LocalEvents.objects.all()
    serializer_class = LocalEventsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = LocalEventsFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class AdditionalElementViewSet(viewsets.ModelViewSet):
    queryset = AdditionalElement.objects.all()
    serializer_class = AdditionalElementSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = AdditionalElementFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class LandUseZoningViewSet(viewsets.ModelViewSet):
    queryset = LandUseZoning.objects.all()
    serializer_class = LandUseZoningSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_classs = LandUseZoningFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class InfrastructureDevelopmentViewSet(viewsets.ModelViewSet):
    queryset = InfrastructureDevelopment.objects.all()
    serializer_class = InfrastructureDevelopmentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = InfrastructureDevelopmentFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class LocalBusinessEmploymentViewSet(viewsets.ModelViewSet):
    queryset = LocalBusinessEmployment.objects.all()
    serializer_class = LocalBusinessEmploymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = LocalBusinessEmploymentFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]

class PublicServicesContactViewSet(viewsets.ModelViewSet):
    queryset = PublicServicesContact.objects.all()
    serializer_class = PublicServicesContactSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = PublicServicesContactFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnlyWithAdminFullAccess]
# Create your views here.
