import json

# Load the GeoJSON file
with open('ASSETS/50pts.geojson', 'r') as f:
    geojson_data = json.load(f)

# Initialize an empty list to store the project numbers
project_numbers = []

# Loop through each feature in the GeoJSON
for feature in geojson_data['features']:
    project_number = feature['properties'].get('Proyect Number')
    coordinates = feature['geometry']['coordinates']  # Get the coordinates
    if project_number:
        project_numbers.append({
            'project_number': project_number,
            'coordinates': coordinates
        })

# Save the project numbers and coordinates to a new JSON file
with open('ASSETS/project_numbers.json', 'w') as f:
    json.dump(project_numbers, f)
