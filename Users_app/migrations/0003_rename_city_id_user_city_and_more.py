# Generated by Django 5.1.6 on 2025-03-19 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users_app', '0002_homefeed_user_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='city_id',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='district_id',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='division_id',
            new_name='division',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='province_id',
            new_name='province',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='village_id',
            new_name='village',
        ),
    ]
