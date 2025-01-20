
### **Ejercicio Propuesto**

1. Realiza una solicitud para obtener cervecerías por tipo (`micro`) en California.
2. Organiza la información en un DataFrame.
3. Calcula cuántas cervecerías hay por ciudad en California.
4. Crea un gráfico de barras que muestre las ciudades con más cervecerías.

# Guía API Open Brewery

### **Configurar el entorno virtual**

```bash
# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate

# Instalar las dependencias necesarias
pip install pandas numpy requests tqdm python-dotenv
```

### **Crear el archivo `requirements.txt`**

Para documentar las dependencias instaladas:

```bash
pip freeze > requirements.txt
```

### **Configurar el archivo `.env`**

Crea un archivo `.env` en el directorio raíz con el contenido:

```makefile
API_KEY=tu_clave_de_api
```

Asegúrate de agregar tanto `venv/` como `.env` a tu `.gitignore`:

```bash
venv/
.env
```

### **Código Python**

```python
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
api_key = os.getenv("API_KEY")

# Verificar la clave API
if not api_key:
    raise ValueError("La clave API no se encuentra en el archivo .env")

# Función para manejar llamadas a la API con manejo de errores
def llamada_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si el código de estado no es 200
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

# URL base de la API
base_url = "https://api.openbrewerydb.org/v1/breweries"

# Ejemplo: Llamada a la API para obtener todas las cervecerías
print("Haciendo llamada a la API para todas las cervecerías...")
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
```

### **Notas adicionales**

1. **Automatización y Escalabilidad**:
    - Las funciones `llamada_api` y `limpieza_datos` permiten un flujo escalable y reutilizable.
    - Puedes agregar más estados a la lista para ampliar el análisis.
2. **Seguridad**:
    - Las claves sensibles, como `API_KEY`, se gestionan a través de `.env` para evitar exposición.
3. **Manejo de Errores**:
    - La función `llamada_api` maneja distintos tipos de errores como problemas de conexión, tiempos de espera o errores de cliente/servidor.
4. **Exportación**:
    - Los datos finales se guardan en un archivo CSV, lo que facilita su uso posterior en herramientas como Excel o Power BI.

### Resultado Final

Este proyecto es modular, seguro y fácil de mantener. Ideal para aprender y aplicar buenas prácticas en el manejo de APIs y procesamiento de datos. ¡Déjame saber si necesitas más ejemplos o mejoras! 🚀