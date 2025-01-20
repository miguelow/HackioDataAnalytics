import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
API_URL = os.getenv("RICK_MORTY_API_URL")

if not API_URL:
    st.error("No se encontró la URL de la API en el archivo .env")
    st.stop()

# Función para obtener personajes
def obtener_personajes(nombre=None, estado=None, especie=None):
    """
    Realiza una solicitud a la API para obtener personajes filtrados.
    Args:
        nombre (str): Nombre del personaje (opcional).
        estado (str): Estado del personaje (opcional).
        especie (str): Especie del personaje (opcional).
    Returns:
        list: Lista de personajes que coinciden con los filtros.
    """
    params = {}
    if nombre:
        params["name"] = nombre
    if estado:
        params["status"] = estado
    if especie:
        params["species"] = especie

    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        st.error(f"Error al realizar la solicitud: {response.status_code}")
        return []

# Función para mostrar personajes
def mostrar_personajes(personajes):
    """
    Muestra una lista de personajes con su información básica.
    Args:
        personajes (list): Lista de personajes.
    """
    for personaje in personajes:
        st.subheader(personaje["name"])
        st.write(f"**Estado:** {personaje['status']}")
        st.write(f"**Especie:** {personaje['species']}")
        st.write(f"**Género:** {personaje['gender']}")
        st.write(f"**Origen:** {personaje['origin']['name']}")
        st.write(f"**Ubicación actual:** {personaje['location']['name']}")
        st.image(personaje["image"], caption=f"Imagen de {personaje['name']}")
        st.markdown("---")

# Configuración de la interfaz
st.title("Rick & Morty API Explorer")
st.markdown("Interfaz para explorar personajes de la serie Rick & Morty utilizando su API oficial.")

# Filtros de búsqueda
with st.sidebar:
    st.header("Filtros de Búsqueda")
    nombre = st.text_input("Nombre del personaje", "")
    estado = st.selectbox("Estado", ["", "Alive", "Dead", "unknown"])
    especie = st.text_input("Especie", "")

# Botón para realizar la búsqueda
if st.button("Buscar personajes"):
    st.markdown("### Resultados de la búsqueda:")
    personajes = obtener_personajes(nombre=nombre, estado=estado, especie=especie)
    if personajes:
        mostrar_personajes(personajes)
    else:
        st.warning("No se encontraron personajes que coincidan con los filtros.")

# Pie de página
st.markdown("---")
st.markdown("Aplicación desarrollada con ❤️ usando Streamlit y la API de Rick & Morty.")
