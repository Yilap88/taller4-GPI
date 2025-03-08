## Este código simula el precio de la energía, el precio del gas y el nivel de los embalses.

## En caso de requerirse instalaremos pandas y numpy con el comando "pip install pandas" y "pip install numpy" respectivamente desde la consola

### Llamamos los paquete a usar
import pandas as pd
import numpy as np
import os #paquete nativo de python

### Simulamos 3 variables, Precio energía (P_energia), Precio Gas natural (P_gas) y Nivel de embalses (Embalses)

np.random.seed(0)  # Para que los resultados sean reproducibles
P_energia = np.random.rand(100)*1000  # 100 valores aleatorios entre 0 y 1, luego multiplicados por 1000 para dar la ilusión de que se habla del precio de la energía en una escala de COP/kWh
P_gas = np.random.rand(100)*5  # 100 valores aleatorios entre 0 y 1, luego multiplicados por 5 para dar la ilusión de que se habla del precio del gas natural en una escala de USD/MBTU
P_carbon = np.random.rand(100)*120  # 100 valores aleatorios entre 0 y 1, luego multiplicados por 120 para dar la ilusión de que se habla del precio de la tonelada de carbon en una escala de USD/ton
P_petroleo = np.random.rand(100)*90  # 100 valores aleatorios entre 0 y 1, luego multiplicados por 90 para dar la ilusión de que se habla del precio del petróleo en una escala de USD/barril
embalses = np.random.rand(100)*100 # 100 valores aleatorios entre 0 y 1, luego multiplicados por 100 para dar la ilusión de que se habla del porcentaje de nivel de los embalses en una escala de USD/MBTU


### Crear un DataFrame con las dos variables
dfdatosenergia = pd.DataFrame({
    'P_energia': P_energia,
    'P_gas': P_gas,
    'P_carbon': P_carbon,
    'P_petroleo': P_petroleo,
    'embalses': embalses
})

## Finalmente guardamos el dataframe en formato CSV

### Obtenemos el directorio actual
ruta_script = os.path.abspath(__file__)  # Ruta completa del script
directorio_actual = os.path.dirname(ruta_script)  # Solo el directorio
directorio_superior = os.path.dirname(directorio_actual) # subimos un directorio
os.chdir(directorio_superior) # Establecemos /proyecto_investigacion/ como ruta de trabajo


### Definimos el nombre del archivo
datos = "data/processed/datos.csv"

### Guardar el DataFrame en el directorio actual
dfdatosenergia.to_csv(datos, index=False)
