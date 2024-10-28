import folium
import time
from IPython.display import display, HTML
import ipywidgets as widgets

# Simulated flight control systems and drone API functions
def initialize_flight_controller():
    print("Initializing flight controller...")

def take_off():
    print("Drone taking off...")
    # Send command to the flight controller or drone API to initiate takeoff

def fly_to(destination):
    print(f"Flying to {destination}...")
    # Send command to the flight controller or drone API to fly to the specified destination

def capture_landmarks():
    print("Capturing aerial views of Coventry landmarks...")
    # Use the drone's camera or imaging system to capture images or video

def land():
    print("Drone landing at the warehouse.")
    # Send command to the flight controller or drone API to initiate landing

# Main program
initialize_flight_controller()
take_off()
fly_to("Coventry city center")
capture_landmarks()
fly_to("the nearby warehouse")
land()

# Simulated flight time
def simulate_flight_time(duration):
    print(f"Simulating flight for {duration} seconds...")
    time.sleep(duration)

flight_duration = 10  # Simulated flight time in seconds
simulate_flight_time(flight_duration)

# Overlay on Map
coventry_coordinates = (52.4068, -1.5197)  # Coventry's latitude and longitude
map_center = coventry_coordinates
zoom_level = 13

# Create a folium map centered around Coventry
coventry_map = folium.Map(location=map_center, zoom_start=zoom_level)

# Add markers for the hospital, city center, and warehouse
hospital_coordinates = (52.4063, -1.5075) #coordinates
hospital_marker = folium.Marker(coventry_coordinates, popup="Coventry University Hospital")
city_center_coordinates = (52.4081, -1.5106)  # Coordinates for Coventry city center
city_center_marker = folium.Marker(city_center_coordinates, popup="Coventry City Center")
warehouse_coordinates = (52.44906, -1.4499)  # Coordinates for the warehouse
warehouse_marker = folium.Marker(warehouse_coordinates, popup="Nearby Warehouse")

hospital_marker.add_to(coventry_map)
city_center_marker.add_to(coventry_map)
warehouse_marker.add_to(coventry_map)

# Draw a line between the markers to represent the drone overlay route
overlay_route = folium.PolyLine(locations=[hospital_marker.location, city_center_marker.location, warehouse_marker.location],
                            color='blue',
                            weight=2,
                            opacity=0.8)
overlay_route.add_to(coventry_map)

# Create a drone marker
drone_marker = folium.Marker(coventry_coordinates, icon=folium.Icon(color='red', icon='plane'), popup="Drone")

# Function to update the drone's position on the map
def update_drone_position(lat, lon):
    drone_marker.location = [lat, lon]

# Simulate motion by updating the drone's position at regular intervals
movement_duration = 10  # Duration of each movement step in seconds

# Simulated drone's movement path
drone_movement_path = [
    (52.4063, -1.5075),  # Starting position (hospital)
    (52.4081, -1.5106),  # City center position
    (52.44906, -1.4499)   # Warehouse position
]

# Function to update the drone's position on the map
def update_drone_position(lat, lon):
    drone_marker.location = [lat, lon]
    coventry_map.add_child(drone_marker)
    display(coventry_map)

# Simulated drone's movement path
drone_movement_path = [
    (52.4081, -1.5106),  # Starting position (city center)
    (52.4063, -1.5197)   # Coventry hospital position
]

def play_button_clicked(b):
    for position in drone_movement_path:
        update_drone_position(position[0], position[1])
        time.sleep(movement_duration)
        coventry_map.save("coventry_drone_overlay.html")  # Save the map after each update

# Create a play button
play_button = widgets.Button(description='Play')

# Assign the play_button_clicked function to the button's on_click event
play_button.on_click(play_button_clicked)

# Display the play button
display(play_button)

# Add the drone marker to the map
drone_marker.add_to(coventry_map)

# Save the map as an HTML file
coventry_map.save("coventry_drone_overlay.html")

print("Drone overlay map created successfully!")
