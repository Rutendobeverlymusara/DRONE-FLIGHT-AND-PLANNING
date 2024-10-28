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

# Sample addresses to add as markers
addresses = [
    "University of Warwick, Coventry",
    "Coventry Cathedral, Coventry",
    "War Memorial Park, Coventry"
]

# Add markers for the addresses
for address in addresses:
    add_marker(address)

# Define the data for the color-coded overlay
data = {
    "Location 1": 25,
    "Location 2": 50,
    "Location 3": 75,
    "Location 4": 100
}

# Define a color scheme for the overlay
color_scheme = {
    "Location 1": "green",
    "Location 2": "yellow",
    "Location 3": "orange",
    "Location 4": "red"
}

# Add the color-coded overlay to the map
for location, value in data.items():
    location_coords = geolocator.geocode(location)
    if location_coords:
        folium.CircleMarker(
            location=[location_coords.latitude, location_coords.longitude],
            radius=10,
            color=color_scheme.get(location, "blue"),
            fill=True,
            fill_color=color_scheme.get(location, "blue"),
            fill_opacity=0.7,
            popup=f"Location: {location}<br>Value: {value}"
        ).add_to(coventry_map)

# Save the map to an HTML file
coventry_map.save("coventry_map.html")
