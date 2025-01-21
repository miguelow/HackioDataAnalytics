### **Paso 1: Crear un entorno virtual**

Primero, crea un entorno virtual para mantener las dependencias del proyecto aisladas:

```bash
# Crear un entorno virtual
python -m venv selenium_env

# Activar el entorno virtual
# En Windows:
selenium_env\Scripts\activate
# En macOS/Linux:
source selenium_env/bin/activate
```

### **Paso 2: Instalar las dependencias necesarias**

Instala las bibliotecas requeridas para Selenium y WebDriver Manager:

```bash
pip install selenium webdriver-manager
```

### **Paso 3: Código paso a paso**

### **1. Inicialización del proyecto**

Crea un archivo Python llamado `wikipedia_scraper.py` y comienza escribiendo el código para inicializar el navegador:

```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Inicializamos el WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Definimos la URL de la página de Wikipedia
url = "https://es.wikipedia.org/wiki/Donald_Trump"

# Navegamos a la página
driver.get(url)

# Esperamos unos segundos para que la página cargue completamente
sleep(3)
```

### **2. Extracción del título de la página**

Busca el título utilizando su atributo `id`. El título de las páginas de Wikipedia se encuentra en un elemento con `id="firstHeading"`:

```python
# Buscar el título de la página por ID
titulo = driver.find_element("id", "firstHeading")
print(f"Título de la página: {titulo.text}")
```

### **3. Extracción de la introducción**

El primer párrafo del artículo se encuentra dentro de un `<p>` bajo el contenedor principal:

```python
# Buscar el primer párrafo de la introducción
introduccion = driver.find_element("css selector", "div.mw-parser-output > p")
print(f"Introducción: {introduccion.text}")
```

### **4. Extracción de imágenes**

Busca todas las imágenes presentes en la página y extrae sus URLs:

```python
# Buscar todas las imágenes en la página
imagenes = driver.find_elements("css selector", "img")

# Extraer y mostrar las URLs de las imágenes
for i, img in enumerate(imagenes[:5]):  # Mostramos solo las primeras 5 imágenes
    print(f"Imagen {i + 1}: {img.get_attribute('src')}")
```

### **5. Extracción de elementos específicos con XPath**

Puedes extraer elementos más específicos, como tablas, utilizando XPath:

```python
# Buscar una tabla específica (ejemplo: tabla de información general)
try:
    tabla = driver.find_element("xpath", '//*[@class="infobox vcard"]')
    print(f"Texto de la tabla:\n{tabla.text}")
except Exception as e:
    print(f"No se encontró la tabla: {e}")
```

### **6. Cierre del navegador**

Cierra el navegador para liberar recursos:

```python
# Cerramos la ventana actual
driver.close()

# Finalizamos la sesión del WebDriver
driver.quit()
```

### **Código completo**

```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Inicializamos el WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# URL de la página de Wikipedia
url = "https://es.wikipedia.org/wiki/Donald_Trump"

# Navegamos a la página
driver.get(url)
sleep(3)

# Extracción del título
titulo = driver.find_element("id", "firstHeading")
print(f"Título de la página: {titulo.text}")

# Extracción de la introducción
introduccion = driver.find_element("css selector", "div.mw-parser-output > p")
print(f"Introducción: {introduccion.text}")

# Extracción de imágenes
imagenes = driver.find_elements("css selector", "img")
for i, img in enumerate(imagenes[:5]):
    print(f"Imagen {i + 1}: {img.get_attribute('src')}")

# Extracción de una tabla específica
try:
    tabla = driver.find_element("xpath", '//*[@class="infobox vcard"]')
    print(f"Texto de la tabla:\n{tabla.text}")
except Exception as e:
    print(f"No se encontró la tabla: {e}")

# Cerramos el navegador
driver.close()
driver.quit()
```

---

### **Ejecución del proyecto**

1. Guarda el código como `wikipedia_scraper.py`.
2. Activa el entorno virtual y ejecuta el script:

```bash
python wikipedia_scraper.py
```

### **Resultado esperado**

Al ejecutar este script, deberías ver en la consola:

- El título de la página.
- El primer párrafo de la introducción.
- URLs de las primeras cinco imágenes.
- Información de la tabla (si está disponible).