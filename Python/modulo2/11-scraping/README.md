# **Introducción al Web Scraping**

### **¿Qué es el Web Scraping?**

El **Web Scraping** es una técnica que permite extraer datos de sitios web de manera automatizada. Este método consiste en interactuar con el contenido visible o subyacente de las páginas web y convertir esa información en un formato estructurado que pueda ser utilizado para análisis o almacenamiento. Es una herramienta fundamental para analistas de datos, desarrolladores y científicos de datos, ya que permite recopilar grandes volúmenes de datos de forma rápida y eficiente.

### **Propósitos del Web Scraping**

1. **Recopilación de datos para análisis**: Obtener información como precios, comentarios de productos, tendencias, entre otros.
2. **Actualización automática**: Crear sistemas que extraen datos periódicamente, como cotizaciones de bolsa o informes climáticos.
3. **Construcción de bases de datos**: Recolectar información dispersa en varias fuentes para almacenarla en un único lugar.

### **Ventajas del Web Scraping**

- **Eficiencia**: Permite recopilar grandes cantidades de datos en segundos o minutos.
- **Automatización**: Reduce la necesidad de tareas manuales repetitivas y propensas a errores.
- **Acceso a información pública**: Extrae datos disponibles públicamente sin necesidad de intervención humana.

### **Herramientas Populares para Web Scraping en Python**

En Python, existen varias bibliotecas y frameworks que simplifican el proceso de scraping:

1. **Beautiful Soup**: Diseñada para extraer datos de documentos HTML y XML, esta biblioteca permite buscar, navegar y manipular la estructura de una página de manera sencilla.
2. **Selenium**: Es ideal para manejar páginas dinámicas generadas con JavaScript, ya que simula la interacción con el navegador, como clics, envíos de formularios y navegación entre páginas.
3. **Scrapy**: Un framework de scraping avanzado que permite realizar extracciones de datos a gran escala con funcionalidades como manejo de sesiones, gestión de errores y almacenamiento de datos.
4. **lxml**: Biblioteca altamente eficiente para procesar y analizar documentos HTML y XML utilizando selectores CSS o expresiones XPath.
5. **Playwright**: Similar a Selenium, pero más moderno y rápido, ideal para interactuar con navegadores y extraer datos de sitios dinámicos.

### **Limitaciones del Web Scraping**

A pesar de sus ventajas, el Web Scraping tiene algunas limitaciones:

- **Cambios en la estructura de la página**: Si el diseño o el HTML de la página cambia, el script de scraping puede dejar de funcionar.
- **Restricciones legales**: Algunos sitios web prohíben explícitamente el scraping en sus términos de servicio.
- **Limitaciones técnicas**: Muchas páginas implementan medidas como captchas o limitaciones de tasa (rate limiting) para evitar el scraping.

### **Consideraciones Éticas**

El Web Scraping debe realizarse respetando las políticas del sitio web y evitando sobrecargar los servidores con solicitudes excesivas. Revisar el archivo `robots.txt` del dominio es una buena práctica para verificar las reglas de acceso automatizado.

# **Introducción a HTML**

### **¿Qué es HTML?**

HTML, que significa **HyperText Markup Language** (Lenguaje de Marcado de Hipertexto), es el lenguaje estándar utilizado para estructurar el contenido de las páginas web. A diferencia de los lenguajes de programación como Python o Java, HTML no contiene lógica de programación; en su lugar, define la estructura, el contenido y las relaciones jerárquicas de los elementos de una página web.

### **¿Cómo funciona HTML?**

HTML utiliza **etiquetas** o **elementos** para delimitar y describir diferentes tipos de contenido, como títulos, párrafos, imágenes, tablas y enlaces. Estas etiquetas son interpretadas por los navegadores para renderizar las páginas web que los usuarios ven e interactúan.

Cada documento HTML comienza con una declaración `<!DOCTYPE html>` que especifica el tipo de documento, seguida de una estructura jerárquica que incluye las siguientes secciones principales:

- **Etiqueta `<html>`**: Es la raíz de un documento HTML y contiene todo el contenido de la página.
- **Etiqueta `<head>`**: Contiene información sobre el documento, como el título, metadatos y enlaces a recursos externos como hojas de estilo o scripts.
- **Etiqueta `<body>`**: Contiene el contenido visible de la página web, como texto, imágenes y otros elementos interactivos.

### **Ejemplo básico de HTML**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi primera página web</title>
</head>
<body>
    <h1>Bienvenidos a mi página</h1>
    <p>Este es un párrafo de ejemplo.</p>
    <a href="https://www.ejemplo.com">Visita Ejemplo.com</a>
    <img src="imagen.jpg" alt="Descripción de la imagen">
</body>
</html>
```

**Explicación del código:**

- **`<title>`**: Define el título que aparece en la pestaña del navegador.
- **`<h1>`**: Un encabezado de nivel 1, generalmente usado para títulos principales.
- **`<p>`**: Define un párrafo de texto.
- **`<a>`**: Crea un enlace a otra página web. El atributo `href` especifica la URL de destino.
- **`<img>`**: Inserta una imagen en la página. El atributo `src` contiene la ruta de la imagen, y `alt` proporciona una descripción para usuarios con discapacidades visuales o cuando la imagen no se carga.

### **Principales etiquetas HTML**

| Etiqueta | Descripción |
| --- | --- |
| `<html>` | Elemento raíz de un documento HTML. |
| `<head>` | Contiene metadatos, enlaces y scripts externos. |
| `<title>` | Especifica el título de la página web. |
| `<body>` | Contiene el contenido visible de la página. |
| `<h1>` a `<h6>` | Encabezados de diferentes niveles, siendo `<h1>` el más importante. |
| `<p>` | Representa un párrafo de texto. |
| `<a>` | Crea enlaces a otras páginas o secciones del mismo documento. |
| `<img>` | Inserta imágenes en la página. |
| `<ul>` | Define una lista no ordenada (con viñetas). |
| `<ol>` | Define una lista ordenada (numerada). |
| `<li>` | Representa un elemento de una lista. |
| `<table>` | Crea una tabla. |
| `<tr>` | Define una fila en una tabla. |
| `<td>` | Representa una celda en una tabla. |
| `<th>` | Define un encabezado de columna o fila en una tabla. |

### **Relación con el Web Scraping**

El conocimiento de HTML es esencial para el **Web Scraping**, ya que los datos que se desean extraer están contenidos dentro de estas etiquetas. Por ejemplo:

- Un texto puede estar en un párrafo (`<p>`).
- Un enlace estará en una etiqueta `<a>`.
- Una tabla de datos estará dentro de una etiqueta `<table>`.

A lo largo de esta unidad, aprenderemos cómo navegar por el HTML, identificar elementos relevantes y utilizar herramientas como **Beautiful Soup** para extraer información de manera eficiente.

# **Selectores CSS**

### **¿Qué son los selectores CSS?**

Los **selectores CSS** son patrones que permiten seleccionar y aplicar estilos a elementos HTML específicos en una página web. Además de su función principal en el diseño web, los selectores CSS son fundamentales en el **Web Scraping**, ya que facilitan la identificación y extracción de datos específicos de un documento HTML.

Los selectores CSS permiten apuntar a elementos HTML basándose en diferentes criterios, como el tipo de etiqueta, el atributo `id`, la clase, la jerarquía o las combinaciones de estas características.

### **Tipos de selectores CSS más comunes**

| Tipo de Selector | Ejemplo | Descripción |
| --- | --- | --- |
| **Selector de tipo** | `p` | Selecciona todos los elementos de un tipo específico, como todos los párrafos (`<p>`). |
| **Selector de clase** | `.clase` | Selecciona todos los elementos que tienen una clase específica, por ejemplo, `.destacado`. |
| **Selector de ID** | `#id` | Selecciona un único elemento con un identificador único, por ejemplo, `#menu`. |
| **Selector de atributo** | `[atributo]` | Selecciona elementos que tienen un atributo específico, por ejemplo, `[src]` para todas las imágenes. |
| **Selector descendente** | `div p` | Selecciona todos los párrafos (`<p>`) que están dentro de un contenedor `<div>`. |
| **Selector hijo directo** | `div > p` | Selecciona los párrafos (`<p>`) que son hijos directos de un contenedor `<div>`. |
| **Selector general de hermanos** | `h1 ~ p` | Selecciona todos los elementos `<p>` que sean hermanos de un `<h1>`. |
| **Selector universal** | `*` | Selecciona todos los elementos en el documento HTML. |

### **Ejemplos prácticos de selectores CSS**

1. **Selector de tipo**
    
    ```html
    <p>Este es un párrafo.</p>
    <p>Este es otro párrafo.</p>
    ```
    
    Selector: `p`
    
    Selecciona: Todos los párrafos.
    
