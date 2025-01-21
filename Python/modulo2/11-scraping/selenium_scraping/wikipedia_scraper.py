from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Inicializamos el WebDriver
service = Service(ChromeDriverManager().install())
options = Options()
driver = webdriver.Chrome(service=service, options=options)

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