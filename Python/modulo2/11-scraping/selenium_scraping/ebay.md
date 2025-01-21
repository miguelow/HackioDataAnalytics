### **Guía Completa para Realizar Scraping en eBay con Selenium**

Este código utiliza Selenium para realizar scraping en eBay, buscando productos relacionados con "Marvel". Además, incorpora manejo avanzado de excepciones, tiempo de espera dinámico, y estrategias de selección múltiple para mejorar la robustez del scraping.

### **1. Configuración Inicial**

1. **Instalar las bibliotecas necesarias**

Asegúrate de tener un entorno virtual configurado y luego instala las bibliotecas requeridas:

```bash
# Crear y activar un entorno virtual (opcional)
python -m venv ebay_scraping_env
source ebay_scraping_env/bin/activate  # En macOS/Linux
ebay_scraping_env\Scripts\activate    # En Windows

# Instalar dependencias
pip install selenium webdriver-manager pandas
```

1. **Verificar Google Chrome**

Asegúrate de tener una versión actualizada de Google Chrome, ya que `webdriver-manager` descargará el ChromeDriver compatible automáticamente.

---

### **2. Código para Scraping**

### **Descripción del Flujo**

1. **Abrir la página base de eBay**: Navega a `https://www.ebay.es`.
2. **Buscar el campo de entrada del buscador**: Usa varios selectores posibles para localizar el campo de búsqueda.
3. **Introducir la palabra clave y buscar**: Escribe "Marvel" y simula un `Enter`.
4. **Extraer información de productos**: Por cada página, recopila:
    - Título del producto.
    - Precio.
    - Ventas (si están disponibles).
5. **Navegar entre páginas**: Utiliza el botón "Siguiente" para pasar a la siguiente página.
6. **Guardar los datos**: Almacena los datos en un archivo CSV.

---

### **Código Completo**

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd

# Configuración de Selenium WebDriver
service = Service(ChromeDriverManager().install())
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=options)

# URL base de eBay
base_url = "https://www.ebay.es"

# Inicialización de variables
products = []
current_page = 1
search_query = "Marvel"

try:
    # Abrir la página base
    driver.get(base_url)
    wait = WebDriverWait(driver, 10)

    # Lista de posibles selectores para el campo de búsqueda
    search_selectors = [
        "input#gh-ac",  # ID principal de búsqueda en eBay
        "input[name='_nkw']",  # Nombre alternativo del campo
        "input.search-box",  # Clase genérica de búsqueda
        "input[type='text']",  # Selector genérico
        "input[placeholder='Buscar artículos']"  # Placeholder en español
    ]

    # Intentar localizar el campo de búsqueda
    search_box = None
    for selector in search_selectors:
        try:
            search_box = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            print(f"Campo de búsqueda encontrado con el selector: {selector}")
            break
        except TimeoutException:
            continue

    if not search_box:
        print("No se pudo encontrar el campo de búsqueda con los selectores proporcionados.")
        raise Exception("Campo de búsqueda no encontrado.")

    # Introducir el término de búsqueda y buscar
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Comenzar a extraer datos de productos
    while True:
        print(f"Scraping página {current_page}...")

        # Esperar a que los productos se carguen
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".s-item")))

        # Extraer información de los productos
        items = driver.find_elements(By.CSS_SELECTOR, ".s-item")
        for item in items:
            try:
                title = item.find_element(By.CSS_SELECTOR, ".s-item__title").text
            except NoSuchElementException:
                title = None

            try:
                price = item.find_element(By.CSS_SELECTOR, ".s-item__price").text
            except NoSuchElementException:
                price = None

            try:
                sales = item.find_element(By.CSS_SELECTOR, ".s-item__hotness").text
            except NoSuchElementException:
                sales = None

            products.append({
                "Title": title,
                "Price": price,
                "Sales": sales
            })

        # Intentar encontrar el botón "Siguiente"
        try:
            next_button = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".pagination__next"))
            )
            if "disabled" in next_button.get_attribute("class"):
                print("Se alcanzó la última página.")
                break

            next_button.click()  # Hacer clic en "Siguiente"
            current_page += 1
        except TimeoutException:
            print("No se encontró el botón 'Siguiente'. Finalizando.")
            break

finally:
    driver.quit()

# Convertir los datos en un DataFrame y guardarlos en un CSV
df = pd.DataFrame(products)
df.to_csv("marvel_products_ebay.csv", index=False)
print("Scraping completado. Datos guardados en 'marvel_products_ebay.csv'.")
```

---

### **3. Resultado**

Este script realiza lo siguiente:

1. Abre la página de eBay.
2. Busca "Marvel" utilizando el buscador.
3. Extrae información de los productos, incluyendo:
    - **Título**: Nombre del producto.
    - **Precio**: Precio mostrado en la lista.
    - **Ventas**: Número de ventas si está disponible.
4. Navega automáticamente por todas las páginas de resultados hasta llegar a la última.
5. Guarda los datos en un archivo CSV llamado `marvel_products_ebay.csv`.

---

### **Consideraciones Adicionales**

1. **Tiempos de espera dinámicos**: Se utilizan `WebDriverWait` y `expected_conditions` para asegurarse de que los elementos estén cargados antes de interactuar con ellos.
2. **Resiliencia**: El código intenta localizar el buscador usando varios selectores.
3. **Términos de uso de eBay**: Este código debe usarse solo para fines educativos y cumplir con las políticas de uso de eBay.