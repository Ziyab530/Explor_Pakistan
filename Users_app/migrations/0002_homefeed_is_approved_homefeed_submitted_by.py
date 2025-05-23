# Generated by Django 5.1.6 on 2025-05-02 14:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homefeed',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='homefeed',
            name='submitted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submitted_home_feeds', to=settings.AUTH_USER_MODEL),
        ),
    ]
