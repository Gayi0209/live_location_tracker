from django.urls import path
from . import views

# This app_name is important for the namespace="tracker" 
# you set in the main project's urls.py
app_name = 'tracker' 

urlpatterns = [
    # Serves home.html
    path('', views.home, name='home'), 
    
    # Serves dashboard.html
    path('dashboard/', views.dashboard, name='dashboard'), 
    
    # API endpoint for receiving location updates
    path('api/update/', views.update_location, name='update_location'),
    
    # API endpoint for fetching the latest locations
    path('api/locations/latest/', views.latest_locations_json, name='latest_locations_json'),
]