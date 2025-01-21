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