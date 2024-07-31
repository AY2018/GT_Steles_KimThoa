import os
import json


directory = 'new_annotations'

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        filepath = os.path.join(directory, filename)
    
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
            original_filename = data['images'][0]['file_name']
        
            new_filename = os.path.splitext(original_filename)[0] + '.json'
        
            new_filepath = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(filepath, new_filepath)
            print(f'Renamed: {filename} -> {new_filename}')
