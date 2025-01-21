### **Objetivo del scraping**

Usaremos un ejemplo de la web de Books to Scrape, que está diseñada para practicar web scraping. Extraer información de todos los libros disponibles en la web, recorriendo cada página del sitio. Específicamente:

1. Título del libro.
2. Precio.
3. Disponibilidad.

---

### **Código paso a paso**

### **1. Configuración inicial del entorno**

Crea un entorno virtual y asegúrate de instalar Selenium:

```bash
# Crear un entorno virtual
python -m venv selenium_env

# Activar el entorno virtual
# En Windows:
selenium_env\Scripts\activate
# En macOS/Linux:
source selenium_env/bin/activate

# Instalar dependencias
pip install selenium webdriver-manager
```

---

### **2. Código para scraping**

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from time import sleep

# Configurar Selenium WebDriver
service = Service(ChromeDriverManager().install())
options = Options()
driver = webdriver.Chrome(service=service, options=options)

# URL inicial de la web
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# Página inicial
current_page = 1
books = []

try:
    while True:
        # Acceder a la URL de la página actual
        driver.get(base_url.format(current_page))
        sleep(2)  # Esperar a que la página cargue

        # Extraer información de los libros en la página actual
        book_elements = driver.find_elements("css selector", "article.product_pod")

        for book in book_elements:
            # Título
            title = book.find_element("css selector", "h3 > a").get_attribute("title")
            # Precio
            price = book.find_element("css selector", "p.price_color").text
            # Disponibilidad
            availability = book.find_element("css selector", "p.instock.availability").text.strip()

            books.append({
                "title": title,
                "price": price,
                "availability": availability
            })

        print(f"Página {current_page} procesada.")

        # Intentar encontrar el botón de siguiente página
        try:
            next_button = driver.find_element("css selector", "li.next > a")
            current_page += 1
        except NoSuchElementException:
            print("No hay más páginas.")
            break

finally:
    # Cerrar el navegador
    driver.close()
    driver.quit()

# Mostrar resultados
for book in books:
    print(f"Título: {book['title']}, Precio: {book['price']}, Disponibilidad: {book['availability']}")
```

---

### **Explicación del código**

1. **Configuración del navegador**:
    - Se usa `webdriver.Chrome` configurado con `Service` y `Options` para manejar el navegador.
    - `ChromeDriverManager` descarga automáticamente el ChromeDriver necesario.
2. **URL con paginación**:
    - El sitio web utiliza URLs con formato `http://books.toscrape.com/catalogue/page-{}.html`, lo que facilita recorrer páginas reemplazando `{}` con el número de página.
3. **Scraping de datos**:
    - Se buscan todos los elementos con el selector `article.product_pod` para obtener los libros en la página actual.
    - Se extraen el título, precio y disponibilidad de cada libro.
4. **Navegación a la siguiente página**:
    - Si existe un botón "Next" (`li.next > a`), Selenium avanza a la siguiente página.
    - Si no hay un botón "Next", el bucle termina.
5. **Manejo de errores**:
    - El bloque `try...finally` asegura que el navegador se cierre correctamente, incluso si ocurre un error.

---

### **Ejecución del código**

Guarda el script como `books_scraper.py` y ejecútalo:

```bash
python books_scraper.py
```

---

### **Resultado esperado**

La salida será algo similar a esta (resumida para una página):

```yaml
Página 1 procesada.
Página 2 procesada.
...
No hay más páginas.
Título: A Light in the Attic, Precio: £51.77, Disponibilidad: In stock
Título: Tipping the Velvet, Precio: £53.74, Disponibilidad: In stock
...
```

---

### **Ampliaciones posibles**

1. **Guardar en un archivo**: Almacena los datos en un archivo CSV o JSON.
2. **Manejo de excepciones**: Añade lógica para manejar errores de conexión o elementos faltantes.
3. **Optimización**: Usa un límite de páginas o un filtro en los datos para mejorar el rendimiento.