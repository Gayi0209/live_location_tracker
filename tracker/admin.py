from django.contrib import admin
from .models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("username", "latitude", "longitude", "accuracy", "timestamp")
    list_filter = ("username",)
