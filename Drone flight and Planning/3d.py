import folium
from pythreejs import *

# Create a base map
m = folium.Map(location=[52.406822, -1.519692], zoom_start=12)  # Coventry city center

# Create a Three.js scene
scene = Scene()

# Add lights to the 3D scene
ambient_light = AmbientLight(color='white', intensity=0.5)
scene.add(ambient_light)

# Create a cube geometry
cube_geometry = BoxGeometry(width=1, height=1, depth=1)
cube_material = MeshLambertMaterial(color='blue')
cube_mesh = Mesh(geometry=cube_geometry, material=cube_material)
scene.add(cube_mesh)

# Define route coordinates (simplified for illustration)
route_coordinates = [
    [52.406822, -1.519692],  # Coventry city center
    [52.408181, -1.511123],  # Nearest Amazon warehouse (simplified coordinates)
]

# Create line geometry for the route
line_geometry = BufferGeometry(attributes={
    "position": BufferAttribute(array=route_coordinates, itemSize=3)
})
line_material = LineBasicMaterial(color='green')
route_line = Line(geometry=line_geometry, material=line_material)
scene.add(route_line)

# Create a camera
camera = PerspectiveCamera(position=[5, 5, 5], aspect=800/600)
controls = OrbitControls(controlling=camera)

# Create a WebGLRenderer
renderer = Renderer(scene=scene, camera=camera, width=800, height=600)

# Define animation function
def animate(time):
    cube_mesh.rotation.x += 0.01
    cube_mesh.rotation.y += 0.01
    renderer.render(scene, camera)
    m._repr_html_()  # Force map update
    renderer.animate(animate)

# Start animation loop
animate(0)

# Display the 3D scene on the map
html = m.get_root().render()
iframe = folium.IFrame(html=html, width=800, height=600)
popup = folium.Popup(iframe, max_width=800)
folium.Marker([52.406822, -1.519692], popup=popup).add_to(m)  # Add marker at Coventry city center

# Save the map
m.save('route_3d_overlay_map.html')
