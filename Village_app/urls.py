from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VillageViewSet, VillageProfileViewSet, SignificantPeopleViewSet, CommunityServicesViewSet, EducationViewSet, HealthCareFacilitiesViewSet, MarketViewSet, TransportationViewSet, UtilitiesViewSet, RecreationalFacilitiesViewSet, TouristAttractionViewSet, NaturalLandmarkViewSet, CulturalHistoricalPlacesViewSet, LocalEventsViewSet, AdditionalElementViewSet, LandUseZoningViewSet, InfrastructureDevelopmentViewSet, LocalBusinessEmploymentViewSet, PublicServicesContactViewSet

router = DefaultRouter()
router.register(r'villages', VillageViewSet)
router.register(r'village-profile', VillageProfileViewSet)
router.register(r'significant-people', SignificantPeopleViewSet)
router.register(r'community_services', CommunityServicesViewSet)
router.register(r'education', EducationViewSet)
router.register(r'healthcare_facilities', HealthCareFacilitiesViewSet)
router.register(r'market', MarketViewSet)
router.register(r'transportation', TransportationViewSet)
router.register(r'utilities', UtilitiesViewSet)
router.register(r'recreational_facilities', RecreationalFacilitiesViewSet)
router.register(r'tourist_attractions', TouristAttractionViewSet)
router.register(r'natural_landmarks', NaturalLandmarkViewSet)
router.register(r'cultural_historical_places', CulturalHistoricalPlacesViewSet)
router.register(r'local_events', LocalEventsViewSet)
router.register(r'additional_elements', AdditionalElementViewSet)
router.register(r'land_use_zoning', LandUseZoningViewSet)
router.register(r'infrastructure_development', InfrastructureDevelopmentViewSet)
router.register(r'local_business_employment', LocalBusinessEmploymentViewSet)
router.register(r'public_services_contact', PublicServicesContactViewSet)




urlpatterns = [
    path('', include(router.urls)),
]
