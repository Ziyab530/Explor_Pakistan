import django_filters
from .models import Village,VillageProfile, SignificantPeople,CommunityServices,Education,HealthCare_facilities,market,Transportations,Uitilites,Recreational_facilites,TouristAttraction,NaturalLandmark,CulturalHistoricalPlaces,LocalEvents,AdditionalElement,LandUseZoning,InfrastructureDevelopment,LocalBusinessEmployment,PublicServicesContact

# Filter for Village
class VillageFilter(django_filters.FilterSet):
    village_id = django_filters.NumberFilter()
    city = django_filters.NumberFilter(field_name='city_id')

    class Meta:
        model = Village
        fields = ['village_id', 'city']


# Filter for VillageProfile
class VillageProfileFilter(django_filters.FilterSet):
    village_name = django_filters.CharFilter(lookup_expr='icontains')
    village_id = django_filters.NumberFilter(field_name='village_id')
    population = django_filters.RangeFilter()
    area = django_filters.RangeFilter()
    elevation = django_filters.RangeFilter()
    climate = django_filters.CharFilter(lookup_expr='icontains')
    primary_language = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = VillageProfile
        fields = ['village_name', 'village_id', 'population', 'area', 'elevation', 'climate', 'primary_language']


# Filter for SignificantPeople
class SignificantPeopleFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    age = django_filters.RangeFilter()
    village = django_filters.NumberFilter(field_name='village_id')
    city = django_filters.NumberFilter(field_name='city_id')
    area_of_influence = django_filters.CharFilter(lookup_expr='icontains')
    historic_period = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = SignificantPeople
        fields = ['name', 'age', 'village', 'city', 'area_of_influence', 'historic_period']


# Filter for CommunityServices
class CommunityServicesFilter(django_filters.FilterSet):
    community_id = django_filters.NumberFilter()
    village_id = django_filters.NumberFilter(field_name='village_id')

    class Meta:
        model = CommunityServices
        fields = ['community_id', 'village_id']


# Filter for Education
class EducationFilter(django_filters.FilterSet):
    community_id = django_filters.NumberFilter(field_name='community_id')
    school = django_filters.CharFilter(lookup_expr='icontains')
    collage = django_filters.CharFilter(lookup_expr='icontains')
    university = django_filters.CharFilter(lookup_expr='icontains')
    traning_center = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Education
        fields = ['community_id', 'school', 'collage', 'university', 'traning_center']
# Filter for HealthCare Facilities
class HealthCareFacilitiesFilter(django_filters.FilterSet):
    community_id = django_filters.NumberFilter(field_name='community_id')
    hospital = django_filters.CharFilter(lookup_expr='icontains')
    clinic = django_filters.CharFilter(lookup_expr='icontains')
    pharmacy = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = HealthCare_facilities
        fields = ['community_id', 'hospital', 'clinic', 'pharmacy']
        # Filter for Market
class MarketFilter(django_filters.FilterSet):
    community_id = django_filters.NumberFilter(field_name='community_id')
    details_local_market = django_filters.CharFilter(lookup_expr='icontains')
    Availibality_essential_goods = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = market
        fields = ['community_id', 'details_local_market', 'Availibality_essential_goods']        

# Filter for Transportations
class TransportationsFilter(django_filters.FilterSet):
    community_id = django_filters.NumberFilter(field_name='community_id')
    major_Road = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Transportations
        fields = ['community_id', 'major_Road']

# Filter for Utilities
class UtilitiesFilter(django_filters.FilterSet):
    community_id = django_filters.NumberFilter(field_name='community_id')
    Water_supply = django_filters.CharFilter(lookup_expr='icontains')
    Electricity = django_filters.CharFilter(lookup_expr='icontains')
    Gas_supply = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Uitilites
        fields = ['community_id', 'Water_supply', 'Electricity', 'Gas_supply']
# Filter for Recreational Facilities
class RecreationalFacilitiesFilter(django_filters.FilterSet):
    community_id = django_filters.NumberFilter(field_name='community_id')
    community_center = django_filters.CharFilter(lookup_expr='icontains')
    sport_facilities = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Recreational_facilites
        fields = ['community_id', 'community_center', 'sport_facilities']

# Filter for Tourist Attraction
class TouristAttractionFilter(django_filters.FilterSet):
    Village_id = django_filters.NumberFilter(field_name='Village_id')

    class Meta:
        model = TouristAttraction
        fields = ['Village_id']


# Filter for Natural Landmarks
class NaturalLandmarkFilter(django_filters.FilterSet):
    tourist_attraction_id = django_filters.NumberFilter(field_name='tourist_attraction_id')
    rivers = django_filters.CharFilter(lookup_expr='icontains')
    mountains = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = NaturalLandmark
        fields = ['tourist_attraction_id', 'rivers', 'mountains']


# Filter for Cultural & Historical Places
class CulturalHistoricalPlacesFilter(django_filters.FilterSet):
    tourist_attraction_id = django_filters.NumberFilter(field_name='tourist_attraction_id')
    temples = django_filters.CharFilter(lookup_expr='icontains')
    monuments = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CulturalHistoricalPlaces
        fields = ['tourist_attraction_id', 'temples', 'monuments']


# Filter for Local Events
class LocalEventsFilter(django_filters.FilterSet):
    tourist_attraction_id = django_filters.NumberFilter(field_name='tourist_attraction_id')
    festivals = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = LocalEvents
        fields = ['tourist_attraction_id', 'festivals']


# Filter for Additional Elements
class AdditionalElementFilter(django_filters.FilterSet):
    Village_id = django_filters.NumberFilter(field_name='Village_id')

    class Meta:
        model = AdditionalElement
        fields = ['Village_id']


# Filter for Land Use Zoning
class LandUseZoningFilter(django_filters.FilterSet):
    Additional_element_id = django_filters.NumberFilter(field_name='Additional_element_id')
    Agriculturals = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = LandUseZoning
        fields = ['Additional_element_id', 'Agriculturals']


# Filter for Infrastructure Development
class InfrastructureDevelopmentFilter(django_filters.FilterSet):
    Additional_element_id = django_filters.NumberFilter(field_name='Additional_element_id')
    Planned_project = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = InfrastructureDevelopment
        fields = ['Additional_element_id', 'Planned_project']


# Filter for Local Business & Employment
class LocalBusinessEmploymentFilter(django_filters.FilterSet):
    Additional_element_id = django_filters.NumberFilter(field_name='Additional_element_id')
    Small_business = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = LocalBusinessEmployment
        fields = ['Additional_element_id', 'Small_business']


# Filter for Public Services Contact
class PublicServicesContactFilter(django_filters.FilterSet):
    Additional_element_id = django_filters.NumberFilter(field_name='Additional_element_id')
    Contact_water_supply = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = PublicServicesContact
        fields = ['Additional_element_id', 'Contact_water_supply']
