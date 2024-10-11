import json

# Load the GeoJSON file
with open('https://storage.googleapis.com/carolina_test/50pts.geojson', 'r') as f:
    geojson_data = json.load(f)

# Initialize an empty list to store the project numbers
project_numbers = []

# Loop through each feature in the GeoJSON
for feature in geojson_data['features']:
   # Extract relevant fields from the properties
    project_number = feature['properties'].get('Proyect Number')
    project_name = feature['properties'].get('Name', 'Unknown Project')
    project_description = feature['properties'].get('Description', 'No description available.')
    
    # Add the project info to the list
    if project_number:
        project_numbers.append({
            'project_number': project_number,
            'name': project_name,
            'description': project_description,
            'coordinates': feature['geometry']['coordinates']
        })
# Print the list of project numbers
print(project_numbers)
