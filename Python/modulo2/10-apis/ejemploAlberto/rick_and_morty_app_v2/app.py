import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import os
from dotenv import load_dotenv

# Configuración de la página
st.set_page_config(page_title="Rick & Morty Analytics", layout="wide")

# Cargar variables de entorno
load_dotenv()
CHARACTER_API_URL = "https://rickandmortyapi.com/api/character"
EPISODE_API_URL = "https://rickandmortyapi.com/api/episode"

# if not CHARACTER_API_URL or not EPISODE_API_URL:
#     st.error("No se encontraron las URLs de la API en el archivo .env")
#     st.stop()

# Funciones auxiliares
def fetch_data_from_api(url):
    """
    Realiza una solicitud GET a una API y devuelve los datos en formato JSON si la solicitud es exitosa.
    Args:
        url (str): URL de la API.
    Returns:
        dict: Datos JSON de la respuesta de la API.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error para códigos de estado HTTP 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error al conectarse a la API: {e}")
        return None

# Funciones principales
def obtener_todos_los_personajes():
    """
    Realiza solicitudes a la API para obtener todos los personajes.
    Returns:
        list: Lista de personajes.
    """
    personajes = []
    url = CHARACTER_API_URL
    while url:
        data = fetch_data_from_api(url)
        if data and "results" in data:
            personajes.extend(data["results"])
            url = data["info"].get("next", None)
        else:
            st.error("Error en el formato de los datos recibidos de la API de personajes.")
            break
    return personajes

def obtener_todos_los_episodios():
    """
    Realiza solicitudes a la API para obtener todos los episodios.
    Returns:
        list: Lista de episodios.
    """
    episodios = []
    url = EPISODE_API_URL
    while url:
        data = fetch_data_from_api(url)
        if data and "results" in data:
            episodios.extend(data["results"])
            url = data["info"].get("next", None)
        else:
            st.error("Error en el formato de los datos recibidos de la API de episodios.")
            break
    return episodios

# Obtener los datos
@st.cache_data
def cargar_datos():
    """
    Carga y estructura los datos de personajes y episodios.
    Returns:
        tuple: DataFrames de personajes y episodios.
    """
    personajes = obtener_todos_los_personajes()
    episodios = obtener_todos_los_episodios()

    if not personajes or not episodios:
        st.error("No se pudieron cargar los datos de la API.")
        st.stop()

    # Convertir a DataFrames
    df_personajes = pd.DataFrame(personajes)
    df_episodios = pd.DataFrame(episodios)

    # Procesar columnas relevantes
    df_personajes["num_episodios"] = df_personajes["episode"].apply(len)

    return df_personajes, df_episodios

# Cargar los datos
df_personajes, df_episodios = cargar_datos()

# Configurar la página
st.title("Rick & Morty API Analytics")
st.markdown("Explora estadísticas clave sobre los personajes y episodios de la serie Rick & Morty.")

# Sección 1: Big Numbers (Personajes vivos vs muertos)
st.header("Personajes Vivos vs. Muertos")
col1, col2, col3 = st.columns(3)

# Contar personajes por estado
estado_counts = df_personajes["status"].value_counts().reset_index()
estado_counts.columns = ["Estado", "Cantidad"]

# Mostrar Big Numbers
vivos = estado_counts.loc[estado_counts["Estado"] == "Alive", "Cantidad"].sum()
muertos = estado_counts.loc[estado_counts["Estado"] == "Dead", "Cantidad"].sum()
desconocidos = estado_counts.loc[estado_counts["Estado"] == "unknown", "Cantidad"].sum()

col1.metric("Vivos", vivos)
col2.metric("Muertos", muertos)
col3.metric("Estado Desconocido", desconocidos)

# Gráfico de barra
fig_estado = px.bar(
    estado_counts,
    x="Estado",
    y="Cantidad",
    labels={"Estado": "Estado", "Cantidad": "Cantidad"},
    title="Distribución de Personajes por Estado",
    text="Cantidad",
    color="Estado",
)
fig_estado.update_traces(textposition="outside")
st.plotly_chart(fig_estado)

# Sección 2: Personajes más frecuentes en episodios
st.header("Personajes con Más Apariciones en Episodios")
top_personajes = df_personajes[["name", "num_episodios"]].sort_values(by="num_episodios", ascending=False).head(10)

# Mostrar tabla de los más frecuentes
st.subheader("Top 10 Personajes con Más Apariciones")
st.table(top_personajes)

# Gráfico de barra horizontal
fig_top_personajes = px.bar(
    top_personajes,
    x="num_episodios",
    y="name",
    orientation="h",
    labels={"name": "Personaje", "num_episodios": "Número de Episodios"},
    title="Personajes con Más Apariciones",
    text="num_episodios",
    color="name",
)
fig_top_personajes.update_traces(textposition="outside")
st.plotly_chart(fig_top_personajes)

# Sección 3: Análisis de episodios
st.header("Episodios y Participación de Personajes")
num_episodios = len(df_episodios)
personajes_por_episodio = df_episodios["characters"].apply(len)

st.metric("Total de Episodios", num_episodios)
st.metric("Promedio de Personajes por Episodio", round(personajes_por_episodio.mean(), 2))

# Gráfico de densidad
fig_densidad = px.histogram(
    personajes_por_episodio,
    nbins=20,
    labels={"value": "Cantidad de Personajes"},
    title="Distribución de Personajes por Episodio",
)
st.plotly_chart(fig_densidad)

# Pie de página
st.markdown("---")
st.markdown("Aplicación desarrollada con ❤️ usando Streamlit, Python y la API de Rick & Morty.")
