import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener la URL base desde el archivo .env
API_URL = os.getenv("API_URL_POKE")

if not API_URL:
    raise ValueError("API_URL no está definido en el archivo .env")

def obtener_pokemon(nombre):
    """
    Realiza una solicitud a la API para obtener información de un Pokémon.
    Args:
        nombre (str): Nombre del Pokémon a buscar.
    Returns:
        dict: Información JSON del Pokémon o un mensaje de error.
    """
    url = f"{API_URL}/{nombre.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return {"Error": f"El Pokémon '{nombre}' no fue encontrado."}
    else:
        return {"Error": f"Error en la solicitud: {response.status_code}"}

# Probar con un Pokémon
if __name__ == "__main__":
    pokemon = input("Introduce el nombre de un Pokémon: ")
    datos = obtener_pokemon(pokemon)
    print(datos)
def transformar_datos_pokemon(datos):
    """
    Transforma los datos crudos de la API en un diccionario organizado.
    Args:
        datos (dict): Datos JSON obtenidos de la API.
    Returns:
        dict: Diccionario con datos clave del Pokémon.
    """
    if "Error" in datos:
        return datos

    # Extraer información relevante
    return {
        "Nombre": datos.get("name", "").capitalize(),
        "Altura": datos.get("height", 0),
        "Peso": datos.get("weight", 0),
        "Tipos": [tipo["type"]["name"].capitalize() for tipo in datos.get("types", [])],
        "Habilidades": [habilidad["ability"]["name"].capitalize() for habilidad in datos.get("abilities", [])],
        "Estadísticas": {stat["stat"]["name"]: stat["base_stat"] for stat in datos.get("stats", [])}
    }

# Integrar las funciones
if __name__ == "__main__":
    pokemon = input("Introduce el nombre de un Pokémon: ")
    datos_crudos = obtener_pokemon(pokemon)
    datos_transformados = transformar_datos_pokemon(datos_crudos)

    if "Error" in datos_transformados:
        print(datos_transformados["Error"])
    else:
        print("Información del Pokémon:")
        for clave, valor in datos_transformados.items():
            print(f"{clave}: {valor}")
import json

def guardar_datos_en_archivo(datos, nombre_archivo="pokemon_data.json"):
    """
    Guarda los datos en un archivo JSON.
    Args:
        datos (dict): Diccionario con los datos a guardar.
        nombre_archivo (str): Nombre del archivo.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)
    print(f"Datos guardados en {nombre_archivo}")

# Integrar la función
if __name__ == "__main__":
    pokemon = input("Introduce el nombre de un Pokémon: ")
    datos_crudos = obtener_pokemon(pokemon)
    datos_transformados = transformar_datos_pokemon(datos_crudos)

    if "Error" in datos_transformados:
        print(datos_transformados["Error"])
    else:
        guardar_datos_en_archivo(datos_transformados)