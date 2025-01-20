import requests
import os
import json
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener la URL base desde el archivo .env
API_URL = os.getenv("RICK_MORTY_API_URL")

if not API_URL:
    raise ValueError("RICK_MORTY_API_URL no está definido en el archivo .env")

def obtener_personaje(nombre):
    """
    Realiza una solicitud para buscar personajes por nombre.
    Args:
        nombre (str): Nombre del personaje a buscar.
    Returns:
        list: Lista de personajes que coinciden con el nombre.
    """
    params = {"name": nombre}
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        return response.json().get("results", [])
    elif response.status_code == 404:
        return {"Error": f"No se encontraron personajes con el nombre '{nombre}'."}
    else:
        return {"Error": f"Error en la solicitud: {response.status_code}"}

# Probar con un personaje
if __name__ == "__main__":
    personaje = input("Introduce el nombre de un personaje: ")
    resultados = obtener_personaje(personaje)
    print(resultados)

def transformar_datos_personaje(datos):
    """
    Transforma los datos de la API en un diccionario organizado.
    Args:
        datos (list): Lista de personajes obtenidos de la API.
    Returns:
        list: Lista de diccionarios con información clave.
    """
    if isinstance(datos, dict) and "Error" in datos:
        return datos

    personajes_transformados = []
    for personaje in datos:
        personajes_transformados.append({
            "Nombre": personaje.get("name"),
            "Estado": personaje.get("status"),
            "Especie": personaje.get("species"),
            "Género": personaje.get("gender"),
            "Origen": personaje.get("origin", {}).get("name"),
            "Ubicación Actual": personaje.get("location", {}).get("name")
        })
    return personajes_transformados

# Probar la transformación
if __name__ == "__main__":
    personaje = input("Introduce el nombre de un personaje: ")
    resultados = obtener_personaje(personaje)
    datos_transformados = transformar_datos_personaje(resultados)

    if isinstance(datos_transformados, dict) and "Error" in datos_transformados:
        print(datos_transformados["Error"])
    else:
        print("Información de los personajes:")
        for p in datos_transformados:
            print(p)

def guardar_datos_personajes(datos, nombre_archivo="personajes_rick_and_morty.json"):
    """
    Guarda la lista de personajes en un archivo JSON.
    Args:
        datos (list): Lista de diccionarios con información de los personajes.
        nombre_archivo (str): Nombre del archivo.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)
    print(f"Datos guardados en {nombre_archivo}")

# Integrar las funciones
if __name__ == "__main__":
    personaje = input("Introduce el nombre de un personaje: ")
    resultados = obtener_personaje(personaje)
    datos_transformados = transformar_datos_personaje(resultados)

    if isinstance(datos_transformados, dict) and "Error" in datos_transformados:
        print(datos_transformados["Error"])
    else:
        guardar_datos_personajes(datos_transformados)

def obtener_episodios(episodios):
    """
    Realiza solicitudes para obtener información sobre episodios.
    Args:
        episodios (list): Lista de URLs de episodios.
    Returns:
        list: Lista de nombres de episodios.
    """
    episodios_info = []
    for url in episodios:
        response = requests.get(url)
        if response.status_code == 200:
            episodios_info.append(response.json().get("name"))
    return episodios_info

# Integrar con el flujo principal
if __name__ == "__main__":
    personaje = input("Introduce el nombre de un personaje: ")
    resultados = obtener_personaje(personaje)
    datos_transformados = transformar_datos_personaje(resultados)

    if isinstance(datos_transformados, dict) and "Error" in datos_transformados:
        print(datos_transformados["Error"])
    else:
        for personaje in datos_transformados:
            print(f"Nombre: {personaje['Nombre']}")
            episodios = [resultados[0].get("episode", [])]
            episodios_info = obtener_episodios(episodios)
            print("Episodios:", ", ".join(episodios_info))