2. **Selector de clase**
    
    ```html
    <div class="destacado">Contenido destacado</div>
    <p class="destacado">Párrafo destacado</p>
    ```
    
    Selector: `.destacado`
    
    Selecciona: El `<div>` y el `<p>` con la clase `destacado`.
    
3. **Selector de ID**
    
    ```html
    <h1 id="titulo-principal">Título</h1>
    ```
    
    Selector: `#titulo-principal`
    
    Selecciona: El encabezado `<h1>` con el ID `titulo-principal`.
    
4. **Selector de atributo**
    
    ```html
    <img src="imagen1.jpg" alt="Imagen 1">
    <img src="imagen2.jpg" alt="Imagen 2">
    ```
    
    Selector: `[src]`
    
    Selecciona: Ambos elementos `<img>` porque tienen el atributo `src`.
    
5. **Selector descendente**
    
    ```html
    <div>
        <p>Párrafo dentro de un div</p>
    </div>
    <p>Párrafo fuera de un div</p>
    ```
    
    Selector: `div p`
    
    Selecciona: Solo el párrafo dentro del `<div>`.
    
6. **Selector hijo directo**
    
    ```html
    <div>
        <p>Párrafo hijo directo</p>
        <div>
            <p>Párrafo hijo no directo</p>
        </div>
    </div>
    ```
    
    Selector: `div > p`
    
    Selecciona: Solo el primer párrafo dentro del `<div>`.
    

### **Uso de los selectores CSS en el Web Scraping**

En **Beautiful Soup**, los selectores CSS se utilizan para identificar y extraer elementos HTML específicos de un documento. Algunos métodos clave incluyen:

1. **Método `select()`**
Permite buscar elementos utilizando selectores CSS. Devuelve una lista de objetos `Tag` que representan los elementos coincidentes.
    
    ```python
    from bs4 import BeautifulSoup
    
    # HTML de ejemplo
    html = """
    <div class="contenedor">
        <p class="texto">Primer párrafo</p>
        <p class="texto">Segundo párrafo</p>
        <a href="https://ejemplo.com">Un enlace</a>
    </div>
    """
    
    # Analizamos el HTML
    soup = BeautifulSoup(html, "html.parser")
    
    # Seleccionamos todos los párrafos con clase "texto"
    elementos = soup.select("p.texto")
    
    # Mostramos el texto de cada elemento
    for elemento in elementos:
        print(elemento.get_text())
    ```
    
    **Salida:**
    
    ```css
    Primer párrafo
    Segundo párrafo
    ```
    
2. **Selector combinado con atributos**
    
    ```python
    # Selecciona todos los enlaces (<a>) con el atributo href
    enlaces = soup.select("a[href]")
    print(enlaces[0].get("href"))  # https://ejemplo.com
    ```
    
3. **Selector de descendencia**
    
    ```python
    # Selecciona los párrafos dentro de un contenedor <div>
    parrafos = soup.select("div.contenedor > p")
    for parrafo in parrafos:
        print(parrafo.get_text())
    ```
    

Con una comprensión sólida de los selectores CSS, podrás identificar y extraer datos específicos de una página web con precisión.

# **Introducción a Beautiful Soup**

### **¿Qué es Beautiful Soup?**

**Beautiful Soup** es una biblioteca de Python diseñada para trabajar con documentos HTML y XML. Su propósito principal es facilitar la **extracción de datos estructurados** o no estructurados de estos documentos. Utilizando Beautiful Soup, puedes navegar y manipular la estructura del árbol DOM (Document Object Model) de una página web.

Esta herramienta se utiliza ampliamente en proyectos de **Web Scraping** debido a su facilidad de uso, su flexibilidad y su capacidad para integrarse con otras bibliotecas como **requests** y **lxml**.

### **Características principales de Beautiful Soup**

1. **Analiza documentos HTML y XML:**
Puede manejar documentos HTML que no están bien formateados y procesarlos de manera eficiente.
2. **Compatibilidad con múltiples analizadores:**
    - `html.parser`: Analizador básico integrado en Python.
    - `lxml`: Analizador rápido y eficiente.
    - `html5lib`: Analizador más tolerante, ideal para documentos muy desordenados.
3. **Navegación intuitiva:**
Representa los documentos HTML/XML como un árbol jerárquico, lo que facilita acceder a las etiquetas, atributos y contenido.
4. **Búsqueda avanzada:**
Ofrece métodos como `find`, `findAll` y `select` (basados en selectores CSS) para buscar elementos en el árbol DOM.
5. **Extracción personalizada:**
Puedes extraer datos específicos utilizando etiquetas, clases, atributos o combinaciones de estos.

### **Instalación de Beautiful Soup**

Antes de comenzar a usar Beautiful Soup, es necesario instalarlo. Se utiliza el siguiente comando para instalarlo junto con uno de los analizadores más comunes (`lxml`):

```bash
pip install beautifulsoup4 lxml
```

### **Cómo funciona Beautiful Soup**

A continuación, se muestra un ejemplo básico del flujo de trabajo con Beautiful Soup:

1. Realizas una solicitud HTTP para obtener el HTML de una página web (puedes usar la biblioteca `requests`).
2. Analizas el HTML usando Beautiful Soup.
3. Navegas y seleccionas los elementos de interés en el árbol DOM.
4. Extraes y manipulas los datos según sea necesario.

### **Ejemplo básico: Analizando HTML con Beautiful Soup**

1. **Código HTML de ejemplo:**
    
    ```html
    <html>
        <head>
            <title>Ejemplo de página web</title>
        </head>
        <body>
            <h1>Encabezado principal</h1>
            <p>Este es un párrafo con un <a href="https://ejemplo.com">enlace</a>.</p>
            <p class="importante">Este es un párrafo importante.</p>
        </body>
    </html>
    ```
    
2. **Uso de Beautiful Soup:**
    
    ```python
    from bs4 import BeautifulSoup
    
    # Código HTML
    html = """
    <html>
        <head>
            <title>Ejemplo de página web</title>
        </head>
        <body>
            <h1>Encabezado principal</h1>
            <p>Este es un párrafo con un <a href="https://ejemplo.com">enlace</a>.</p>
            <p class="importante">Este es un párrafo importante.</p>
        </body>
    </html>
    """
    
    # Crear el objeto BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    
    # Acceso a elementos del árbol DOM
    print(soup.title)           # <title>Ejemplo de página web</title>
    print(soup.title.text)      # Ejemplo de página web
    print(soup.h1)              # <h1>Encabezado principal</h1>
    print(soup.p)               # <p>Este es un párrafo con un <a href="https://ejemplo.com">enlace</a>.</p>
    
    # Extraer atributos
    enlace = soup.a
    print(enlace["href"])       # https://ejemplo.com
    ```
    
3. **Salida esperada:**
    
    ```less
    <title>Ejemplo de página web</title>
    Ejemplo de página web
    <h1>Encabezado principal</h1>
    <p>Este es un párrafo con un <a href="https://ejemplo.com">enlace</a>.</p>
    https://ejemplo.com
    ```
    

### **Principales métodos de Beautiful Soup**

| Método | Descripción |
| --- | --- |
| **`find(tag)`** | Devuelve el primer elemento que coincide con la etiqueta especificada. |
| **`findAll(tag)`** | Devuelve todos los elementos que coinciden con la etiqueta especificada en forma de lista. |
| **`select(selector)`** | Devuelve elementos que coinciden con un selector CSS. |
| **`get(attr)`** | Obtiene el valor de un atributo específico de una etiqueta. |
| **`getText()`** | Devuelve el texto contenido dentro de una etiqueta, eliminando las etiquetas HTML. |
| **`prettify()`** | Devuelve una representación legible del árbol DOM con sangría. |

### **Elección del analizador**

Aunque Beautiful Soup es compatible con varios analizadores, es importante seleccionar el más adecuado según tus necesidades:

- **`html.parser`:** Analizador integrado en Python. Es suficiente para la mayoría de los casos y no requiere instalación adicional.
- **`lxml`:** Muy rápido y eficiente. Requiere instalar la biblioteca `lxml` por separado.
- **`html5lib`:** Más tolerante, ideal para documentos HTML mal formateados.

```python
# Crear un objeto BeautifulSoup con diferentes analizadores
soup_html_parser = BeautifulSoup(html, "html.parser")
soup_lxml = BeautifulSoup(html, "lxml")
soup_html5lib = BeautifulSoup(html, "html5lib")

```

# **Métodos importantes de Beautiful Soup**

Beautiful Soup proporciona una variedad de métodos que hacen que la extracción y manipulación de datos HTML/XML sea sencilla y eficiente. A continuación, se explican los métodos más importantes con ejemplos prácticos.

### **`BeautifulSoup`**

