from django.db import models
from Citys_app.models import City

class Village(models.Model):
    village_id = models.IntegerField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="villages")
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="Village")
    is_approved = models.BooleanField(default=False)



    def __str__(self):
        return str(self.village_id)

class VillageProfile(models.Model):
    village_code = models.AutoField(primary_key=True)
    village_name = models.CharField(max_length=255)
    village_id = models.ForeignKey(Village, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField()
    population = models.IntegerField()
    area = models.FloatField(help_text="Area in square kilometers")
    elevation = models.FloatField(help_text="Elevation in meters")
    climate = models.CharField(max_length=100)
    primary_language = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="Village_Profile")
    is_approved = models.BooleanField(default=False)

    
    def __str__(self):
        return self.village_name

class SignificantPeople(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name="significant_people")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="significant_people")
    biography = models.TextField()
    contribution = models.TextField()
    area_of_influence = models.CharField(max_length=255)
    historic_period = models.CharField(max_length=255)
    award_or_recognation = models.TextField()
    related_events = models.TextField()
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="Significant_People")
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class CommunityServices(models.Model):
    community_id = models.IntegerField(primary_key=True)
    village_id = models.ForeignKey(Village, on_delete=models.CASCADE, related_name="community_services")
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="Community_Services")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.community_id)

class Education(models.Model):
    community_id = models.ForeignKey(CommunityServices, on_delete=models.CASCADE, related_name="education")
    school = models.CharField(max_length=255)
    collage = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    traning_center = models.CharField(max_length=255)
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="Education")
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.school

class HealthCare_facilities(models.Model):
    community_id = models.ForeignKey(CommunityServices, on_delete=models.CASCADE, related_name="healthcare_facilities")
    hospital = models.CharField(max_length=255)
    clinic = models.CharField(max_length=255)
    pharmacy = models.CharField(max_length=255)
    model_health_servics = models.CharField(max_length=255)
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="healthcare_facilities")
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.hospital

class market(models.Model):
    community_id = models.ForeignKey(CommunityServices, on_delete=models.CASCADE, related_name="market")
    details_local_market = models.TextField()
    Availibality_essential_goods = models.CharField(max_length=255)
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="market")
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.details_local_market

class Transportations(models.Model):
    community_id = models.ForeignKey(CommunityServices, on_delete=models.CASCADE, related_name="transportations")
    Buses = models.TextField()
    Rickshaw = models.TextField()
    Suzuki = models.TextField()
    major_Road = models.CharField(max_length=255)
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="Transportations")
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.Buses

class Uitilites(models.Model):
    community_id = models.ForeignKey(CommunityServices, on_delete=models.CASCADE, related_name="utilities")
    Water_supply = models.TextField()
    Electricity = models.TextField()
    Gas_supply = models.TextField()
    Petrol_pump = models.TextField()
    Internet_services = models.TextField()
    Network = models.TextField()
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="Uitilites")
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.Water_supply

class Recreational_facilites(models.Model):
    community_id = models.ForeignKey(CommunityServices, on_delete=models.CASCADE, related_name="recreational_facilities")
    parks_playground = models.CharField(max_length=255)
    community_center = models.CharField(max_length=255)
    sport_facilities = models.CharField(max_length=255)
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="Recreational_facilites")
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.community_center



# Main Tourist Attraction Model
class TouristAttraction(models.Model):
    tourist_attraction_id = models.AutoField(primary_key=True)
    Village_id = models.ForeignKey(Village, on_delete=models.CASCADE,related_name='TouristAttraction') # Assuming it's an integer ID referring to a Village model
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="TouristAttraction")
    is_approved = models.BooleanField(default=False)
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="Tourist_Attraction")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.tourist_attraction_id

# Natural Landmark Model
class NaturalLandmark(models.Model):
    tourist_attraction_id = models.ForeignKey(TouristAttraction, on_delete=models.CASCADE, related_name="natural_landmark")
    rivers = models.CharField(max_length=255)
    lakes = models.CharField(max_length=255)
    mountains = models.CharField(max_length=255)
    forest = models.CharField(max_length=255)
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="Natural_Landmark")
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.rivers 

# Cultural & Historical Places Model
class CulturalHistoricalPlaces(models.Model):
    tourist_attraction_id = models.ForeignKey(TouristAttraction, on_delete=models.CASCADE, related_name="cultural_places")
    temples = models.CharField(max_length=255)
    old_building = models.CharField(max_length=255)
    monuments = models.CharField(max_length=255)
    museums = models.CharField(max_length=255)
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="Cultural_HistoricalPlaces")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.temples

# Local Events Model
class LocalEvents(models.Model):
    tourist_attraction_id = models.ForeignKey(TouristAttraction, on_delete=models.CASCADE, related_name="local_events" )
    festivals = models.CharField(max_length=255)
    exhibitions = models.CharField(max_length=255)
    cultural_performance = models.CharField(max_length=255)
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="Local_Events")
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.festivals



# Main Additional Element Model
class AdditionalElement(models.Model):
    Additional_id = models.AutoField(primary_key=True)
    Village_id = models.ForeignKey(Village,on_delete=models.CASCADE)  # Assuming it's an integer ID referring to a Village model
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="Additional_Element")
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.Additional_id

# Land Use Zoning Model
class LandUseZoning(models.Model):
    Additional_element_id = models.ForeignKey( AdditionalElement, on_delete=models.CASCADE, related_name="land_use_zoning" )
    Agriculturals = models.CharField(max_length=255)
    Residential = models.CharField(max_length=255)
    Commercial_industrial = models.CharField(max_length=255)
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="Land_UseZoning")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.Agriculturals

# Infrastructure Development Model
class InfrastructureDevelopment(models.Model):
    Additional_element_id = models.ForeignKey(AdditionalElement, on_delete=models.CASCADE, related_name="infrastructure_development")
    Planned_project = models.CharField(max_length=255)
    Road_construction = models.CharField(max_length=255)
    Housing = models.CharField(max_length=255)
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="Infrastructure_Development")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.Planned_project

# Local Business & Employment Model
class LocalBusinessEmployment(models.Model):
    Additional_element_id = models.ForeignKey(AdditionalElement, on_delete=models.CASCADE, related_name="local_business_employment")
    Small_business = models.CharField(max_length=255)
    Job_opportunities = models.CharField(max_length=255)
    Skill_development_center = models.CharField(max_length=255)
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="Local_Business_Employment")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.Small_business

# Public Services Contact Model
class PublicServicesContact(models.Model):
    Additional_element_id = models.ForeignKey(AdditionalElement, on_delete=models.CASCADE, related_name="public_services_contact")
    Contact_water_supply = models.CharField(max_length=255)
    Contact_electricity = models.CharField(max_length=255)
    Contact_gas_supply = models.CharField(max_length=255)
    Emergency_helpline = models.CharField(max_length=255)
    submitted_by = models.ForeignKey('Users_app.User', on_delete=models.CASCADE, related_name="public_services_contact")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.Contact_water_supply
