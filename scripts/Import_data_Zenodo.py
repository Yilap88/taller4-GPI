# zenodo_data_acquisition.py
#
# Purpose: Download data directly from Zenodo repositories
# This script demonstrates how to automate data acquisition for research reproducibility
 

# Step 1: Import the necessary libraries
# requests: For downloading files from the internet
# json: For parsing JSON data (metadata)
# pandas: For working with tabular data
# os: For file path operations
import requests
import json
import pandas as pd
import os
from pathlib import Path
 
# Step 2: Set up information about the Zenodo repository
# This is like providing the "address" of where our data lives online
zenodo_api = "https://zenodo.org/api/records/"  # The base API URL
zenodo_id = "15029998"  # The specific ID for our dataset
api_url = zenodo_api + zenodo_id  # The complete URL to access our data
 
print(f"Preparing to download data from: {api_url}")
 
# Step 3A
### Obtenemos el directorio actual
ruta_script = os.path.abspath(__file__)  # Ruta completa del script
directorio_actual = os.path.dirname(ruta_script)  # Solo el directorio
directorio_superior = os.path.dirname(directorio_actual) # subimos un directorio
os.chdir(directorio_superior) # Establecemos /proyecto_investigacion/ como ruta de trabajo

# Step 3: Create a temporary folder to store our files
# It's good practice to organize where downloaded files will go
temp_folder = "data/processed/"
if not os.path.exists(temp_folder):
    os.makedirs(temp_folder)
    print(f"Created temporary folder: {temp_folder}")


 
# Step 4: Download the metadata (information about the files)
# This tells us what files are available and where to get them
print("Downloading metadata...")
response = requests.get(api_url)
 
# Check if the download was successful
if response.status_code == 200:  # 200 means "OK" in HTTP
    print("Successfully downloaded metadata")
    
    # Save the metadata as a JSON file for reference
    metadata_file = os.path.join(temp_folder, "metadata.json")
    with open(metadata_file, 'w') as f:
        f.write(response.text)
    
    # Parse the JSON data
    metadata = json.loads(response.text)
    
    # Step 5: Extract the download URL for the actual data file
    # We're looking for the file URL within the metadata
    if 'files' in metadata and len(metadata['files']) > 0:
        # Get the download link for the first file (assuming it's our data)
        file_url = metadata['files'][0]['links']['self']
        
        print(f"Found data file at: {file_url}")
        
        # Step 6: Download the actual data file
        print("Downloading data file...")
        data_response = requests.get(file_url)
        
        if data_response.status_code == 200:
            # Save the downloaded file
            data_file = os.path.join(temp_folder, "datos.csv")
            with open(data_file, 'wb') as f:
                f.write(data_response.content)
            
            print(f"Data saved to: {data_file}")
            
            # Step 7: Load the data into a pandas DataFrame for analysis
            print("Loading data for analysis...")
            survey_data = pd.read_csv(data_file)
            
            # Step 8: Clean column names (convert to lowercase, replace spaces with underscores)
            survey_data.columns = [col.lower().replace(' ', '_') for col in survey_data.columns]
            
            # Display information about the data
            print("\nData summary:")
            print(f"Number of rows: {len(survey_data)}")
            print(f"Number of columns: {len(survey_data.columns)}")
            print("First few column names:", list(survey_data.columns)[:5])
            
            # Display the first few rows of data
            print("\nPreview of data:")
            print(survey_data.head())
            
            print("\nData acquisition complete and ready for analysis!")
        else:
            print(f"Error downloading data file. Status code: {data_response.status_code}")
    else:
        print("No files found in the metadata")
else:
    print(f"Error downloading metadata. Status code: {response.status_code}")