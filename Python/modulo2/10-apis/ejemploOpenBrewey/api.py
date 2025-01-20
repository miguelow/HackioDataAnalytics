# Importar librerías necesarias
import pandas as pd
import numpy as np
import requests
from tqdm import tqdm
from time import sleep
import os
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()
base_url = os.getenv("API_KEY")
# API_KEY=https://api.openbrewerydb.org/v1/breweries

# Verificar la clave API
if not base_url:
    raise ValueError("La clave API no se encuentra en el archivo .env")

# Función para manejar llamadas a la API con manejo de errores 
def llamada_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si el código de estado no es 200
        print(response.json())
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")
    except requests.exceptions.ConnectionError as err:
        print(f"Error de conexión: {err}")
    except requests.exceptions.Timeout as err:
        print(f"Timeout error: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error en la solicitud: {err}")
    return None

# Función para limpiar datos
def limpieza_datos(datos, campos):
    diccionario = {clave: [] for clave in campos.values()}
    for elemento in datos:
        for campo_api, campo_local in campos.items():
            try:
                diccionario[campo_local].append(elemento[campo_api])
            except KeyError:
                diccionario[campo_local].append(np.nan)
    return pd.DataFrame(diccionario)

# Campos que nos interesan
campos_interes = {
    "name": "nombre",
    "brewery_type": "tipo",
    "city": "ciudad",
    "state": "estado",
    "street": "direccion"
}

# Ejemplo: Llamada a la API para obtener todas las cervecerías
print("Haciendo llamada a la API para todas las cervecerías...")
if __name__ == "__main__":
    datos_todas = llamada_api(base_url)

if datos_todas:
    print("Transformando datos...")
    df_todas = limpieza_datos(datos_todas, campos_interes)
    print("Ejemplo de datos transformados:")
    print(df_todas.head())

# Ejemplo: Consultar cervecerías por estado de forma escalable
estados = ["california", "florida", "texas"]
df_final = pd.DataFrame()

print("Obteniendo datos por estado...")
for estado in tqdm(estados, desc="Procesando estados"):
    url_estado = f"{base_url}?by_state={estado}&per_page=5"
    datos_estado = llamada_api(url_estado)
    if datos_estado:
        df_estado = limpieza_datos(datos_estado, campos_interes)
        df_final = pd.concat([df_final, df_estado], ignore_index=True)

print("Ejemplo de datos combinados:")
print(df_final.sample(5))

# Guardar el resultado en un archivo CSV
df_final.to_csv("cervecerias_por_estado.csv", index=False)
print("Datos guardados en 'cervecerias_por_estado.csv'.")
