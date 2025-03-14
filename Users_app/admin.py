from django.contrib import admin
from .models import UserProfile,HomeFeed,Comment,User,VillageUpdateRequest

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(HomeFeed)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(VillageUpdateRequest)