El constructor principal de Beautiful Soup, que convierte el código HTML o XML en un objeto navegable.

```python
from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>Ejemplo</title>
    </head>
    <body>
        <h1>Encabezado</h1>
        <p>Contenido de prueba</p>
    </body>
</html>
"""

# Crear un objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Navegar por el árbol DOM
print(soup.title)  # <title>Ejemplo</title>
print(soup.body.h1)  # <h1>Encabezado</h1>
```

### **`find()`**

Busca y devuelve el **primer elemento** que coincide con los criterios especificados.

```python
html = """
<html>
    <body>
        <h1>Primer encabezado</h1>
        <h1>Segundo encabezado</h1>
        <p class="contenido">Párrafo de prueba</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Encuentra el primer <h1>
print(soup.find("h1"))  # <h1>Primer encabezado</h1>

# Encuentra el primer elemento <p> con clase "contenido"
print(soup.find("p", class_="contenido"))  # <p class="contenido">Párrafo de prueba</p>
```

### **`findAll()`**

Devuelve **todos los elementos** que coinciden con los criterios en forma de lista.

```python
html = """
<html>
    <body>
        <h1>Primer encabezado</h1>
        <h1>Segundo encabezado</h1>
        <p class="contenido">Párrafo de prueba</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Encuentra todos los <h1>
print(soup.findAll("h1"))
# [<h1>Primer encabezado</h1>, <h1>Segundo encabezado</h1>]

# Iterar sobre los resultados
for h1 in soup.findAll("h1"):
    print(h1.text)
```

### **`select()`**

Permite buscar elementos utilizando **selectores CSS**.

```python
html = """
<html>
    <body>
        <div class="contenedor">
            <p class="texto">Texto 1</p>
            <p class="texto">Texto 2</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Buscar elementos con clase "texto"
resultados = soup.select(".texto")
for res in resultados:
    print(res.text)
```

### **5.5 `get()`**

Obtiene el valor de un atributo específico de un elemento.

```python
html = """
<html>
    <body>
        <a href="https://example.com">Enlace</a>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Obtener el atributo href del enlace
enlace = soup.find("a")
print(enlace.get("href"))  # https://example.com
```

### **`getText()`**

Extrae solo el texto de un elemento, eliminando las etiquetas HTML.

```python
html = """
<html>
    <body>
        <h1>Encabezado</h1>
        <p>Texto de ejemplo</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Extraer texto
print(soup.h1.getText())  # Encabezado
print(soup.p.getText())   # Texto de ejemplo
```

### **`prettify()`**

Devuelve el código HTML/XML con una estructura legible (agrega sangría y saltos de línea).

```python
html = """
<html><body><h1>Encabezado</h1><p>Texto de ejemplo</p></body></html>
"""

soup = BeautifulSoup(html, "html.parser")

# Imprimir el HTML formateado
print(soup.prettify())
```

**Salida:**

```html
<html>
 <body>
  <h1>
   Encabezado
  </h1>
  <p>
   Texto de ejemplo
  </p>
 </body>
</html>
```

### **Otros métodos útiles**

1. **`parent`:** Permite acceder al elemento padre de un nodo.
    
    ```python
    nodo = soup.find("h1")
    print(nodo.parent)  # Muestra el contenido del elemento <body>
    ```
    
2. **`children`:** Devuelve un generador que permite iterar sobre los hijos directos de un nodo.
    
    ```python
    for child in soup.body.children:
        print(child)
    ```
    
3. **`descendants`:** Devuelve todos los descendientes de un nodo.
    
    ```python
    for desc in soup.body.descendants:
        print(desc)
    ```
    
4. **`previous_sibling` y `next_sibling`:** Permiten navegar entre elementos hermanos.
    
    ```python
    nodo = soup.find("h1")
    print(nodo.next_sibling)  # Muestra el nodo siguiente a <h1>
    ```
    

### **Ejemplo completo**

```python
html = """
<html>
    <head>
        <title>Página de ejemplo</title>
    </head>
    <body>
        <h1>Encabezado</h1>
        <p class="info">Este es un párrafo.</p>
        <a href="https://example.com" class="link">Enlace</a>
    </body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")

# Usando varios métodos
print(soup.title.text)  # Página de ejemplo
print(soup.find("p", class_="info").getText())  # Este es un párrafo.
print(soup.find("a").get("href"))  # https://example.com
print(soup.select(".link")[0].getText())  # Enlace
```

# **Biblioteca `requests`**

La biblioteca `requests` es una de las herramientas más utilizadas en Python para realizar solicitudes HTTP. Nos permite enviar solicitudes a servidores web y manejar las respuestas fácilmente. En el contexto del web scraping, `requests` es fundamental para obtener el código HTML de las páginas que deseamos analizar.

### **Introducción a `requests`**

Con `requests`, podemos realizar solicitudes HTTP como `GET`, `POST`, `PUT`, `DELETE`, entre otros, de manera sencilla y eficiente. Estas solicitudes nos permiten interactuar con servidores para obtener datos o enviar información.

### **Instalación**

Si aún no tienes instalada la biblioteca, puedes hacerlo con el siguiente comando:

```bash
pip install requests
```

### **Métodos básicos de `requests`**

### **`requests.get()`**

El método `get()` se utiliza para realizar una solicitud HTTP de tipo `GET`, que generalmente se usa para obtener datos de un servidor.

```python
import requests

# URL de la página web
url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"

# Realizar la solicitud
response = requests.get(url)

# Imprimir el código de respuesta
print(f"Código de estado: {response.status_code}")

# Imprimir el contenido HTML
print(response.text[:500])  # Muestra los primeros 500 caracteres del HTML
```

### **`requests.post()`**

El método `post()` se utiliza para enviar datos al servidor, como formularios o credenciales.

```python
# URL de ejemplo para una solicitud POST
url = "https://httpbin.org/post"

# Datos a enviar
data = {"usuario": "prueba", "contraseña": "12345"}

# Realizar la solicitud POST
response = requests.post(url, data=data)

# Imprimir la respuesta del servidor
print(response.json())
```

### **Propiedades de las respuestas**

Cuando hacemos una solicitud con `requests`, obtenemos un objeto de respuesta que contiene varias propiedades útiles:

### **`response.status_code`**

El código de estado HTTP indica si la solicitud fue exitosa. Algunos códigos comunes son:

- `200`: Éxito.
- `404`: No encontrado.
- `500`: Error interno del servidor.

```python
if response.status_code == 200:
    print("La solicitud fue exitosa.")
else:
    print(f"Error: {response.status_code}")
```

### **`response.text`**

Contiene el contenido de la respuesta en formato de texto.

```python
html = response.text
print(html[:100])  # Imprime los primeros 100 caracteres del HTML
```

### **`response.content`**

Devuelve el contenido en formato binario, útil para manejar imágenes o archivos.

```python
contenido_binario = response.content
```

### **`response.json()`**

Si el servidor devuelve datos en formato JSON, podemos analizarlos fácilmente con este método.

```python
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

# Convertir la respuesta a JSON
datos = response.json()
print(datos)
```

### **Headers y User-Agent**

Algunos servidores bloquean solicitudes de scripts automáticos. Para simular un navegador, podemos incluir un `User-Agent` en los encabezados de la solicitud.

```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}

# Solicitud con headers personalizados
response = requests.get(url, headers=headers)

print(response.status_code)
```

### **Manejo de errores**

Es importante manejar errores como conexiones fallidas o respuestas no exitosas.

```python
try:
    response = requests.get("https://example.com")
    response.raise_for_status()  # Lanza una excepción si el código no es 200
    print("Solicitud exitosa")
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")
```

---

### **Ejemplo completo: Obtener el HTML de Wikipedia**

```python
import requests

url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"

# Encabezados personalizados
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}

# Realizar la solicitud
response = requests.get(url, headers=headers)

# Verificar el estado de la solicitud
if response.status_code == 200:
    print("Solicitud exitosa")
    # Guardar el contenido HTML en un archivo
    with open("WikipediaPortada.html", "w", encoding="utf-8") as archivo:
        archivo.write(response.text)
else:
    print(f"Error en la solicitud: {response.status_code}")
```

# **Extracción de datos de Wikipedia**

En este apartado, utilizaremos **`requests`** junto con **`Beautiful Soup`** para extraer datos específicos de la página de inicio de Wikipedia. Este ejemplo nos ayudará a entender cómo combinar ambas herramientas para realizar web scraping de manera eficiente.

### **Configuración inicial**

Antes de comenzar, asegúrate de haber instalado las bibliotecas necesarias:

```bash
pip install requests beautifulsoup4
```

Importamos las bibliotecas y definimos la URL de la página que deseamos analizar:

