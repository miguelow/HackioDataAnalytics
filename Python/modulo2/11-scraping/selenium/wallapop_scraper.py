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
import time

# Configuración de Selenium WebDriver
service = Service(ChromeDriverManager().install())
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=options)

# URL base 
base_url = "https://es.wallapop.com/"
products = []
search_query = "moto"
button_clicked = False
PRODUCT_LIMIT = 200

def scrape_visible_products():
    """Función para scrapear los productos actualmente visibles en la página"""
    items = driver.find_elements(By.CSS_SELECTOR, "a.ItemCardList__item")
    new_products_found = False
    
    for item in items:
        if len(products) >= PRODUCT_LIMIT:
            return new_products_found

        try:
            title = item.find_element(By.CSS_SELECTOR, "p.ItemCard__title").text
            price = item.find_element(By.CSS_SELECTOR, "span.ItemCard__price").text
            
            product_data = {
                "Title": title,
                "Price": price
            }
            
            if product_data not in products:
                products.append(product_data)
                new_products_found = True
                current_count = len(products)
                if current_count % 50 == 0:
                    print(f"Progreso: {current_count}/{PRODUCT_LIMIT} productos recolectados")
                
        except Exception as e:
            continue
            
    return new_products_found

def fast_scroll():
    """Realiza un scroll rápido para cargar más productos"""
    current_scroll = driver.execute_script("return window.pageYOffset;")
    window_height = driver.execute_script("return window.innerHeight;")
    scroll_increment = window_height * 2  # Scroll de 2 pantallas cada vez
    
    driver.execute_script(f"window.scrollTo({current_scroll}, {current_scroll + scroll_increment});")
    time.sleep(1)  # Espera mínima para que carguen los elementos

try:
    driver.get(base_url)
    wait = WebDriverWait(driver, 10)

    # Aceptar cookies
    try:
        cookie_button = wait.until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        cookie_button.click()
        print("Cookies aceptadas exitosamente")
        time.sleep(1)
    except Exception as e:
        print(f"Error al aceptar cookies: {str(e)}")

    # Buscar y usar el campo de búsqueda
    search_box = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input#searchbox-form-input"))
    )
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)

    attempts = 0
    max_attempts = 20

    while len(products) < PRODUCT_LIMIT and attempts < max_attempts:
        new_products_found = scrape_visible_products()
        
        if len(products) >= PRODUCT_LIMIT:
            break
            
        if not button_clicked:
            try:
                load_more_button = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "walla-button#btn-load-more"))
                )
                
                driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    load_more_button
                )
                time.sleep(1)
                
                try:
                    load_more_button.click()
                except:
                    driver.execute_script("arguments[0].click();", load_more_button)
                    
                print("Se hizo clic en 'Ver más productos'")
                button_clicked = True
                time.sleep(2)
                
            except Exception as e:
                attempts += 1
        else:
            try:
                # Usar la función de scroll rápido
                fast_scroll()
                
                # Verificar si llegamos al final
                current_height = driver.execute_script("return document.body.scrollHeight")
                if not new_products_found:
                    attempts += 1
                
            except Exception as e:
                attempts += 1
            
        if not new_products_found:
            attempts += 1

except Exception as e:
    print(f"Error general: {str(e)}")

finally:
    driver.quit()

# Convertir los datos en un DataFrame
df = pd.DataFrame(products)
df.to_csv("scraped_products.csv", index=False)
print(f"\nScraping completado. Se obtuvieron {len(products)} productos de {PRODUCT_LIMIT} objetivo.")
print("Datos guardados en 'scraped_products.csv'.")