# Import_data_Zenodo.py
#
# Objetivo: Descargar los datos simulados del taller 4 de GPICA directamente de Zenodo


# Paso 1: Cargamos librerías
# requests: Para manejar URL de internet
# json: para leer y generar archivos .json
# pandas: Para manejar dataset tabular
# os: Para trabajar con directorios locales
import requests
import json
import pandas as pd
import os
from pathlib import Path
 
# Paso 2: Configuramos direcciones URL del API del repositorio Zenodo
zenodo_api = "https://zenodo.org/api/records/"  # La URL base
zenodo_id = "15029998"  # El id de la base de datos
api_url = zenodo_api + zenodo_id  # Contatenamos para crear la URL completa
 
print(f"Preparandose para descargar datos desde: {api_url}")
 
# Step 3
### Obtenemos el directorio actual (directorio dinámico)
ruta_script = os.path.abspath(__file__)  # Ruta completa del script
directorio_actual = os.path.dirname(ruta_script)  # Solo el directorio
directorio_superior = os.path.dirname(directorio_actual) # subimos un directorio
os.chdir(directorio_superior) # Establecemos /proyecto_investigacion/ como ruta de trabajo

# Desde el directorio base definimos donde alojar nuestros datos y metadata descargada, si el directorio no existe, se crea
directorio_datos = "data/processed/"
if not os.path.exists(directorio_datos):
    os.makedirs(directorio_datos)
    print(f"Directorio creado: {directorio_datos}")


 
# Step 4: Download the metadata (information about the files)
# This tells us what files are available and where to get them
print("Descargando metadata...")
response = requests.get(api_url)
 
# Check if the download was successful
if response.status_code == 200:  # 200 means "OK" in HTTP
    print("Descarga Exitosa de metadata")
    
    # Save the metadata as a JSON file for reference
    metadata_file = os.path.join(directorio_datos, "metadata.json")
    with open(metadata_file, 'w') as f:
        f.write(response.text)
    
    # Parse the JSON data
    metadata = json.loads(response.text)
    
    # Step 5: Extract the download URL for the actual data file
    # We're looking for the file URL within the metadata
    if 'files' in metadata and len(metadata['files']) > 0:
        # Get the download link for the first file (assuming it's our data)
        file_url = metadata['files'][0]['links']['self']
        
        print(f"Datos encontrados en: {file_url}")
        
        # Step 6: Download the actual data file
        print("Descargando datos...")
        data_response = requests.get(file_url)
        
        if data_response.status_code == 200:
            # Save the downloaded file
            data_file = os.path.join(directorio_datos, "datos.csv")
            with open(data_file, 'wb') as f:
                f.write(data_response.content)
            
            print(f"Datos guardados en: {data_file}")
                   
            print("\nAdquisición de datos completa y listo para análisis")
        else:
            print(f"Error descargando los datos. Status code: {data_response.status_code}")
    else:
        print("Archivos no encontrados en la metadata")
else:
    print(f"Error de descarga de la metadata. Status code: {response.status_code}")