```python
from bs4 import BeautifulSoup
import requests

# URL de la página de Wikipedia
url_wiki = "https://es.wikipedia.org/wiki/Wikipedia:Portada"

# Encabezados personalizados
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}

# Realizamos la solicitud GET
response = requests.get(url_wiki, headers=headers)

# Verificamos el estado de la solicitud
if response.status_code == 200:
    print("Solicitud exitosa")
else:
    print(f"Error en la solicitud: {response.status_code}")
```

### **Crear el objeto `BeautifulSoup`**

Una vez que obtenemos el contenido HTML, utilizamos **`BeautifulSoup`** para analizarlo:

```python
# Creamos un objeto BeautifulSoup para analizar el contenido HTML
sopa_wiki = BeautifulSoup(response.content, "html.parser")

# Mostramos los primeros 500 caracteres del HTML para verificar
print(sopa_wiki.prettify()[:500])
```

### **Guardar el contenido HTML**

Para realizar un análisis más detallado, podemos guardar el HTML en un archivo local:

```python
# Guardamos el código HTML en un archivo local
ruta_guardado = "WikipediaPortada.html"
with open(ruta_guardado, "w", encoding="utf-8") as archivo:
    archivo.write(sopa_wiki.prettify())
```

### **Extraer etiquetas específicas**

A continuación, buscamos etiquetas HTML comunes para extraer información relevante:

### **Etiqueta `<head>`**

La etiqueta `<head>` contiene metadatos y configuraciones de la página:

```python
etiquetas_head = sopa_wiki.findAll("head")
print(f"Número de etiquetas <head>: {len(etiquetas_head)}")

# Extraemos el contenido del <head>
contenido_head = sopa_wiki.find("head").getText()
print(contenido_head[:200])  # Mostramos los primeros 200 caracteres
```

### **Etiqueta `<title>`**

El título de la página se encuentra en la etiqueta `<title>`:

```python
etiquetas_title = sopa_wiki.findAll("title")
print(f"Número de etiquetas <title>: {len(etiquetas_title)}")

# Extraemos el contenido del <title>
contenido_title = sopa_wiki.find("title").getText()
print(f"Título de la página: {contenido_title}")
```

### **Etiqueta `<body>`**

El contenido principal de la página está dentro de la etiqueta `<body>`:

```python
etiquetas_body = sopa_wiki.findAll("body")
print(f"Número de etiquetas <body>: {len(etiquetas_body)}")

# Extraemos el contenido del <body>
contenido_body = sopa_wiki.find("body").getText()[:200]  # Mostramos los primeros 200 caracteres
print(f"Contenido del body: {contenido_body}")
```

### **Etiqueta `<h1>`**

Los encabezados principales de la página están dentro de etiquetas `<h1>`:

```python
etiquetas_h1 = sopa_wiki.findAll("h1")
print(f"Número de etiquetas <h1>: {len(etiquetas_h1)}")

# Mostramos el texto de cada <h1>
for i, h1 in enumerate(etiquetas_h1):
    print(f"Texto del <h1> {i + 1}: {h1.getText()}")
```

### **Etiqueta `<a>`**

Los enlaces de la página están contenidos en etiquetas `<a>`:

```python
etiquetas_a = sopa_wiki.findAll("a")
print(f"Número de etiquetas <a>: {len(etiquetas_a)}")

# Mostramos los primeros 5 enlaces
for i, enlace in enumerate(etiquetas_a[:5]):
    print(f"Enlace {i + 1}: {enlace.getText()} | URL: {enlace.get('href')}")
```

### **Etiqueta `<img>`**

Las imágenes de la página están en etiquetas `<img>`:

```python
etiquetas_img = sopa_wiki.findAll("img")
print(f"Número de etiquetas <img>: {len(etiquetas_img)}")

# Mostramos las rutas de las primeras 5 imágenes
for i, img in enumerate(etiquetas_img[:5]):
    print(f"Imagen {i + 1}: {img.get('src')}")
```

### **Crear una función para extraer datos**

Podemos encapsular todos los pasos anteriores en una función reutilizable:

```python
def extraer_datos_wikipedia(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error en la solicitud: {response.status_code}")
        return None

    sopa = BeautifulSoup(response.content, "html.parser")
    datos = {
        "titulo": sopa.find("title").getText(),
        "enlaces": [a.getText() for a in sopa.findAll("a")[:10]],
        "imagenes": [img.get("src") for img in sopa.findAll("img")[:5]],
    }
    return datos
```

### **Probar la función**

Llamamos a la función para obtener datos específicos de la página de Wikipedia:

```python
datos_wikipedia = extraer_datos_wikipedia("https://es.wikipedia.org/wiki/Wikipedia:Portada")
print("Título de la página:", datos_wikipedia["titulo"])
print("Primeros 10 enlaces:", datos_wikipedia["enlaces"])
print("Primeras 5 imágenes:", datos_wikipedia["imagenes"])
```

# **Creación de una función para web scraping reutilizable**

En este punto, encapsularemos el flujo de trabajo de web scraping en una función general y modular. Esto permitirá reutilizar el código para diferentes páginas web y necesidades específicas.

### **Definir la estructura básica**

La función debe aceptar como parámetros la URL de la página web y los selectores necesarios para extraer datos específicos, como enlaces, imágenes o encabezados.

```python
from bs4 import BeautifulSoup
import requests

def web_scraping(url, elementos_a_extraer):
    """
    Función reutilizable para realizar web scraping en cualquier página web.

    Parámetros:
    - url (str): URL de la página web a analizar.
    - elementos_a_extraer (dict): Diccionario con los elementos a extraer y sus selectores.

    Retorno:
    - dict: Diccionario con los datos extraídos.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    }

    # Realizamos la solicitud
    response = requests.get(url, headers=headers)

    # Verificamos el estado de la solicitud
    if response.status_code != 200:
        print(f"Error en la solicitud: {response.status_code}")
        return None

    # Analizamos el contenido HTML con BeautifulSoup
    sopa = BeautifulSoup(response.content, "html.parser")

    # Extraemos los datos según los selectores
    datos_extraidos = {}
    for nombre, selector in elementos_a_extraer.items():
        if selector.get("tipo") == "texto":
            datos_extraidos[nombre] = [elem.getText() for elem in sopa.select(selector["selector"])]
        elif selector.get("tipo") == "atributo":
            datos_extraidos[nombre] = [elem.get(selector["atributo"]) for elem in sopa.select(selector["selector"])]

    return datos_extraidos
```

### **Explicación de la función**

1. **Parámetros de entrada**:
    - `url`: La dirección web de la página de la que queremos extraer datos.
    - `elementos_a_extraer`: Un diccionario que define qué elementos queremos extraer y cómo hacerlo. Cada clave del diccionario es un nombre para los datos extraídos, y el valor es otro diccionario con los siguientes campos:
        - `selector`: El selector CSS para ubicar los elementos en el HTML.
        - `tipo`: Define si queremos extraer texto (`"texto"`) o un atributo (`"atributo"`).
        - `atributo`: (Opcional) Especifica el atributo a extraer si el tipo es `"atributo"`.
2. **Cabeceras**:
Usamos un encabezado `User-Agent` para evitar bloqueos por parte de servidores que detectan solicitudes automatizadas.
3. **Procesamiento de datos**:
    - Analizamos el HTML con BeautifulSoup.
    - Recorremos los elementos definidos en `elementos_a_extraer` para buscar y extraer los datos según el selector proporcionado.

### **Ejemplo de uso**

Veamos cómo utilizar esta función para extraer datos de la página de inicio de Wikipedia.

```python
# Definimos la URL y los elementos a extraer
url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
elementos_a_extraer = {
    "titulo": {"selector": "title", "tipo": "texto"},
    "enlaces": {"selector": "a", "tipo": "atributo", "atributo": "href"},
    "imagenes": {"selector": "img", "tipo": "atributo", "atributo": "src"},
}

# Llamamos a la función
datos_extraidos = web_scraping(url, elementos_a_extraer)

# Mostramos los resultados
print("Título de la página:", datos_extraidos["titulo"])
print("Primeros 5 enlaces:", datos_extraidos["enlaces"][:5])
print("Primeras 5 imágenes:", datos_extraidos["imagenes"][:5])
```

### **Ejemplo de salida**

```
Título de la página: ['Wikipedia, la enciclopedia libre']
Primeros 5 enlaces: ['#content', '/wiki/Portada', '/wiki/Wikipedia:Portal_de_la_comunidad', '/wiki/Wikipedia:Actualidad', '/wiki/Especial:CambiosRecientes']
Primeras 5 imágenes: ['/static/images/icons/wikipedia.png', '/static/images/mobile/copyright/wikipedia-wordmark-en.svg', '/static/images/mobile/copyright/wikipedia-tagline-es.svg', '//upload.wikimedia.org/wikipedia/commons/thumb/8/86/Madonna-Like_A_Virgin-CD.png/220px-Madonna-Like_A_Virgin-CD.png', '//upload.wikimedia.org/wikipedia/commons/thumb/b/b3/OOjs_UI_icon_ellipsis.svg/20px-OOjs_UI_icon_ellipsis.svg.png']
```

