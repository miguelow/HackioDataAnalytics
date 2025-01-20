### **Guía Paso a Paso: Aplicación de Streamlit para Análisis de la API de Rick & Morty**

A continuación, te explico cómo configurar y entender cada sección del código para que puedas ejecutarlo y personalizarlo según tus necesidades.

---

### **1. Configuración del Entorno de Trabajo**

### **a. Crear un Entorno Virtual**

1. Crea un entorno virtual para aislar las dependencias del proyecto:
    
    ```bash
    python -m venv venv
    ```
    
2. Activa el entorno virtual:
    - **Windows**:
        
        ```bash
        venv\Scripts\activate
        ```
        
    - **macOS/Linux**:
        
        ```bash
        source venv/bin/activate
        ```
        

### **b. Instalar las Dependencias**

Dentro del entorno virtual, instala las bibliotecas necesarias:

```bash
pip install streamlit requests python-dotenv pandas plotly
```

### **c. Configurar Variables de Entorno**

1. En la raíz del proyecto, crea un archivo llamado `.env` con el siguiente contenido:
    
    ```
    RICK_MORTY_API_URL=https://rickandmortyapi.com/api/character
    ```
    
2. Asegúrate de que `.env` esté excluido del control de versiones añadiéndolo a `.gitignore`:
    
    ```
    .env
    venv/
    ```
    

---

### **2. Estructura del Proyecto**

Guarda el código proporcionado en un archivo llamado `app.py`. Tu estructura del proyecto debe lucir así:

```bash
rick_and_morty_app/
├── app.py             # Código principal de la aplicación
├── .env               # Variables de entorno
└── venv/              # Entorno virtual
```

---

### **3. Código Explicado Paso a Paso**

### **a. Configuración de Streamlit y Variables**

```python
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
CHARACTER_API_URL = os.getenv("RICK_MORTY_API_URL", "https://rickandmortyapi.com/api/character")
EPISODE_API_URL = "https://rickandmortyapi.com/api/episode"
```

- **`st.set_page_config`**: Configura el título y el diseño de la aplicación.
- **`load_dotenv`**: Carga las variables de entorno desde `.env`.
- **`os.getenv`**: Recupera las URLs de la API de las variables de entorno.

---

### **b. Función para Obtener Todos los Personajes**

```python
def obtener_todos_los_personajes():
    personajes = []
    url = CHARACTER_API_URL
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            personajes.extend(data["results"])
            url = data["info"]["next"]
        else:
            st.error(f"Error al obtener personajes: {response.status_code}")
            break
    return personajes
```

- **Propósito**: Realiza solicitudes a la API para recuperar todos los personajes iterando a través de las páginas de resultados.
- **`response.json()`**: Convierte la respuesta de la API en un objeto JSON.
- **`data["info"]["next"]`**: Obtiene la URL de la siguiente página.

---

### **c. Función para Obtener Todos los Episodios**

```python
def obtener_todos_los_episodios():
    episodios = []
    url = EPISODE_API_URL
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            episodios.extend(data["results"])
            url = data["info"]["next"]
        else:
            st.error(f"Error al obtener episodios: {response.status_code}")
            break
    return episodios
```

- **Propósito**: Recupera información de todos los episodios usando paginación.
- Similar a la función de personajes, pero trabaja con episodios.

---

### **d. Carga de Datos con `@st.cache_data`**

```python
@st.cache_data
def cargar_datos():
    personajes = obtener_todos_los_personajes()
    episodios = obtener_todos_los_episodios()
    df_personajes = pd.DataFrame(personajes)
    df_episodios = pd.DataFrame(episodios)
    df_personajes["num_episodios"] = df_personajes["episode"].apply(len)
    return df_personajes, df_episodios
```

- **`@st.cache_data`**: Acelera el procesamiento almacenando en caché los datos descargados.
- **`pd.DataFrame`**: Convierte las listas en DataFrames para facilitar su análisis.
- **`apply(len)`**: Calcula el número de episodios en los que aparece cada personaje.

---

### **e. Mostrar Estadísticas y Gráficos**

### **Big Numbers: Personajes Vivos vs. Muertos**

```python
estado_counts = df_personajes["status"].value_counts().reset_index()
estado_counts.columns = ["Estado", "Cantidad"]

col1.metric("Vivos", estado_counts.loc[estado_counts["Estado"] == "Alive", "Cantidad"].sum())
col2.metric("Muertos", estado_counts.loc[estado_counts["Estado"] == "Dead", "Cantidad"].sum())
col3.metric("Estado Desconocido", estado_counts.loc[estado_counts["Estado"] == "unknown", "Cantidad"].sum())

fig_estado = px.bar(
    estado_counts,
    x="Estado",
    y="Cantidad",
    text="Cantidad",
    title="Distribución de Personajes por Estado"
)
st.plotly_chart(fig_estado)
```

- **`value_counts()`**: Cuenta los personajes por estado.
- **`metric`**: Muestra números destacados (Big Numbers).
- **`px.bar`**: Crea un gráfico de barras interactivo.

---

### **Top 10 Personajes con Más Apariciones**

```python
top_personajes = df_personajes[["name", "num_episodios"]].sort_values(by="num_episodios", ascending=False).head(10)
st.table(top_personajes)

fig_top_personajes = px.bar(
    top_personajes,
    x="num_episodios",
    y="name",
    orientation="h",
    text="num_episodios",
    title="Top 10 Personajes con Más Apariciones"
)
st.plotly_chart(fig_top_personajes)
```

- **`sort_values`**: Ordena los personajes por el número de episodios en los que aparecen.
- **`st.table`**: Muestra una tabla interactiva.

---

### **Episodios y Personajes por Episodio**

```python
personajes_por_episodio = df_episodios["characters"].apply(len)

st.metric("Total de Episodios", len(df_episodios))
st.metric("Promedio de Personajes por Episodio", round(personajes_por_episodio.mean(), 2))

fig_densidad = px.histogram(
    personajes_por_episodio,
    nbins=20,
    title="Distribución de Personajes por Episodio"
)
st.plotly_chart(fig_densidad)
```

- **`apply(len)`**: Calcula la cantidad de personajes por episodio.
- **`px.histogram`**: Crea un histograma para mostrar la distribución.

---

### **4. Ejecuta la Aplicación**

1. Inicia la aplicación:
    
    ```bash
    streamlit run app.py
    ```
    
2. Abre tu navegador en `http://localhost:8501`.

---

### **5. Resultados Esperados**

- **Sección 1**: Big Numbers y gráfico de distribución por estado.
- **Sección 2**: Tabla y gráfico con los personajes más recurrentes.
- **Sección 3**: Estadísticas de episodios y un histograma de distribución