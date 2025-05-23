# Generated by Django 5.1.6 on 2025-04-26 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Citys_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalElement',
            fields=[
                ('Additional_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityServices',
            fields=[
                ('community_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TouristAttraction',
            fields=[
                ('tourist_attraction_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=255)),
                ('collage', models.CharField(max_length=255)),
                ('university', models.CharField(max_length=255)),
                ('traning_center', models.CharField(max_length=255)),
                ('community_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='Village_app.communityservices')),
            ],
        ),
        migrations.CreateModel(
            name='HealthCare_facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.CharField(max_length=255)),
                ('clinic', models.CharField(max_length=255)),
                ('pharmacy', models.CharField(max_length=255)),
                ('model_health_servics', models.CharField(max_length=255)),
                ('community_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='healthcare_facilities', to='Village_app.communityservices')),
            ],
        ),
        migrations.CreateModel(
            name='InfrastructureDevelopment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Planned_project', models.CharField(max_length=255)),
                ('Road_construction', models.CharField(max_length=255)),
                ('Housing', models.CharField(max_length=255)),
                ('Additional_element_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infrastructure_development', to='Village_app.additionalelement')),
            ],
        ),
        migrations.CreateModel(
            name='LandUseZoning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Agriculturals', models.CharField(max_length=255)),
                ('Residential', models.CharField(max_length=255)),
                ('Commercial_industrial', models.CharField(max_length=255)),
                ('Additional_element_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='land_use_zoning', to='Village_app.additionalelement')),
            ],
        ),
        migrations.CreateModel(
            name='LocalBusinessEmployment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Small_business', models.CharField(max_length=255)),
                ('Job_opportunities', models.CharField(max_length=255)),
                ('Skill_development_center', models.CharField(max_length=255)),
                ('Additional_element_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='local_business_employment', to='Village_app.additionalelement')),
            ],
        ),
        migrations.CreateModel(
            name='market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details_local_market', models.TextField()),
                ('Availibality_essential_goods', models.CharField(max_length=255)),
                ('community_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='market', to='Village_app.communityservices')),
            ],
        ),
        migrations.CreateModel(
            name='PublicServicesContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contact_water_supply', models.CharField(max_length=255)),
                ('Contact_electricity', models.CharField(max_length=255)),
                ('Contact_gas_supply', models.CharField(max_length=255)),
                ('Emergency_helpline', models.CharField(max_length=255)),
                ('Additional_element_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='public_services_contact', to='Village_app.additionalelement')),
            ],
        ),
        migrations.CreateModel(
            name='Recreational_facilites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parks_playground', models.CharField(max_length=255)),
                ('community_center', models.CharField(max_length=255)),
                ('sport_facilities', models.CharField(max_length=255)),
                ('community_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recreational_facilities', to='Village_app.communityservices')),
            ],
        ),
        migrations.CreateModel(
            name='NaturalLandmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rivers', models.CharField(max_length=255)),
                ('lakes', models.CharField(max_length=255)),
                ('mountains', models.CharField(max_length=255)),
                ('forest', models.CharField(max_length=255)),
                ('tourist_attraction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='natural_landmark', to='Village_app.touristattraction')),
            ],
        ),
        migrations.CreateModel(
            name='LocalEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('festivals', models.CharField(max_length=255)),
                ('exhibitions', models.CharField(max_length=255)),
                ('cultural_performance', models.CharField(max_length=255)),
                ('tourist_attraction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='local_events', to='Village_app.touristattraction')),
            ],
        ),
        migrations.CreateModel(
            name='CulturalHistoricalPlaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temples', models.CharField(max_length=255)),
                ('old_building', models.CharField(max_length=255)),
                ('monuments', models.CharField(max_length=255)),
                ('museums', models.CharField(max_length=255)),
                ('tourist_attraction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cultural_places', to='Village_app.touristattraction')),
            ],
        ),
        migrations.CreateModel(
            name='Transportations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Buses', models.TextField()),
                ('Rickshaw', models.TextField()),
                ('Suzuki', models.TextField()),
                ('major_Road', models.CharField(max_length=255)),
                ('community_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transportations', to='Village_app.communityservices')),
            ],
        ),
        migrations.CreateModel(
            name='Uitilites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Water_supply', models.TextField()),
                ('Electricity', models.TextField()),
                ('Gas_supply', models.TextField()),
                ('Petrol_pump', models.TextField()),
                ('Internet_services', models.TextField()),
                ('Network', models.TextField()),
                ('community_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utilities', to='Village_app.communityservices')),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('village_id', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='villages', to='Citys_app.city')),
            ],
        ),
        migrations.AddField(
            model_name='touristattraction',
            name='Village_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TouristAttraction', to='Village_app.village'),
        ),
        migrations.CreateModel(
            name='SignificantPeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('biography', models.TextField()),
                ('contribution', models.TextField()),
                ('area_of_influence', models.CharField(max_length=255)),
                ('historic_period', models.CharField(max_length=255)),
                ('award_or_recognation', models.TextField()),
                ('related_events', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='significant_people', to='Citys_app.city')),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='significant_people', to='Village_app.village')),
            ],
        ),
        migrations.AddField(
            model_name='communityservices',
            name='village_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_services', to='Village_app.village'),
        ),
        migrations.AddField(
            model_name='additionalelement',
            name='Village_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Village_app.village'),
        ),
        migrations.CreateModel(
            name='VillageProfile',
            fields=[
                ('village_code', models.AutoField(primary_key=True, serialize=False)),
                ('village_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('population', models.IntegerField()),
                ('area', models.FloatField(help_text='Area in square kilometers')),
                ('elevation', models.FloatField(help_text='Elevation in meters')),
                ('climate', models.CharField(max_length=100)),
                ('primary_language', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('village_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='Village_app.village')),
            ],
        ),
    ]