### **Ventajas de esta implementación**

- **Reusabilidad**: La función puede usarse para extraer datos de cualquier página web simplemente definiendo nuevos selectores.
- **Flexibilidad**: Soporta tanto la extracción de texto como de atributos específicos.
- **Modularidad**: Facilita la ampliación o modificación del scraping sin cambiar la lógica principal.

# **Extracción de datos de zapatillas en eBay**

En este punto, aplicaremos las técnicas de web scraping para extraer información específica de una página web de eBay que contiene zapatillas. Nuestro objetivo es construir un **DataFrame** que incluya los siguientes datos:

- Descripción del producto.
- Precio del producto.
- Gastos de envío.
- Tipo de vendedor.
- URL de la imagen.

### **Configuración inicial**

Comenzamos por importar las bibliotecas necesarias y definir la URL de la página web.

```python
from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL de la página web
url_zapatillas = "https://www.ebay.es/e/_moda/adidassneakerses?_pgn=1"

# Solicitud HTTP
response = requests.get(url_zapatillas)

# Verificamos el estado de la solicitud
if response.status_code == 200:
    print(f"Solicitud exitosa: {response.status_code}")
else:
    print(f"Error en la solicitud: {response.status_code}")
```

### **Análisis del HTML**

Creamos un objeto `BeautifulSoup` para analizar el contenido de la página web.

```python
# Creamos un objeto BeautifulSoup
sopa_zapatillas = BeautifulSoup(response.content, "html.parser")

# Mostramos una parte del HTML estructurado para entender su formato
print(sopa_zapatillas.prettify()[:500])  # Mostramos los primeros 500 caracteres
```

Con esta salida, identificamos las etiquetas y clases que contienen los datos que queremos extraer.

### **Extracción de la descripción del producto**

Buscamos las descripciones de los productos utilizando la clase correspondiente (`s-item__title`).

```python
# Extraemos las descripciones
lista_descripcion_producto = sopa_zapatillas.findAll("h3", {"class": "s-item__title"})

# Mostramos los primeros resultados
for i, desc in enumerate(lista_descripcion_producto[:5]):
    print(f"Descripción {i + 1}: {desc.getText()}")

# Guardamos las descripciones en una lista
descripcion_productos = [desc.getText() for desc in lista_descripcion_producto]
```

### **Extracción del precio del producto**

Buscamos los precios de las zapatillas con la clase `s-item__price`.

```python
# Extraemos los precios
lista_precios = sopa_zapatillas.findAll("span", {"class": "s-item__price"})

# Mostramos los primeros resultados
for i, precio in enumerate(lista_precios[:5]):
    print(f"Precio {i + 1}: {precio.getText()}")

# Limpiamos y convertimos los precios a números
precio_productos = [float(precio.getText().split()[0].replace(",", ".").replace("EUR", "")) for precio in lista_precios]
```

### **Extracción de los gastos de envío**

Buscamos los gastos de envío utilizando la clase `s-item__shipping`.

```python
# Extraemos los gastos de envío
lista_gastos_envio = sopa_zapatillas.findAll("span", {"class": "s-item__shipping s-item__logisticsCost"})

# Mostramos los primeros resultados
for i, envio in enumerate(lista_gastos_envio[:5]):
    print(f"Gastos de envío {i + 1}: {envio.getText()}")

# Limpiamos y convertimos los gastos de envío
gastos_envio = [
    0 if envio.getText().split()[0] == "Envío" else float(envio.getText().split()[0].replace(",", ".").replace("EUR", ""))
    for envio in lista_gastos_envio
]
```

### **Extracción del tipo de vendedor**

Extraemos si el vendedor es una empresa o un particular usando la clase `s-item__subtitle`.

```python
# Extraemos el tipo de vendedor
lista_tipo_vendedor = sopa_zapatillas.findAll("div", {"class": "s-item__subtitle"})

# Mostramos los primeros resultados
for i, tipo in enumerate(lista_tipo_vendedor[:5]):
    print(f"Tipo de vendedor {i + 1}: {tipo.getText()}")

# Guardamos los tipos de vendedor en una lista
tipo_vendedor = [tipo.getText() for tipo in lista_tipo_vendedor]
```

### **Extracción de la URL de la imagen**

Extraemos las URLs de las imágenes de las zapatillas con el atributo `src` en la clase `s-item__image-img`.

```python
# Extraemos las imágenes
lista_imagenes = sopa_zapatillas.findAll("img", {"class": "s-item__image-img"})

# Mostramos los primeros resultados
for i, imagen in enumerate(lista_imagenes[:5]):
    print(f"Imagen {i + 1}: {imagen.get('src')}")

# Guardamos las URLs de las imágenes en una lista
imagenes_producto = [imagen.get("src") for imagen in lista_imagenes]
```

### **Creación de un DataFrame**

Finalmente, combinamos todas las listas extraídas en un **DataFrame** para analizar los datos.

```python
# Creamos un DataFrame
df_zapatillas = pd.DataFrame({
    "Descripción": descripcion_productos,
    "Precio (€)": precio_productos,
    "Gastos de Envío (€)": gastos_envio,
    "Tipo de Vendedor": tipo_vendedor,
    "Imagen": imagenes_producto
})

# Mostramos las primeras filas
print(df_zapatillas.head())
```

### **Guardar el DataFrame en un archivo CSV**

Podemos guardar los datos extraídos en un archivo CSV para un análisis posterior.

```python
# Guardamos el DataFrame en un archivo CSV
ruta_guardado = "zapatillas_ebay.csv"
df_zapatillas.to_csv(ruta_guardado, index=False, encoding="utf-8")
print(f"Datos guardados en {ruta_guardado}")
```

### **Salida esperada**

```
Descripción            Precio (€)    Gastos de Envío (€)    Tipo de Vendedor    Imagen
0 Adidas Zapatos...    106.94        0.0                   Empresa             https://...
1 Adidas Crazy...      160.27        6.16                  Empresa             https://...
...
```

# **Extracción de datos del IBEX-35**

En este apartado, aplicaremos técnicas de **web scraping** para extraer datos de las tablas del histórico de precios del índice IBEX-35. El objetivo es construir un **DataFrame** que contenga:

- Fecha.
- Precio.
- Variación porcentual.
- Máximo.
- Mínimo.
- Apertura.

### **Configuración inicial**

Primero, configuramos las librerías necesarias y realizamos la solicitud HTTP a la página web del IBEX-35.

```python
from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL de la página web
url_ibex = "https://www.bolsamania.com/indice/IBEX-35/historico-precios"

# Realizamos la solicitud HTTP
response = requests.get(url_ibex)

# Verificamos el estado de la solicitud
if response.status_code == 200:
    print(f"Solicitud exitosa: {response.status_code}")
else:
    print(f"Error en la solicitud: {response.status_code}")
```

### **Análisis del HTML**

Utilizamos `BeautifulSoup` para analizar el contenido de la página web y mostrar una parte del HTML para identificar las tablas.

```python
# Creamos un objeto BeautifulSoup
sopa_ibex = BeautifulSoup(response.content, "html.parser")

# Mostramos parte del HTML para entender su estructura
print(sopa_ibex.prettify()[:500])  # Mostramos los primeros 500 caracteres
```

Analizando el HTML, identificamos que la tabla de interés es la tercera en la estructura del documento.

### **Extracción de la tabla**

Buscamos las tablas presentes en la página web y seleccionamos la tercera.

```python
# Extraemos todas las tablas del HTML
tablas = sopa_ibex.findAll("table")

# Verificamos el número de tablas encontradas
print(f"Cantidad de tablas encontradas: {len(tablas)}")

# Seleccionamos la tabla que contiene los datos históricos
tabla_ibex = tablas[2]
```

### **Extracción de los encabezados**

Extraemos los encabezados de la tabla utilizando las etiquetas `<th>`.

```python
# Extraemos los encabezados de la tabla
encabezados = [th.getText().strip() for th in tabla_ibex.findAll("th")]

# Mostramos los encabezados extraídos
print(f"Encabezados: {encabezados}")
```

**Salida esperada:**

```
Encabezados: ['Fecha', 'Precio', 'Variación %', 'Máximo', 'Mínimo', 'Apertura']
```

### **Extracción de las filas de datos**

Extraemos las filas de datos utilizando las etiquetas `<tr>` y limpiamos los datos.

