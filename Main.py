import json

# Load the GeoJSON file
with open('ASSETS/50pts.geojson', 'r') as f:
    geojson_data = json.load(f)

# Initialize an empty list to store the project numbers
project_numbers = []

# Loop through each feature in the GeoJSON
for feature in geojson_data['features']:
    # Extract the "Proyect Number" from the properties and add it to the list
    project_number = feature['properties'].get('Proyect Number')
    if project_number:
        project_numbers.append(project_number)

# Print the list of project numbers
print(project_numbers)
