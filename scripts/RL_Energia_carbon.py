## Este código realiza una predicción usando una regresión lineal.

## En caso de requerirse instalaremos los paquetes con los comandos "pip install matplotlib", "pip install scikit-learn", "pip install pandas" y "pip install numpy" respectivamente desde la consola

### IMPORTAMOS LOS PAQUETES A USAR
import pandas as pd
import numpy as np
import os #paquete nativo de python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt



### CARGAMOS LA BASE DE DATOS - HACEMOS LOS DIRECTORIOS DINÁMICOS
ruta_script = os.path.abspath(__file__)  # Ruta completa del script
directorio_actual = os.path.dirname(ruta_script)  # Solo el directorio donde está ubicado el script
directorio_superior = os.path.dirname(directorio_actual) # subimos un directorio
os.chdir(directorio_superior) # Establecemos /proyecto_investigacion/ como ruta de trabajo
dforiginal = pd.read_csv('data/processed/datos.csv') # Como ya estamos en el directorio donde tenemos los datos en formato csv los cargamos a un dataframe
# Filtrar solo las columnas 'Edad' y 'Salario'
df = dforiginal[['P_energia', 'P_carbon']]



# REALIZAR REGRESIÓN LINEAL ENTRE EL PAR DE VARIABLES
### Definir las variables predictoras (X) y la variable dependiente (Y)
X = df[['P_carbon']]  # Variables predictoras
y = df['P_energia']  # Variable dependiente

### Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

### Crear el modelo de regresión lineal
modelo = LinearRegression()# Entrenar el modelo
modelo.fit(X_train, y_train)

### Realizar predicciones con el conjunto de prueba
predicciones = modelo.predict(X_test)

### Mostrar las predicciones
print("Predicciones:", predicciones)




# CREAMOS GRÁFICO
# Graficar los datos originales
plt.scatter(X, y, color='yellow', label='Datos reales')

# Graficar la recta de regresión
plt.plot(X_test, predicciones, color='red', label='Recta de regresión')

# Agregar etiquetas y título
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regresión Lineal Energía vs Precio del Carbon')

# Agregar leyenda
plt.legend()

# Guardar la grafica como un archivo .png
plt.savefig('results/figures/02_RL_Energia_carbon_grafica.png', format="png", bbox_inches="tight", dpi=300)

# Mostrar la imagen (opcional)
##plt.show()
######




# EVALUAR MODELO SEGÚN MSE Y MAE, y GUARDAR TABLA DE RESULTADOS
### Evaluar el modelo (MSE)
mse = mean_squared_error(y_test, predicciones)
mse = round(mse, 2)
print("Error cuadrático medio (MSE):", mse)

### Evaluar el modelo (MAE)
mae = mean_absolute_error(y_test, predicciones)
mae = round(mae, 2)
print("Error cuadrático medio (MAE):", mae)

#Creamos una tabla para mostrar el MSE y el MAE
resultadospred = pd.DataFrame({
    'Métrica': ['MSE', 'MAE'],
    'Valor': [mse, mae]
})

# Mostrar la tabla
print(resultadospred)

# Crear una figura y agregar una tabla a la figura
fig, ax = plt.subplots(figsize=(4, 4))  # Tamaño de la imagen (ancho, alto)
ax.axis('tight')
ax.axis('off')  # Desactiva los ejes

# Crear la tabla a partir del DataFrame
tabla = ax.table(cellText=resultadospred.values, colLabels=resultadospred.columns, loc='center', cellLoc='center', colColours=['lightgrey']*len(df.columns))

# Guardar la tabla como un archivo .png
plt.savefig('results/tables/02_RL_Energia_carbon_evaluacion.png', format="png", bbox_inches="tight", dpi=300)

# Mostrar la imagen (opcional)
#plt.show()