```python
# Extraemos todas las filas de la tabla
filas = tabla_ibex.findAll("tr")[1:]  # Excluimos la primera fila (encabezados)

# Procesamos cada fila para extraer las celdas de datos
datos = []
for fila in filas:
    celdas = [celda.getText().strip() for celda in fila.findAll("td")]
    datos.append(celdas)

# Mostramos las primeras filas de datos
print(f"Primeras filas de datos: {datos[:2]}")
```

**Salida esperada:**

```
Primeras filas de datos:
[['16-sep-24', '11.581,000', '0,35%', '11.592,500', '11.510,000', '11.520,800'],
 ['17-sep-24', '11.703,400', '1,06%', '11.753,900', '11.620,700', '11.620,900']]
```

### **Limpieza de datos**

Convertimos los datos extraídos a un formato adecuado para análisis, eliminando caracteres no deseados y formateando los números.

```python
# Limpieza de datos
datos_limpios = []
for fila in datos:
    fila_limpia = []
    for elemento in fila:
        try:
            # Convertimos números al formato flotante
            elemento_limpio = float(elemento.replace("%", "").replace(".", "").replace(",", "."))
        except ValueError:
            # Si no es un número (por ejemplo, fechas), lo mantenemos como string
            elemento_limpio = elemento
        fila_limpia.append(elemento_limpio)
    datos_limpios.append(fila_limpia)

# Mostramos las primeras filas limpias
print(f"Datos limpios: {datos_limpios[:2]}")
```

**Salida esperada:**

```
Datos limpios:
[['16-sep-24', 11581.0, 0.35, 11592.5, 11510.0, 11520.8],
 ['17-sep-24', 11703.4, 1.06, 11753.9, 11620.7, 11620.9]]
```

### **Creación de un DataFrame**

Utilizamos Pandas para convertir los datos procesados en un **DataFrame**.

```python
# Creamos el DataFrame
df_ibex = pd.DataFrame(datos_limpios, columns=encabezados)

# Mostramos las primeras filas del DataFrame
print(df_ibex.head())
```

**Salida esperada:**

```
Fecha    Precio  Variación %    Máximo     Mínimo   Apertura
0  16-sep-24  11581.00        0.35  11592.50  11510.00  11520.80
1  17-sep-24  11703.40        1.06  11753.90  11620.70  11620.90
...
```

### **Análisis preliminar**

Realizamos un análisis básico de los datos utilizando métodos de Pandas.

```python
# Información del DataFrame
print(df_ibex.info())

# Estadísticas descriptivas
print(df_ibex.describe())

# Valores únicos en la columna "Variación %"
print(df_ibex["Variación %"].unique())
```

### **Guardar el DataFrame en un CSV**

Guardamos el DataFrame en un archivo CSV para su uso posterior.

```python
# Ruta para guardar el CSV
ruta_csv = "datos_ibex.csv"

# Guardamos el DataFrame en un archivo CSV
df_ibex.to_csv(ruta_csv, index=False, encoding="utf-8")
print(f"Datos guardados en {ruta_csv}")
```

# **Creación de una función genérica para scraping del IBEX-35**

Vamos a encapsular todo el proceso de extracción de datos en una función reutilizable. Esto nos permitirá ejecutar el scraping del IBEX-35 de manera más eficiente y aplicar el mismo enfoque para otras páginas con estructura similar.

### **Definición de la función**

La función realizará las siguientes tareas:

1. Enviar una solicitud HTTP a la página.
2. Analizar el HTML para identificar la tabla de interés.
3. Extraer y limpiar los datos de la tabla.
4. Crear y devolver un DataFrame con los datos.

```python
def extraer_tabla_ibex(url):
    """
    Función para extraer datos del IBEX-35 desde una URL dada.

    Parámetros:
        url (str): URL de la página web que contiene la tabla del IBEX-35.

    Retorna:
        pd.DataFrame: DataFrame con los datos extraídos y limpios.
    """
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd

    # Solicitud HTTP
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error en la solicitud: {response.status_code}")
        return None

    # Análisis del HTML
    sopa = BeautifulSoup(response.content, "html.parser")

    # Selección de la tabla
    tablas = sopa.findAll("table")
    if len(tablas) < 3:
        print("No se encontró la tabla deseada.")
        return None

    tabla_ibex = tablas[2]

    # Extracción de encabezados
    encabezados = [th.getText().strip() for th in tabla_ibex.findAll("th")]

    # Extracción de filas
    filas = tabla_ibex.findAll("tr")[1:]  # Excluimos los encabezados
    datos = []
    for fila in filas:
        celdas = [celda.getText().strip() for celda in fila.findAll("td")]
        datos.append(celdas)

    # Limpieza de datos
    datos_limpios = []
    for fila in datos:
        fila_limpia = []
        for elemento in fila:
            try:
                # Convertimos números al formato flotante
                elemento_limpio = float(elemento.replace("%", "").replace(".", "").replace(",", "."))
            except ValueError:
                # Si no es un número, lo mantenemos como string
                elemento_limpio = elemento
            fila_limpia.append(elemento_limpio)
        datos_limpios.append(fila_limpia)

    # Creación del DataFrame
    df = pd.DataFrame(datos_limpios, columns=encabezados)
    return df
```

### **Uso de la función**

Probamos la función con la URL del IBEX-35.

```python
# URL del IBEX-35
url_ibex = "https://www.bolsamania.com/indice/IBEX-35/historico-precios"

# Llamamos a la función y guardamos el resultado
df_ibex = extraer_tabla_ibex(url_ibex)

# Mostramos las primeras filas del DataFrame resultante
if df_ibex is not None:
    print(df_ibex.head())
```

**Salida esperada:**

```
Fecha    Precio  Variación %    Máximo     Mínimo   Apertura
0  16-sep-24  11581.00        0.35  11592.50  11510.00  11520.80
1  17-sep-24  11703.40        1.06  11753.90  11620.70  11620.90
...
```

### **Guardado de datos en un archivo CSV**

Podemos guardar los datos extraídos en un archivo CSV para su análisis posterior.

```python
# Verificamos si el DataFrame contiene datos
if df_ibex is not None:
    ruta_guardado = "datos_ibex.csv"
    df_ibex.to_csv(ruta_guardado, index=False, encoding="utf-8")
    print(f"Datos guardados en {ruta_guardado}")
```

### **Ampliación de la funcionalidad**

Podemos extender la función para:

1. **Scraping dinámico**: Extraer datos de varias páginas iterando sobre diferentes URLs.
2. **Automatización**: Integrar un sistema que actualice automáticamente los datos del IBEX-35 periódicamente.
3. **Visualización**: Crear gráficos con Pandas o Matplotlib para representar las tendencias de los datos extraídos.

# **Uso avanzado: Automatización del scraping de múltiples páginas**

En esta sección, vamos a ampliar la funcionalidad de nuestro scraping para automatizar la extracción de datos de múltiples páginas web. Esto es útil cuando los datos que queremos obtener están distribuidos en varias páginas de un sitio web.

### **Automatización del scraping**

La idea principal es iterar sobre un rango de URLs que correspondan a diferentes páginas. Por ejemplo, si cada página tiene un número en su URL (`?_page=1`, `?_page=2`, etc.), podemos usar un bucle para generar dinámicamente estas URLs.

### **Código para extraer datos de múltiples páginas**

```python
def extraer_datos_multiplas_paginas(base_url, paginas):
    """
    Función para extraer datos de múltiples páginas web.

    Parámetros:
        base_url (str): URL base del sitio web.
        paginas (int): Número de páginas a extraer.

    Retorna:
        pd.DataFrame: DataFrame con los datos de todas las páginas.
    """
    import pandas as pd

    # Lista para almacenar los datos de todas las páginas
    datos_completos = []

    # Iteramos sobre el rango de páginas
    for pagina in range(1, paginas + 1):
        url = f"{base_url}?_page={pagina}"
        print(f"Extrayendo datos de la página: {url}")

        # Llamamos a la función que extrae datos de una sola página
        df_pagina = extraer_tabla_ibex(url)

        if df_pagina is not None:
            datos_completos.append(df_pagina)
        else:
            print(f"Error al procesar la página {pagina}.")

    # Concatenamos los datos en un único DataFrame
    if datos_completos:
        df_completo = pd.concat(datos_completos, ignore_index=True)
        return df_completo
    else:
        print("No se extrajeron datos.")
        return None
```

### **Uso de la función**

Probamos la función para extraer datos de varias páginas del IBEX-35. Suponemos que la URL base sigue un patrón de paginación.

```python
# URL base del IBEX-35
url_base = "https://www.bolsamania.com/indice/IBEX-35/historico-precios"

# Número de páginas a extraer
num_paginas = 5

# Llamamos a la función para extraer datos de todas las páginas
df_ibex_completo = extraer_datos_multiplas_paginas(url_base, num_paginas)

# Mostramos las primeras filas del DataFrame resultante
if df_ibex_completo is not None:
    print(df_ibex_completo.head())
```

