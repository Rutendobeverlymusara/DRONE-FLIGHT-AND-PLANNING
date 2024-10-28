import folium
from geopy.geocoders import Nominatim

# Define the center coordinates of Coventry
coventry_coords = (52.4068, -1.5197)

# Initialize the map
coventry_map = folium.Map(location=coventry_coords, zoom_start=13)

# Create a geocoder object
geolocator = Nominatim(user_agent="coventry_drone_map")

# Function to geocode an address and add a marker to the map
def add_marker(address):
    location = geolocator.geocode(address)
    if location:
        marker = folium.Marker(location=[location.latitude, location.longitude], popup=address)
        marker.add_to(coventry_map)

# Warehouse addresses in Coventry
warehouses = [
    "Unit 1, Example Road, Coventry",
    "Warehouse Lane, Coventry",
    "New Industrial Estate, Coventry",
    "Commercial Park, Coventry"
]

# Add markers for the warehouses
for warehouse in warehouses:
    add_marker(warehouse)

# Define the drone icon image
drone_icon = folium.features.CustomIcon(icon_image='drone_icon.png', icon_size=(50, 50))

# Add a custom drone marker to the map
drone_marker = folium.Marker(location=(52.4099, -1.5032), popup="Drone", icon=drone_icon)
drone_marker.add_to(coventry_map)

# Save the map to an HTML file
coventry_map.save("coventry_map.html")
