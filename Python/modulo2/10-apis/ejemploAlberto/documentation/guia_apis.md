### **Taller Interactivo: Uso de APIs con Python**

Empezaremos con el **Bloque 1: Introducción a las Peticiones y API de PokeAPI**, detallando cada paso para crear un proyecto que oculte configuraciones sensibles y transforme la información en un diccionario para su manipulación.

---

## **Bloque 1: API de PokeAPI**

### **Paso a Paso**

### **1. Configuración del Entorno**

Primero, configuraremos un entorno virtual y crearemos un archivo `.env` para manejar configuraciones sensibles, como las URL base de la API.

1. **Crear el entorno virtual**:
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # En macOS/Linux
    venv\Scripts\activate     # En Windows
    ```
    
2. **Instalar dependencias necesarias**:
    
    ```bash
    pip install requests python-dotenv
    ```
    
3. **Crear el archivo `.env`**:
    - En la raíz del proyecto, crea un archivo llamado `.env` con el siguiente contenido:
        
        ```makefile
        API_URL=https://pokeapi.co/api/v2/pokemon
        ```
        
4. **Asegurarse de ignorar `.env` en Git**:
    - Crea o edita un archivo `.gitignore` en la raíz y añade:
        
        ```bash
        .env
        venv/
        ```
        
5. **Cargar variables del archivo `.env`**:
    - Utilizaremos la biblioteca `python-dotenv` para cargar las variables en el código.

---

### **2. Código Inicial: Configuración y Solicitudes**

Crearemos un script base para realizar solicitudes a la API y manejar configuraciones.

```python
import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener la URL base desde el archivo .env
API_URL = os.getenv("API_URL")

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

```

---

### **3. Transformar la Información en un Diccionario**

El siguiente paso es filtrar y organizar los datos relevantes en un diccionario para su manipulación.

```python
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
```

---

### **4. Guardar Información en un Archivo**

Podemos guardar la información transformada en un archivo JSON para su uso posterior.

```python
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
```

---

### **5. Ejercicio para los Participantes**

- **Tarea 1**: Ampliar el programa para aceptar varios nombres de Pokémon como entrada y guardar la información de todos en un archivo único.
- **Tarea 2**: Usar el endpoint `/pokemon-species/{id}` para obtener información sobre las evoluciones del Pokémon.

---

### **Guía para Ejecutar**

1. Asegúrate de que el entorno virtual esté activo.
2. Instala las dependencias necesarias:
    
    ```bash
    pip install requests python-dotenv
    ```
    
3. Crea el archivo `.env` con la URL base:
    
    ```makefile
    API_URL=https://pokeapi.co/api/v2/pokemon
    ```
    
4. Ejecuta el script:
    
    ```bash
    python main.py
    ```
### **Bloque 2: Uso de la API de Rick and Morty**

### **1. Configuración del Entorno**

1. **Crear el entorno virtual**:
Si ya tienes el entorno creado desde el Bloque 1, puedes reutilizarlo. Si no:
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # En macOS/Linux
    venv\Scripts\activate     # En Windows
    ```
    
2. **Instalar las dependencias necesarias**:
    
    ```bash
    pip install requests python-dotenv
    ```
    
3. **Crear el archivo `.env`**:
En la raíz del proyecto, crea un archivo `.env`:
    
    ```makefile
    RICK_MORTY_API_URL=https://rickandmortyapi.com/api/character
    ```
    
4. **Asegúrate de que `.env` esté en el `.gitignore`**:
    - Si ya lo añadiste en el Bloque 1, no es necesario repetir este paso.
    
    ```bash
    .env
    venv/
    ```
    

---

### **2. Código Inicial: Configuración y Solicitudes**

Crearemos un script base para realizar solicitudes a la API de Rick and Morty y manejar configuraciones.

```python
import requests
import os
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
```

---

### **3. Transformar la Información en un Diccionario**

Extraeremos información relevante, como el estado, especie, ubicación y origen.

```python
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
```

---

### **4. Guardar Información en un Archivo**

Guardaremos los datos en un archivo JSON para que sean reutilizables.

```python
import json

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
```

---

### **5. Ejercicio Interactivo**

- **Tarea 1**: Ampliar el programa para buscar personajes filtrando por estado (`Alive`, `Dead`, `Unknown`).
- **Tarea 2**: Obtener los episodios en los que aparece un personaje utilizando los IDs en `episode` de los resultados.

---

### **6. Ejemplo Avanzado: Obtener Episodios**

Expandiremos el programa para buscar los episodios en los que aparece un personaje específico.

```python
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
```

---

### **Guía para Ejecutar**

1. **Configurar el entorno virtual**:
    
    ```bash
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
    ```
    
2. **Instalar dependencias**:
    
    ```bash
    pip install requests python-dotenv
    ```
    
3. **Crear y configurar el archivo `.env`**:
    
    ```makefile
    RICK_MORTY_API_URL=https://rickandmortyapi.com/api/character
    ```
    
4. **Ejecutar el script**:
    
    ```bash
    python main.py
    ```