**Salida esperada:**

```
Extrayendo datos de la página: https://www.bolsamania.com/indice/IBEX-35/historico-precios?_page=1
Extrayendo datos de la página: https://www.bolsamania.com/indice/IBEX-35/historico-precios?_page=2
Extrayendo datos de la página: https://www.bolsamania.com/indice/IBEX-35/historico-precios?_page=3
...
```

### **Guardado de los datos extraídos**

Podemos guardar los datos combinados en un archivo CSV.

```python
# Guardamos los datos en un archivo CSV
if df_ibex_completo is not None:
    ruta_guardado = "datos_ibex_completo.csv"
    df_ibex_completo.to_csv(ruta_guardado, index=False, encoding="utf-8")
    print(f"Datos guardados en {ruta_guardado}")
```

### **Consideraciones adicionales**

1. **Paginación dinámica**: Algunas páginas no incluyen paginación explícita. En ese caso, podríamos necesitar analizar las etiquetas de navegación HTML para obtener las URLs de las páginas adicionales.
2. **Límite de solicitudes**: Si el sitio web tiene un límite de solicitudes por minuto (rate limiting), podemos introducir retrasos entre las solicitudes con `time.sleep()`.
3. **Manejo de errores**: Implementar manejo de excepciones para continuar el scraping incluso si una página falla.

### **Conclusión y próximas acciones**

Hemos desarrollado un sistema completo de scraping que:

- Extrae datos estructurados de páginas web.
- Los limpia y organiza en DataFrames.
- Permite automatizar la extracción para múltiples páginas.

# **Visualización de los datos extraídos**

Ahora que hemos automatizado el scraping y consolidado los datos en un DataFrame, podemos visualizarlos para obtener información valiosa. Usaremos bibliotecas como **Matplotlib** y **Seaborn** para crear gráficos que resalten tendencias y patrones en los datos.

### **Ejemplo de visualización con datos del IBEX-35**

Supongamos que el DataFrame `df_ibex_completo` tiene las siguientes columnas: `Fecha`, `Precio`, `Máximo`, `Mínimo`, `Apertura`, `Variación %`. Vamos a realizar algunas visualizaciones clave.

### **Visualización 1: Evolución de precios a lo largo del tiempo**

El objetivo es crear un gráfico de línea que muestre cómo el precio del IBEX-35 ha cambiado con el tiempo.

```python
import matplotlib.pyplot as plt
import pandas as pd

# Convertimos la columna Fecha al formato datetime
df_ibex_completo['Fecha'] = pd.to_datetime(df_ibex_completo['Fecha'], format='%d-%b-%y')

# Ordenamos los datos por fecha
df_ibex_completo = df_ibex_completo.sort_values('Fecha')

# Gráfico de la evolución de precios
plt.figure(figsize=(12, 6))
plt.plot(df_ibex_completo['Fecha'], df_ibex_completo['Precio'], label='Precio', linewidth=2)
plt.title('Evolución del precio del IBEX-35', fontsize=16)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Precio', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
```

### **Visualización 2: Distribución de las variaciones porcentuales**

Podemos visualizar cómo se distribuyen las variaciones porcentuales diarias del IBEX-35.

```python
import seaborn as sns

# Gráfico de distribución
plt.figure(figsize=(10, 6))
sns.histplot(df_ibex_completo['Variación %'], kde=True, bins=20, color='blue')
plt.title('Distribución de las variaciones porcentuales del IBEX-35', fontsize=16)
plt.xlabel('Variación %', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.grid(True)
plt.show()
```

### **Visualización 3: Comparación de valores máximos y mínimos**

Crearemos un gráfico de líneas para comparar los valores máximos y mínimos del IBEX-35 a lo largo del tiempo.

```python
# Gráfico de comparación de valores
plt.figure(figsize=(12, 6))
plt.plot(df_ibex_completo['Fecha'], df_ibex_completo['Máximo'], label='Máximo', linewidth=2, linestyle='--', color='green')
plt.plot(df_ibex_completo['Fecha'], df_ibex_completo['Mínimo'], label='Mínimo', linewidth=2, linestyle='--', color='red')
plt.title('Comparación de valores máximos y mínimos del IBEX-35', fontsize=16)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Valores', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
```

### **Visualización 4: Boxplot de precios**

Un boxplot es útil para entender la distribución y detectar valores atípicos en los precios.

```python
# Gráfico de caja para los precios
plt.figure(figsize=(8, 6))
sns.boxplot(data=df_ibex_completo, x='Precio', color='skyblue')
plt.title('Distribución de los precios del IBEX-35', fontsize=16)
plt.xlabel('Precio', fontsize=12)
plt.grid(True)
plt.show()
```

### **Visualización de los datos limpios**

Estos gráficos nos permiten obtener:

1. **Tendencias**: Identificar patrones en la evolución del precio del IBEX-35.
2. **Distribuciones**: Analizar cómo se comportan las variaciones porcentuales.
3. **Comparaciones**: Ver cómo se relacionan los valores máximos y mínimos.

# Exportar los gráficos en un informe automatizado

### **Paso 1: Generar los gráficos y guardarlos como imágenes**

Guardaremos los gráficos en formato PNG antes de incluirlos en el PDF.

```python
# Configuración
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Crear directorio para las imágenes
output_dir = "graficos_ibex"
os.makedirs(output_dir, exist_ok=True)

# Gráfico 1: Evolución de precios
plt.figure(figsize=(12, 6))
plt.plot(df_ibex_completo['Fecha'], df_ibex_completo['Precio'], label='Precio', linewidth=2)
plt.title('Evolución del precio del IBEX-35', fontsize=16)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Precio', fontsize=12)
plt.legend()
plt.grid(True)
plt.savefig(f"{output_dir}/evolucion_precio.png")
plt.close()

# Gráfico 2: Distribución de las variaciones porcentuales
plt.figure(figsize=(10, 6))
sns.histplot(df_ibex_completo['Variación %'], kde=True, bins=20, color='blue')
plt.title('Distribución de las variaciones porcentuales del IBEX-35', fontsize=16)
plt.xlabel('Variación %', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.grid(True)
plt.savefig(f"{output_dir}/variacion_porcentual.png")
plt.close()

# Gráfico 3: Comparación de valores máximos y mínimos
plt.figure(figsize=(12, 6))
plt.plot(df_ibex_completo['Fecha'], df_ibex_completo['Máximo'], label='Máximo', linewidth=2, linestyle='--', color='green')
plt.plot(df_ibex_completo['Fecha'], df_ibex_completo['Mínimo'], label='Mínimo', linewidth=2, linestyle='--', color='red')
plt.title('Comparación de valores máximos y mínimos del IBEX-35', fontsize=16)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Valores', fontsize=12)
plt.legend()
plt.grid(True)
plt.savefig(f"{output_dir}/comparacion_max_min.png")
plt.close()

# Gráfico 4: Boxplot de precios
plt.figure(figsize=(8, 6))
sns.boxplot(data=df_ibex_completo, x='Precio', color='skyblue')
plt.title('Distribución de los precios del IBEX-35', fontsize=16)
plt.xlabel('Precio', fontsize=12)
plt.grid(True)
plt.savefig(f"{output_dir}/boxplot_precios.png")
plt.close()
```

---

### **Paso 2: Crear el informe PDF**

Usaremos **ReportLab** para incluir las imágenes generadas y añadir descripciones.

```python
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet

# Configuración del documento
pdf_file = "informe_ibex.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter)
elements = []

# Estilos
styles = getSampleStyleSheet()

# Título
elements.append(Paragraph("Informe de análisis del IBEX-35", styles['Title']))
elements.append(Spacer(1, 12))

# Introducción
elements.append(Paragraph("Este informe contiene un análisis gráfico de los precios y variaciones del índice IBEX-35, incluyendo visualizaciones detalladas de los datos extraídos.", styles['BodyText']))
elements.append(Spacer(1, 12))

# Gráfico 1: Evolución de precios
elements.append(Paragraph("Evolución del precio del IBEX-35", styles['Heading2']))
elements.append(Image(f"{output_dir}/evolucion_precio.png", width=400, height=200))
elements.append(Spacer(1, 12))

# Gráfico 2: Distribución de las variaciones porcentuales
elements.append(Paragraph("Distribución de las variaciones porcentuales", styles['Heading2']))
elements.append(Image(f"{output_dir}/variacion_porcentual.png", width=400, height=200))
elements.append(Spacer(1, 12))

# Gráfico 3: Comparación de valores máximos y mínimos
elements.append(Paragraph("Comparación de valores máximos y mínimos", styles['Heading2']))
elements.append(Image(f"{output_dir}/comparacion_max_min.png", width=400, height=200))
elements.append(Spacer(1, 12))

# Gráfico 4: Boxplot de precios
elements.append(Paragraph("Distribución de los precios del IBEX-35", styles['Heading2']))
elements.append(Image(f"{output_dir}/boxplot_precios.png", width=400, height=200))
elements.append(Spacer(1, 12))

# Generar PDF
doc.build(elements)

print(f"Informe PDF generado: {pdf_file}")
```

### **Paso 3: Verificar y descargar el informe**

1. Revisa el archivo `informe_ibex.pdf` generado en el directorio actual.
2. Puedes personalizar el diseño del informe añadiendo más texto, encabezados o tablas.

# **Caso Práctico 1: Scraping de Books to Scrape**

[Scraping_Books_to_Scrape.ipynb](https://prod-files-secure.s3.us-west-2.amazonaws.com/46e22cad-2a77-477a-8815-1f60d4f32eea/c32de4e9-2cb9-4512-b933-fa3d424c689a/Scraping_Books_to_Scrape.ipynb)

En esta guía realizaremos un scraping del sitio [Books to Scrape](http://books.toscrape.com/) para extraer información sobre libros disponibles. Usaremos Python, `Beautiful Soup` para analizar el HTML, y `SQLite` para guardar los datos extraídos.

### **Objetivos**

1. Extraer información sobre los libros disponibles: título, precio y disponibilidad.
2. Usar `Beautiful Soup` para analizar la estructura del HTML.
3. Guardar los datos en una base de datos SQLite para su análisis posterior.

### **Paso 1: Instalar las Bibliotecas Necesarias**

Primero, instalaremos las bibliotecas `beautifulsoup4` y `requests`, que se necesitan para el scraping:

```python
import sys
!{sys.executable} -m pip install beautifulsoup4 requests

# Verificar las versiones instaladas
import bs4
import requests

print(f'BeautifulSoup4 versión: {bs4.__version__}')
print(f'Requests versión: {requests.__version__}')
```

Este paso asegura que el entorno esté correctamente configurado.

### **Paso 2: Descargar el HTML de Books to Scrape**

Usaremos la biblioteca `requests` para descargar el contenido de la página web.

```python
# URL de la página principal de Books to Scrape
url = 'http://books.toscrape.com/'

# Configurar las cabeceras HTTP
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

# Realizar la solicitud HTTP
response = requests.get(url, headers=headers)

# Verificar si la página fue descargada correctamente
if response.status_code == 200:
    print('Página descargada con éxito')
else:
    print(f'Error al descargar la página: {response.status_code}')
```

Este código descarga el contenido HTML de la página principal.

### **Paso 3: Analizar el HTML con Beautiful Soup**

Utilizaremos `Beautiful Soup` para analizar la estructura del HTML y explorar los datos disponibles.

```python
from bs4 import BeautifulSoup

# Analizar el contenido HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Mostrar una muestra del HTML para entender su estructura
print(soup.prettify()[:1000])
```

Este paso ayuda a identificar las etiquetas HTML que contienen la información que necesitamos.

### **Paso 4: Extraer Información de los Libros**

Extraeremos datos clave como el título, precio y disponibilidad de cada libro. Aseguraremos que el texto HTML tenga la codificación correcta y limpiaremos caracteres extraños en los precios.

```python
python
Copiar código
# Asegurar la codificación UTF-8
response.encoding = 'utf-8'

# Extraer información de los libros
libros = soup.find_all('article', {'class': 'product_pod'})
print(f'Se encontraron {len(libros)} libros')

libros_extraidos = []

for libro in libros:
    # Extraer título
    titulo = libro.h3.a['title']

    # Extraer y limpiar precio
    precio = libro.find('p', class_='price_color').text.replace('Â', '').replace('£', '').strip()
    precio = float(precio)

    # Extraer disponibilidad
    disponibilidad = libro.find('p', class_='instock availability').text.strip()

    # Guardar en la lista
    libros_extraidos.append({
        'titulo': titulo,
        'precio': precio,
        'disponibilidad': disponibilidad
    })

# Mostrar resultados
for libro in libros_extraidos:
    print(libro)
```

---

### **Paso 5: Guardar los Datos en SQLite**

Crearemos una base de datos SQLite para almacenar los datos extraídos.

```python
import sqlite3

# Conectar a SQLite y crear una tabla
conn = sqlite3.connect('books_data.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    precio REAL NOT NULL,
    disponibilidad TEXT NOT NULL
)''')
conn.commit()

# Insertar los datos extraídos
for libro in libros_extraidos:
    cursor.execute('''
    INSERT INTO libros (titulo, precio, disponibilidad)
    VALUES (?, ?, ?)
    ''', (libro['titulo'], libro['precio'], libro['disponibilidad']))

conn.commit()
conn.close()

print('Datos de los libros guardados correctamente')
```

Este paso garantiza que los datos se guarden de forma estructurada para un acceso posterior.

### **Paso 6: Verificar los Datos Almacenados**

Finalmente, consultaremos los datos almacenados para asegurarnos de que todo está correcto:

```python
# Conectar a la base de datos y consultar los datos
conn = sqlite3.connect('books_data.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM libros')
resultados = cursor.fetchall()

# Mostrar los resultados
for fila in resultados:
    print(fila)

conn.close()
```

### **Resumen**

Esta guía cubre todo el proceso de scraping de Books to Scrape:

1. Descarga y análisis del HTML.
2. Extracción de datos estructurados (título, precio, disponibilidad).
3. Almacenamiento en una base de datos SQLite.
4. Consulta de los datos almacenados.

# **Ejercicio Propuesto: Generar un Informe Automatizado con Gráficos y Datos**

**Objetivo del Ejercicio:**

Automatizar la creación de un informe en PDF que contenga gráficos y análisis descriptivos basados en un conjunto de datos proporcionado (por ejemplo, precios del IBEX-35). Los estudiantes deberán replicar los pasos aprendidos y personalizar el informe con su propio análisis.

### **Instrucciones:**

1. **Importación de datos:**
    - Descarga los datos del IBEX-35 desde [Bolsamanía - Histórico de Precios](https://www.bolsamania.com/indice/IBEX-35/historico-precios) o utiliza cualquier otro conjunto de datos similar con precios, fechas y métricas adicionales.
    - Guarda los datos en un archivo CSV para facilitar su manejo.
2. **Análisis exploratorio:**
    - Carga los datos utilizando Pandas.
    - Genera análisis descriptivos básicos (medias, máximos, mínimos) con el método `describe()` y visualiza los valores únicos de cada columna relevante.
3. **Visualizaciones:**
    - Crea al menos 3 gráficos diferentes:
        1. Gráfico de líneas que muestre la evolución de precios a lo largo del tiempo.
        2. Histograma de las variaciones porcentuales.
        3. Comparación de valores máximos y mínimos en un gráfico combinado.
    - Asegúrate de etiquetar los ejes y agregar títulos descriptivos a cada gráfico.
4. **Automatización del informe:**
    - Guarda los gráficos generados en formato PNG en un directorio temporal.
    - Usando `ReportLab`, genera un informe en PDF que incluya:
        - Un título y una introducción breve al análisis.
        - Cada gráfico con su descripción asociada.
        - Un resumen de las estadísticas descriptivas en una tabla.
5. **Entrega:**
    - Guarda el archivo PDF como `informe_ibex_estudiante.pdf`.
    - Opcional: Incluye una tabla final en el PDF con las métricas clave extraídas (por ejemplo, precio promedio, máxima variación, etc.).

### **Criterios de Evaluación:**

1. **Carga de datos correcta:** Los datos deben importarse correctamente desde un archivo CSV.
2. **Análisis exploratorio:** Se espera un análisis descriptivo claro y que los resultados sean interpretados correctamente.
3. **Calidad de los gráficos:** Los gráficos deben estar bien etiquetados y visualmente claros.
4. **Automatización del PDF:** El informe PDF debe incluir todos los gráficos y una explicación clara de cada uno.
5. **Documentación:** El código debe estar bien comentado y organizado.

### **Ejemplo de Salida Esperada:**

**Informe PDF**

- **Título:** "Análisis del IBEX-35: Evolución y Desempeño"
- **Secciones:**
    - Introducción: Breve descripción del análisis realizado.
    - Gráfico 1: Evolución de precios con explicación.
    - Gráfico 2: Distribución de variaciones porcentuales.
    - Gráfico 3: Comparación de valores máximos y mínimos.
    - Tabla: Estadísticas descriptivas (Precio promedio, Máximo, Mínimo, etc.).

### **Extensiones Opcionales:**

- Añade más gráficos, como boxplots o gráficos de dispersión.
- Integra funciones reutilizables para automatizar el proceso de generación de gráficos y del informe.