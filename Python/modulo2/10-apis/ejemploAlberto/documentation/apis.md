### **Introducción**

Para entender qué es una API, empecemos con una analogía. Imagina que estás en un restaurante. El menú representa los servicios disponibles (platos) y tú, como cliente, decides lo que deseas pedir. Una vez que eliges, el camarero actúa como intermediario entre tú y la cocina, llevando tu pedido y devolviéndote el plato que solicitaste.

De manera similar, en el mundo digital, una **API (Application Programming Interface)** funciona como el camarero, permitiendo que diferentes programas o sistemas interactúen entre sí para intercambiar información o ejecutar acciones.

### **Definición técnica**

Una **API** es un conjunto de reglas y protocolos que permite que una aplicación se comunique con otra. Estas reglas están diseñadas para definir cómo se deben realizar las solicitudes (peticiones) y cómo deben ser procesadas las respuestas. En términos simples, una API es un puente que conecta aplicaciones, software o servicios para que trabajen juntos de manera eficiente.

### **Ejemplos cotidianos de uso de APIs**

Las APIs están presentes en muchas de las actividades que realizamos en el día a día:

1. **Redes sociales**: Cuando usas una aplicación para publicar un tweet desde otra plataforma, estás utilizando la API de Twitter para hacerlo.
2. **Mapas y geolocalización**: Las aplicaciones como Uber o Lyft utilizan la API de Google Maps para mostrar la ubicación en tiempo real y calcular rutas.
3. **Pago en línea**: Cuando compras algo en línea y usas PayPal como método de pago, el sitio web utiliza la API de PayPal para procesar el pago.
4. **Datos del clima**: Aplicaciones que muestran el clima actual y pronósticos utilizan APIs, como la API de OpenWeatherMap, para obtener información meteorológica.

### **¿Por qué son importantes las APIs para Data?**

En el campo del análisis de datos, las APIs son fundamentales porque permiten:

- **Acceso a datos externos**: Extraer datos en tiempo real desde plataformas como redes sociales, servicios meteorológicos o bases de datos públicas.
- **Automatización de procesos**: Automatizar la recopilación y transformación de datos, haciendo más eficiente el flujo de trabajo.
- **Enriquecimiento de datos**: Completar datasets con información adicional proveniente de servicios externos.
- **Integración de sistemas**: Conectar herramientas y aplicaciones para centralizar datos o crear flujos de trabajo personalizados.

### **Aclaraciones clave para principiantes**

1. **API ≠ Base de datos**: Una API no es lo mismo que una base de datos. Aunque puede acceder a datos de una base de datos, la API solo ofrece acceso controlado a los datos, no a la base completa.
2. **API ≠ Interfaz de usuario**: Las APIs son invisibles para los usuarios finales; están diseñadas para que los sistemas interactúen, no para que las personas las usen directamente.

# **Tipos de APIs**

Una API puede tomar diferentes formas dependiendo de cómo está diseñada, cómo se utiliza y en qué contexto opera. A continuación, exploraremos los tipos principales de APIs, con ejemplos y explicaciones detalladas.

### **APIs Web**

### **¿Qué son?**

Las APIs web son interfaces que permiten que dos sistemas se comuniquen a través de internet utilizando el protocolo HTTP (el mismo que se usa para navegar en la web). Estas APIs son ideales para obtener datos de servicios o proporcionar funcionalidades accesibles en línea.

### **Ejemplo práctico: API de OpenWeatherMap**

Supongamos que estás desarrollando una aplicación de clima. Para mostrar la temperatura actual de una ciudad, puedes usar la API de OpenWeatherMap. A través de esta API, tu aplicación envía una solicitud a los servidores de OpenWeatherMap y recibe la temperatura como respuesta en formato JSON.

### **Características principales**:

- Accesibles desde cualquier lugar con conexión a internet.
- Utilizan métodos HTTP como `GET`, `POST`, `PUT`, y `DELETE`.
- Los datos suelen ser entregados en formatos estándar como **JSON** o **XML**.

### **APIs de Biblioteca**

### **¿Qué son?**

Las APIs de biblioteca son interfaces que proporcionan funciones o métodos para realizar tareas específicas dentro de un lenguaje de programación. Estas se incluyen en librerías o frameworks que los desarrolladores integran en sus proyectos.

### **Ejemplo práctico: NumPy en Python**

Si necesitas realizar operaciones matemáticas avanzadas en Python, puedes usar la API de NumPy. Por ejemplo, la función `numpy.mean()` permite calcular la media de un conjunto de números. Al usar esta función, estás interactuando con la API que NumPy ofrece.

### **Características principales**:

- Diseñadas para trabajar dentro de un lenguaje de programación específico (Python, Java, etc.).
- Requieren que la biblioteca esté instalada en tu proyecto.
- Ofrecen funciones listas para usar, como cálculos matemáticos, gráficos o procesamiento de datos.

### **APIs del Sistema Operativo**

### **¿Qué son?**

Estas APIs permiten que las aplicaciones interactúen con el sistema operativo subyacente. Proveen acceso a recursos como el sistema de archivos, la red o el hardware.

### **Ejemplo práctico: API de archivos en Windows**

Cuando usas Python para crear o leer un archivo en tu computadora, estás interactuando con la API de archivos del sistema operativo. Por ejemplo, el método `open("archivo.txt", "r")` usa las API de archivos de tu sistema operativo para acceder al archivo en el disco.

### **Características principales**:

- Proveen acceso controlado a recursos del sistema operativo.
- Son esenciales para aplicaciones que necesitan trabajar con hardware o gestionar recursos como la memoria.

### **APIs de Terceros**

### **¿Qué son?**

Estas APIs son desarrolladas por empresas o plataformas externas y proporcionan acceso a servicios que no están directamente integrados en tu software. Por ejemplo, plataformas de redes sociales, pasarelas de pago o servicios en la nube.

### **Ejemplo práctico: API de PayPal**

Si estás desarrollando una tienda en línea y deseas permitir pagos con PayPal, puedes usar su API. Cuando un cliente realiza un pago, tu aplicación usa la API para enviar los detalles del pago a PayPal, que procesa la transacción y devuelve la confirmación.

### **Características principales**:

- Proporcionadas por terceros y suelen requerir autenticación.
- Frecuentemente tienen límites de uso y costos asociados.
- Facilitan la integración de funcionalidades avanzadas sin necesidad de desarrollarlas desde cero.

### **APIs Internas**

### **¿Qué son?**

Son APIs diseñadas para ser usadas exclusivamente dentro de una organización. Estas APIs conectan diferentes sistemas internos para compartir datos o funcionalidades de manera segura.

### **Ejemplo práctico: Sistema de recursos humanos**

En una empresa, el sistema de gestión de recursos humanos podría tener una API que permita consultar el estado de los empleados o actualizar información como sus horas trabajadas. Esta API solo estaría disponible dentro de la red interna de la empresa.

### **Características principales**:

- No están disponibles públicamente; solo pueden ser usadas por sistemas autorizados.
- Ayudan a conectar aplicaciones internas de manera eficiente.
- Suelen diseñarse para necesidades específicas de la organización.

### **APIs Abiertas (Open APIs)**

### **¿Qué son?**

Son APIs públicas que cualquier desarrollador puede usar sin restricciones significativas. Estas APIs fomentan la innovación al permitir que cualquiera las incorpore en sus proyectos.

### **Ejemplo práctico: API de Open Brewery**

La API de Open Brewery permite acceder a información sobre cervecerías en Estados Unidos. Puedes usar esta API para crear aplicaciones que muestren información de cervecerías por ciudad o estado sin necesidad de autenticación.

### **Características principales**:

- Acceso público y gratuito (aunque pueden tener límites de uso).
- Documentación accesible para que los desarrolladores entiendan cómo utilizarlas.
- Usadas para experimentación, aprendizaje y desarrollo rápido de aplicaciones.

### **Resumen**

| **Tipo de API** | **Uso Principal** | **Ejemplo** |
| --- | --- | --- |
| APIs Web | Acceso a servicios o datos a través de internet. | OpenWeatherMap |
| APIs de Biblioteca | Funciones específicas dentro de un lenguaje. | NumPy |
| APIs del Sistema Operativo | Interacción con recursos del sistema operativo. | Manejo de archivos en Windows |
| APIs de Terceros | Integración de servicios externos. | PayPal, Twitter |
| APIs Internas | Conexión de sistemas dentro de una organización. | Gestión de recursos humanos |
| APIs Abiertas | Acceso público para fomentar la innovación. | Open Brewery |

# **Conceptos Importantes**

Trabajar con APIs requiere comprender una serie de conceptos clave. Estos conceptos proporcionan la base para interactuar correctamente con una API y aprovechar al máximo sus capacidades. En esta sección, desglosaremos los términos más relevantes, explicándolos desde cero y utilizando ejemplos prácticos para garantizar una comprensión completa.

### **Endpoints**

### **¿Qué son?**

Los *endpoints* son puntos de acceso específicos en una API. Representan la URL que utilizamos para realizar una operación particular, como obtener datos, enviar información o ejecutar una acción en un sistema externo.

### **Analogía**

Imagina una biblioteca con varias secciones: libros, revistas y DVDs. Cada sección es un *endpoint*. Si quieres buscar libros, irás directamente a la sección de libros. De manera similar, en una API, cada *endpoint* está diseñado para cumplir una función específica.

### **Ejemplo práctico: API de Open Brewery**

La API de Open Brewery ofrece varios *endpoints*:

1. **Obtener todas las cervecerías:**
    - URL: `https://api.openbrewerydb.org/breweries`
    - Este *endpoint* devuelve una lista completa de cervecerías.
2. **Filtrar cervecerías por ciudad:**
    - URL: `https://api.openbrewerydb.org/breweries?by_city=san_diego`
    - Este *endpoint* devuelve las cervecerías ubicadas en San Diego.
3. **Filtrar cervecerías por estado:**
    - URL: `https://api.openbrewerydb.org/breweries?by_state=california`
    - Este *endpoint* devuelve las cervecerías de California.

### **Resumen**

- Un *endpoint* es una URL específica que define la acción que queremos realizar en una API.
- Cada *endpoint* puede aceptar parámetros para personalizar la solicitud.

### **Métodos HTTP**

### **¿Qué son?**

Los métodos HTTP son instrucciones que indican a la API qué acción realizar en un *endpoint*. Los métodos más comunes son:

| **Método** | **Función** |
| --- | --- |
| **GET** | Solicitar datos (leer información). |
| **POST** | Enviar datos (crear nuevos recursos). |
| **PUT** | Actualizar datos existentes. |
| **DELETE** | Eliminar datos existentes. |

### **Ejemplo práctico: API de usuarios**

Supongamos que estás gestionando usuarios en una aplicación. Los métodos HTTP podrían usarse así:

1. **GET**: Obtener información de un usuario.
    - URL: `https://api.example.com/users/123`
    - Acción: Obtiene los detalles del usuario con ID 123.
2. **POST**: Crear un nuevo usuario.
    - URL: `https://api.example.com/users`
    - Datos enviados: `{ "nombre": "Ana", "edad": 28 }`
    - Acción: Crea un usuario llamado Ana.
3. **PUT**: Actualizar la información de un usuario.
    - URL: `https://api.example.com/users/123`
    - Datos enviados: `{ "edad": 29 }`
    - Acción: Actualiza la edad del usuario 123 a 29.
4. **DELETE**: Eliminar un usuario.
    - URL: `https://api.example.com/users/123`
    - Acción: Elimina al usuario con ID 123.

### **Resumen**

- Los métodos HTTP determinan la acción que deseas realizar en un *endpoint*.
- **GET** es el método más utilizado en APIs, especialmente para obtener datos.

### **Solicitudes y Respuestas**

### **¿Qué son?**

Cuando interactúas con una API, realizas una **solicitud** (request) y recibes una **respuesta** (response). La solicitud es como enviar una carta con una pregunta, y la respuesta es la carta que recibes con la respuesta a tu pregunta.

### **Estructura de una solicitud**

Una solicitud incluye:

- **URL**: La dirección del *endpoint* (por ejemplo, `https://api.example.com/users`).
- **Método HTTP**: La acción que deseas realizar (GET, POST, etc.).
- **Parámetros** (opcional): Información adicional para personalizar la solicitud.
- **Cabeceras** (opcional): Metadatos como credenciales de autenticación.
- **Cuerpo** (solo para POST y PUT): Los datos que estás enviando.

### **Estructura de una respuesta**

Una respuesta incluye:

- **Código de estado**: Indica si la solicitud fue exitosa.
    - **200**: Éxito.
    - **404**: No encontrado.
    - **500**: Error interno del servidor.
- **Cuerpo**: Los datos devueltos (generalmente en formato JSON).

### **Ejemplo práctico: Obtener datos de cervecerías**

1. **Solicitud**:
    - URL: `https://api.openbrewerydb.org/breweries`
    - Método: GET.
2. **Respuesta**:
    
    ```json
    [
        {
            "id": "1",
            "name": "Brewery 1",
            "city": "San Diego",
            "state": "California"
        },
        {
            "id": "2",
            "name": "Brewery 2",
            "city": "Austin",
            "state": "Texas"
        }
    ]
    ```
    

### **Resumen**

- Una solicitud especifica lo que quieres de la API.
- Una respuesta contiene los datos que la API devuelve.

### **Autenticación**

### **¿Qué es?**

La autenticación es el proceso de verificar la identidad de quien realiza una solicitud a la API. Esto asegura que solo usuarios autorizados puedan acceder a los datos o funcionalidades.

### **Tipos de autenticación**

1. **Clave API (API Key)**:
    - Se incluye una clave única en la solicitud.
    - Ejemplo: `https://api.example.com/data?apikey=123456`.
2. **OAuth**:
    - Un sistema más avanzado que usa tokens de acceso.
    - Se utiliza en plataformas como Google o Facebook.
3. **Autenticación Básica**:
    - Requiere un nombre de usuario y contraseña.
    - Se envía como cabecera en la solicitud.

### **Ejemplo práctico: Autenticación con API Key**

Supongamos que estás usando la API de OMDb para obtener información de películas:

1. Solicitud con clave API:
    - URL: `http://www.omdbapi.com/?apikey=123456&t=Inception`.
2. Respuesta:
    
    ```json
    {
        "Title": "Inception",
        "Year": "2010",
        "Director": "Christopher Nolan"
    }
    ```
    

### **Resumen**

- La autenticación asegura que solo usuarios autorizados accedan a la API.
- **API Key** es el método más común y fácil de implementar.

### **Limitación de Tasa (Rate Limiting)**

### **¿Qué es?**

La limitación de tasa controla cuántas solicitudes puedes hacer a una API en un período de tiempo. Esto protege al servidor de sobrecargas.

### **Ejemplo práctico: Límite de 1,000 solicitudes por día**

Si estás usando la API de OMDb con un límite de 1,000 solicitudes diarias:

1. Si realizas 999 solicitudes, todo funciona bien.
2. Si haces una solicitud adicional, la API puede devolver un error 429 (demasiadas solicitudes).

### **Resumen**

- El límite de tasa protege el rendimiento de la API.
- Planifica tus solicitudes para evitar errores.

### **Formato de Datos**

### **¿Qué es?**

El formato de datos se refiere a cómo se estructuran los datos en las respuestas de una API. Los formatos más comunes son:

1. **JSON**:
    - Estructura basada en pares clave-valor.
    - Fácil de leer y usar en Python.
    - Ejemplo:
        
        ```json
        {
            "name": "Brewery 1",
            "city": "San Diego"
        }
        ```
        
2. **XML**:
    - Estructura jerárquica.
    - Menos común en APIs modernas.
    - Ejemplo:
        
        ```xml
        <brewery>
            <name>Brewery 1</name>
            <city>San Diego</city>
        </brewery>
        ```
        

### **Resumen**

- JSON es el formato más popular en APIs actuales.
- Asegúrate de saber cómo manejar el formato que utiliza la API.

### **Documentación**

### **¿Qué es?**

La documentación de una API es una guía que explica cómo usarla correctamente. Incluye:

- Lista de *endpoints* disponibles.
- Descripción de los parámetros.
- Ejemplos de solicitudes y respuestas.

### **Importancia**

La documentación es esencial para entender cómo interactuar con la API. Leerla detenidamente ahorra tiempo y evita errores.

# **Buenas Prácticas para Trabajar con APIs**

Cuando trabajamos con APIs, seguir buenas prácticas es crucial para maximizar la eficiencia, mantener la seguridad de los datos y garantizar que nuestro código sea reutilizable y fácil de mantener. A continuación, desglosaremos las principales recomendaciones que debes seguir al interactuar con APIs.

### **Comprender la Documentación**

### **¿Por qué es importante?**

La documentación de una API es tu principal fuente de información para entender cómo interactuar con ella. Te ayuda a:

- Identificar los *endpoints* disponibles.
- Entender qué parámetros se necesitan para cada solicitud.
- Interpretar los posibles códigos de respuesta y errores.

### **Consejo práctico**

Antes de escribir una sola línea de código, dedica tiempo a leer la documentación. Familiarízate con:

- Los *endpoints* principales.
- Los métodos HTTP que utiliza.
- Ejemplos de solicitudes y respuestas.

### **Ejemplo: Documentación de Open Brewery API**

La API de Open Brewery tiene un *endpoint* para filtrar cervecerías por ciudad:

1. **Endpoint**: `https://api.openbrewerydb.org/breweries`
2. **Parámetro**: `by_city`
3. **Ejemplo de solicitud**:
    - URL: `https://api.openbrewerydb.org/breweries?by_city=san_diego`
4. **Ejemplo de respuesta**:
    
    ```json
    [
        {
            "id": "1",
            "name": "Brewery 1",
            "city": "San Diego",
            "state": "California"
        }
    ]
    ```
    

### **Seleccionar la API Correcta**

### **¿Cómo hacerlo?**

No todas las APIs son iguales. Antes de elegir una API, evalúa:

- **Relevancia**: ¿La API proporciona los datos o funcionalidades que necesitas?
- **Confiabilidad**: ¿La API tiene una buena reputación? ¿Es estable?
- **Facilidad de uso**: ¿Está bien documentada? ¿Es fácil de implementar?
- **Límites de uso**: ¿Tiene restricciones que podrían afectar tu proyecto?
- **Costo**: ¿Es gratuita o de pago? ¿Se ajusta a tu presupuesto?

### **Ejemplo**

Supongamos que necesitas información meteorológica. Puedes comparar dos APIs:

1. **OpenWeatherMap API**:
    - Pros: Gratuita para uso básico, fácil de usar.
    - Contras: Límites estrictos en la cantidad de solicitudes diarias.
2. **WeatherStack API**:
    - Pros: Respuesta rápida, más detalles en los datos.
    - Contras: Planes gratuitos muy limitados.

### **Gestionar Credenciales de Forma Segura**

### **¿Por qué es importante?**

Las claves de API y tokens son como contraseñas. Si se exponen, alguien podría usarlas para consumir tus recursos o, peor aún, para realizar acciones indebidas.

### **Buenas prácticas**

1. **Usar variables de entorno**:
    - Almacena tus claves en un archivo `.env` y cárgalas en tu código utilizando bibliotecas como `python-dotenv`.
    
    ```python
    from dotenv import load_dotenv
    import os
    
    # Cargar las variables de entorno desde un archivo .env
    load_dotenv()
    
    # Obtener la clave de API
    api_key = os.getenv("API_KEY")
    ```
    
2. **Añadir `.env` al `.gitignore`**:
    - Asegúrate de que tu archivo `.env` no se suba a tu repositorio de Git.
    
    ```bash
    # .gitignore
    *.env
    ```
    
3. **Evitar incluir claves directamente en el código**:
    - Nunca expongas claves en tus scripts, especialmente si compartes tu código.

### **Manejar Errores de Forma Efectiva**

### **¿Por qué es importante?**

Los errores son inevitables cuando trabajas con APIs. Pueden deberse a problemas de red, errores en la solicitud o limitaciones de la API.

### **Tipos de errores comunes**

1. **Errores del cliente (4xx)**:
    - Ejemplo: 404 (No encontrado), 401 (No autorizado).
    - Solución: Verifica que la URL y los parámetros sean correctos.
2. **Errores del servidor (5xx)**:
    - Ejemplo: 500 (Error interno del servidor).
    - Solución: Intenta nuevamente más tarde o contacta al soporte de la API.
3. **Errores de conexión**:
    - Ejemplo: Tiempo de espera agotado.
    - Solución: Asegúrate de tener una conexión estable.

### **Ejemplo de manejo de errores**

```python
import requests

url = "https://api.example.com/data"

try:
    response = requests.get(url)
    response.raise_for_status()  # Verifica si hay errores HTTP
    data = response.json()
    print(data)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")
except Exception as err:
    print(f"An error occurred: {err}")
```

### **Documentar tu Código**

### **¿Por qué es importante?**

Documentar tu código facilita su comprensión y mantenimiento, tanto para ti como para otros desarrolladores.

### **Buenas prácticas**

1. **Comentarios claros**:
    - Explica qué hace cada parte del código.
    
    ```python
    # Realizar una solicitud GET a la API
    response = requests.get(url)
    ```
    
2. **Uso de docstrings**:
    - Describe el propósito de las funciones.
    
    ```python
    def obtener_datos(url):
        """
        Realiza una solicitud GET a la API y devuelve los datos en formato JSON.
        Args:
            url (str): La URL del endpoint de la API.
        Returns:
            dict: Los datos en formato JSON.
        """
        response = requests.get(url)
        return response.json()
    ```
    

### **Respetar los Límites de Llamadas**

### **¿Cómo hacerlo?**

Si una API tiene un límite de llamadas, implementa pausas en tu código para no excederlo.

### **Ejemplo**

```python
from time import sleep

# Llamar a la API en un bucle
for i in range(10):
    response = requests.get("https://api.example.com/data")
    print(response.json())

    # Pausa de 2 segundos entre solicitudes
    sleep(2)
```

### **Usar Funciones Reutilizables**

### **¿Por qué es importante?**

Encapsular tu lógica en funciones reutilizables hace que tu código sea más modular y fácil de mantener.

### **Ejemplo**

```python
def llamada_api(url, params=None):
    """
    Realiza una solicitud GET a la API.
    Args:
        url (str): URL del endpoint.
        params (dict): Parámetros de consulta.
    Returns:
        dict: Respuesta en formato JSON.
    """
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
```

# **Respuestas de las APIs**

Cuando trabajamos con APIs, obtener y manejar correctamente las respuestas es una de las tareas más importantes. Las respuestas contienen los datos solicitados o mensajes de error en caso de que algo haya salido mal. Es fundamental comprender cómo interpretar estas respuestas para poder integrarlas en nuestros proyectos.

### **¿Qué contiene una respuesta de una API?**

Una respuesta de una API incluye varios elementos, entre los cuales destacan:

1. **Código de Estado (Status Code)**:
    - Indica el resultado de la solicitud.
    - Ejemplos comunes:
        - `200`: Éxito.
        - `404`: No encontrado.
        - `401`: No autorizado.
        - `500`: Error interno del servidor.
2. **Cuerpo de la Respuesta (Response Body)**:
    - Contiene los datos solicitados, generalmente en formato JSON o XML.
3. **Encabezados de la Respuesta (Response Headers)**:
    - Proveen información adicional, como el tipo de contenido (`Content-Type`) o las políticas de caché.

### **Ejemplo de una respuesta en formato JSON**

```json
{
    "id": "1",
    "name": "Example Brewery",
    "city": "San Diego",
    "state": "California",
    "type": "micro"
}
```

## **Flujo de Trabajo con APIs**

Cuando trabajamos con APIs, podemos dividir el flujo de trabajo en cinco fases principales:

### **Fase 1: Comprender la API**

Antes de interactuar con una API, es fundamental entender cómo funciona. Esto incluye:

1. **Leer la documentación**:
    - Aprende sobre los *endpoints*, parámetros, métodos HTTP y tipos de respuesta.
    - Familiarízate con las limitaciones de uso y la autenticación.
2. **Obtener credenciales**:
    - Si la API requiere autenticación, asegúrate de registrar una cuenta y obtener tu clave API.

### **Ejemplo**

Supongamos que queremos usar la API de Open Brewery. El primer paso sería consultar su [documentación](https://www.openbrewerydb.org/) para identificar:

- Los *endpoints* disponibles.
- Qué parámetros acepta cada *endpoint*.
- Ejemplos de solicitudes y respuestas.

### **Fase 2: Realizar una Solicitud a la API**

Esta fase implica enviar una solicitud a la API utilizando un método HTTP, como GET o POST.

### **Pasos a seguir**

1. **Define la URL del *endpoint***:
    - Incluye la URL base y los parámetros necesarios.
    - Ejemplo: `https://api.openbrewerydb.org/breweries?by_city=san_diego`.
2. **Realiza la solicitud**:
    - Utiliza una biblioteca como `requests` en Python.
    
    ```python
    import requests
    url = "https://api.openbrewerydb.org/breweries?by_city=san_diego"
    response = requests.get(url)
    ```
    
3. **Verifica el estado de la solicitud**:
    - Comprueba el código de estado para asegurarte de que la solicitud fue exitosa.
    
    ```python
    if response.status_code == 200:
        print("Solicitud exitosa")
    else:
        print(f"Error: {response.status_code}")
    ```
    

### **Fase 3: Manejar la Respuesta**

Después de realizar la solicitud, necesitamos procesar los datos obtenidos.

### **Pasos a seguir**

1. **Convertir el cuerpo de la respuesta al formato adecuado**:
    - Por ejemplo, convierte el JSON en un diccionario para trabajar con los datos fácilmente.
    
    ```python
    data = response.json()
    print(data)
    ```
    
2. **Extraer información específica**:
    - Utiliza las claves del diccionario para acceder a los datos relevantes.
    
    ```python
    for brewery in data:
        print(f"Nombre: {brewery['name']}, Ciudad: {brewery['city']}")
    ```
    

### **Fase 4: Manejo de Errores**

Es posible que las solicitudes a la API fallen por diversas razones. En esta fase, gestionaremos esos errores de manera adecuada.

### **Tipos de errores comunes**

1. **Errores del cliente (4xx)**:
    - Ejemplo: `404` (Recurso no encontrado), `401` (No autorizado).
2. **Errores del servidor (5xx)**:
    - Ejemplo: `500` (Error interno del servidor).
3. **Errores de conexión y tiempo de espera**:
    - Ejemplo: No hay conexión a Internet, el servidor no responde.

### **Manejo de errores en Python**

Utiliza bloques `try-except` para capturar y manejar los errores:

```python
try:
    response = requests.get(url)
    response.raise_for_status()  # Lanza una excepción si hay un error HTTP
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Error de conexión: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error: {timeout_err}")
except Exception as err:
    print(f"Error inesperado: {err}")
```

### **Fase 5: Automatización y Buenas Prácticas**

### **Automatización del flujo de trabajo**

Crea funciones reutilizables para simplificar el proceso:

```python
def llamada_api(url, params=None):
    """
    Realiza una solicitud GET a la API.
    Args:
        url (str): URL del endpoint.
        params (dict): Parámetros de consulta.
    Returns:
        dict: Respuesta en formato JSON.
    """
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error al hacer la solicitud: {e}")
        return None
```

### **Buenas prácticas adicionales**

1. **Manejar autenticación de forma segura**:
    - Usa archivos `.env` para almacenar claves API.
2. **Documentar el código**:
    - Añade comentarios y *docstrings* para describir la funcionalidad de cada función.
3. **Controlar la frecuencia de solicitudes**:
    - Usa la función `sleep()` para respetar los límites de tasa.

# **API Open Brewery**

La **API Open Brewery** es un excelente punto de partida para aprender a trabajar con APIs. Proporciona información detallada sobre cervecerías en los Estados Unidos, y lo mejor de todo es que **no requiere autenticación ni límites estrictos de uso**. Esto la convierte en una herramienta ideal para explorar cómo funcionan las APIs.

### **Comprender la API Open Brewery**

Antes de interactuar con cualquier API, es fundamental leer su documentación. La API Open Brewery tiene su documentación disponible en [este enlace](https://www.openbrewerydb.org/). Según la documentación, esta API ofrece varios *endpoints* para buscar cervecerías según diferentes criterios.

### **Principales *Endpoints***

1. **Obtener todas las cervecerías**:
    - Devuelve una lista con todas las cervecerías en la base de datos.
    - URL: `https://api.openbrewerydb.org/breweries`
2. **Obtener cervecerías por ciudad**:
    - Filtra las cervecerías por ciudad.
    - URL: `https://api.openbrewerydb.org/breweries?by_city=san_diego`
3. **Obtener cervecerías por estado**:
    - Filtra las cervecerías por estado.
    - URL: `https://api.openbrewerydb.org/breweries?by_state=california`
4. **Obtener cervecerías por tipo**:
    - Filtra por tipo de cervecería, como `micro`, `nano`, `large`, etc.
    - URL: `https://api.openbrewerydb.org/breweries?by_type=micro`
5. **Buscar cervecerías por nombre**:
    - Encuentra cervecerías que coincidan con un término específico.
    - URL: `https://api.openbrewerydb.org/breweries?by_name=dog`

### **Formato de Respuesta**

La API Open Brewery devuelve las respuestas en formato JSON. Por ejemplo, al solicitar todas las cervecerías, la respuesta podría ser:

```json
[
    {
        "id": "10-barrel-brewing-co-bend",
        "name": "10 Barrel Brewing Co",
        "brewery_type": "large",
        "city": "Bend",
        "state": "Oregon",
        "country": "United States",
        "website_url": "http://www.10barrel.com",
        "phone": "5415851007",
        "street": "62970 18th St"
    }
]
```

### **Realizar la Primera Solicitud a la API**

Ahora que conocemos los *endpoints*, haremos una solicitud básica para obtener todas las cervecerías.

### **Configuración del Entorno**

Antes de empezar, asegúrate de tener instaladas las siguientes librerías de Python:

- `requests`: Para realizar solicitudes HTTP.
- `pandas`: Para organizar los datos en tablas estructuradas.
- `tqdm`: Para visualizar barras de progreso en procesos iterativos.

Si no las tienes instaladas, usa este comando:

```bash
pip install requests pandas tqdm
```

### **Código para la Solicitud**

```python
import requests  # Librería para interactuar con APIs
import pandas as pd  # Librería para manipulación de datos
from tqdm import tqdm  # Barra de progreso

# URL del endpoint para obtener todas las cervecerías
url = "https://api.openbrewerydb.org/breweries"

# Realizar la solicitud GET
response = requests.get(url)

# Verificar el estado de la respuesta
if response.status_code == 200:
    print("Solicitud exitosa")
else:
    print(f"Error: {response.status_code}")

# Convertir la respuesta a JSON
datos_cervecerias = response.json()

# Mostrar los dos primeros registros para inspeccionar los datos
print(datos_cervecerias[:2])
```

### **Extraer Información Específica**

La respuesta contiene muchos datos, pero podríamos estar interesados solo en algunos campos, como el nombre, tipo, ciudad, estado y dirección de las cervecerías. A continuación, organizaremos esta información en un DataFrame de Pandas.

### **Código para Organizar los Datos**

```python
# Crear un diccionario para almacenar los datos relevantes
diccionario_cervecerias = {
    "nombre": [],
    "tipo": [],
    "ciudad": [],
    "estado": [],
    "direccion": []
}

# Iterar sobre los datos y extraer información específica
for cerveceria in datos_cervecerias:
    diccionario_cervecerias["nombre"].append(cerveceria.get("name"))
    diccionario_cervecerias["tipo"].append(cerveceria.get("brewery_type"))
    diccionario_cervecerias["ciudad"].append(cerveceria.get("city"))
    diccionario_cervecerias["estado"].append(cerveceria.get("state"))
    diccionario_cervecerias["direccion"].append(cerveceria.get("street"))

# Convertir el diccionario en un DataFrame
df_cervecerias = pd.DataFrame(diccionario_cervecerias)

# Mostrar las primeras 5 filas del DataFrame
print(df_cervecerias.head())
```

### **Manejo de Errores**

Es posible que algo falle al realizar la solicitud. Implementemos un manejo básico de errores:

```python
try:
    response = requests.get(url)
    response.raise_for_status()  # Lanza una excepción si hay un error HTTP
    datos_cervecerias = response.json()
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Error de conexión: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error: {timeout_err}")
except Exception as err:
    print(f"Error inesperado: {err}")
```

### **Proyectos Sugeridos**

Con los datos extraídos, podríamos realizar proyectos interesantes como:

1. **Análisis de Popularidad**:
    - ¿Cuáles son los estados con más cervecerías?
    - ¿Qué tipos de cervecerías son los más comunes?
2. **Visualización Geográfica**:
    - Mapa interactivo de cervecerías por estado.
3. **Filtrado y Búsqueda**:
    - Implementar un sistema para buscar cervecerías según criterios específicos.

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

# **API OMDb**

La **API OMDb** (*Open Movie Database API*) es una herramienta poderosa para obtener información sobre películas, series y episodios. A diferencia de la API Open Brewery, esta API requiere una **clave de autenticación (API key)** para acceder a sus servicios, lo que nos introduce al concepto de **autenticación en APIs**.

### **Comprender la API OMDb**

La API OMDb permite buscar y recuperar información relacionada con producciones audiovisuales. Antes de comenzar, debemos registrarnos para obtener una clave API gratuita en [OMDb API](https://www.omdbapi.com/apikey.aspx).

### **Principales *Endpoints***

1. **Búsqueda por Título**:
    - Busca información detallada sobre una película, serie o episodio por su título.
    - URL base: `http://www.omdbapi.com/?apikey=[yourkey]&t=[titulo]`
2. **Búsqueda por ID (IMDb ID)**:
    - Busca información usando el ID único de IMDb.
    - URL: `http://www.omdbapi.com/?apikey=[yourkey]&i=[id]`
3. **Búsqueda por Palabra Clave**:
    - Devuelve una lista de títulos que coinciden con una palabra clave.
    - URL: `http://www.omdbapi.com/?apikey=[yourkey]&s=[palabra_clave]`
4. **Filtrado por Tipo**:
    - Filtra resultados por tipo (`movie`, `series`, `episode`).
    - URL: `http://www.omdbapi.com/?apikey=[yourkey]&t=[titulo]&type=[tipo]`
5. **Filtrado por Año**:
    - Filtra los resultados por año de lanzamiento.
    - URL: `http://www.omdbapi.com/?apikey=[yourkey]&t=[titulo]&y=[año]`
6. **Personalización de Trama (Plot)**:
    - Devuelve una trama breve o completa.
    - URL: `http://www.omdbapi.com/?apikey=[yourkey]&t=[titulo]&plot=[short/full]`

### **Formato de Respuesta**

La respuesta es un JSON con campos como:

```json
{
    "Title": "Inception",
    "Year": "2010",
    "Rated": "PG-13",
    "Released": "16 Jul 2010",
    "Runtime": "148 min",
    "Genre": "Action, Adventure, Sci-Fi",
    "Director": "Christopher Nolan",
    "Actors": "Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page",
    "Plot": "A thief who steals corporate secrets...",
    "Ratings": [
        {"Source": "Internet Movie Database", "Value": "8.8/10"},
        {"Source": "Rotten Tomatoes", "Value": "87%"},
        {"Source": "Metacritic", "Value": "74/100"}
    ]
}
```

### **Configuración del Entorno**

Para trabajar con la API OMDb, necesitas:

1. **Clave API**:
    - Regístrate en [OMDb API](https://www.omdbapi.com/apikey.aspx).
    - Guarda tu clave en un archivo `.env` para protegerla.
2. **Librerías**:
    - `python-dotenv`: Para manejar la clave API de forma segura.
    - `requests`: Para realizar solicitudes HTTP.
    - `pandas`: Para organizar los datos.

Si no tienes estas librerías, instálalas con:

```bash
pip install python-dotenv requests pandas
```

### **Archivo `.env`**

Crea un archivo llamado `.env` en tu proyecto y agrega:

```
OMDB_API_KEY='tu_clave_aqui'
```

### **Código para Cargar la Clave**

```python
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave API
api_key = os.getenv("OMDB_API_KEY")

# Confirmar que la clave se cargó correctamente (¡No mostrar la clave en producción!)
print(f"Clave API cargada: {api_key}")
```

### **Realizar Solicitudes a la API**

Comenzaremos con una búsqueda sencilla por título.

### **Código para Búsqueda por Título**

```python
import requests

# URL base de la API OMDb
base_url = "http://www.omdbapi.com/"

# Parámetros de la solicitud
titulo = "Inception"
params = {
    "apikey": api_key,
    "t": titulo
}

# Realizar la solicitud GET
response = requests.get(base_url, params=params)

# Verificar el estado de la respuesta
if response.status_code == 200:
    print("Solicitud exitosa")
else:
    print(f"Error: {response.status_code}")

# Convertir la respuesta a JSON
datos_pelicula = response.json()

# Mostrar la información obtenida
print(datos_pelicula)
```

### **Manejo de Errores**

La API puede devolver errores debido a un título no encontrado, una clave API incorrecta o una solicitud mal formada. Implementemos un manejo básico de errores.

### **Código para Manejo de Errores**

```python
try:
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Detecta errores HTTP
    datos_pelicula = response.json()

    if datos_pelicula.get("Response") == "False":
        print(f"Error en la búsqueda: {datos_pelicula.get('Error')}")
    else:
        print("Datos obtenidos con éxito")
        print(datos_pelicula)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Error de conexión: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Error de tiempo de espera: {timeout_err}")
except Exception as err:
    print(f"Error inesperado: {err}")
```

### **Proyectos Sugeridos**

Con la información obtenida, puedes realizar análisis interesantes como:

1. **Análisis Comparativo de Calificaciones**:
    - Compara las calificaciones de IMDb, Rotten Tomatoes y Metacritic.
2. **Enriquecimiento de Datos**:
    - Combina datos de OMDb con otros conjuntos de datos (como los de TMDB).
3. **Búsquedas Avanzadas**:
    - Implementa filtros por género, año o tipo.

### **Ejercicio Propuesto**

1. Realiza una búsqueda por palabra clave (`s`) para encontrar películas relacionadas con "Batman".
2. Extrae las calificaciones de todas las películas encontradas.
3. Calcula la calificación promedio de las películas en IMDb.
4. Crea un gráfico de barras con las calificaciones obtenidas.

# Guía API OMDb

## **Configuración del Entorno**

### **Configurar un entorno virtual**

Crea un entorno virtual para manejar las dependencias del proyecto de forma aislada:

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate

# Instalar las dependencias necesarias
pip install pandas numpy requests tqdm python-dotenv
```

### **Crear un archivo `requirements.txt`**

Para documentar las dependencias:

```bash
pip freeze > requirements.txt
```

### **Configurar el archivo `.env`**

Crea un archivo llamado `.env` en el directorio raíz y agrega tu clave API de OMDb:

```makefile
OMDB_API_KEY=tu_api_key
```

### **Actualizar el archivo `.gitignore`**

Asegúrate de excluir el entorno virtual y el archivo `.env`:

```bash
venv/
.env
```

## **Código Python**

### **Importar Librerías y Configurar Variables de Entorno**

```python
import pandas as pd
import numpy as np
import requests
from tqdm import tqdm
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
api_key = os.getenv("OMDB_API_KEY")

# Verificar que la clave API se haya cargado correctamente
if not api_key:
    raise ValueError("La clave de API de OMDb no se encuentra en el archivo .env.")
```

## **Cargar y Explorar el Conjunto de Datos**

### **Cargar el archivo CSV**

```python
# Cargar el conjunto de datos de TMDB
df_pelis = pd.read_csv("../Datos/Apis/Clase/TMDb_updated.CSV", index_col=0)

# Mostrar una muestra aleatoria de películas
print(df_pelis.sample(5))
```

### **Ejemplo de salida**

|  | title | overview | original_language | vote_count | vote_average |
| --- | --- | --- | --- | --- | --- |
| 1 | Spider-Man: Homecoming | A young Peter Parker... | en | 18045 | 7.4 |
| 2 | The Bank Job | Terry is a small-time... | en | 1270 | 6.8 |

## **Realizar Llamadas a la API**

### **Función para Hacer Llamadas a la API**

```python
def llamada_api_omdb(titulo, api_key):
    """Realiza una llamada a la API de OMDb para obtener información de una película."""
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={titulo}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar {titulo}: {e}")
        return None
```

### **Seleccionar Películas Aleatorias**

```python
# Seleccionar 100 títulos aleatorios del conjunto de datos
peliculas_aleatorias = df_pelis['title'].sample(n=100).values
print(f"Algunas películas seleccionadas: {peliculas_aleatorias[:5]}")
```

### **Realizar las Llamadas**

```python
# Crear un DataFrame vacío para almacenar los resultados
df_resultados = pd.DataFrame()

# Iterar por los títulos y obtener datos de la API
for titulo in tqdm(peliculas_aleatorias, desc="Consultando películas"):
    datos = llamada_api_omdb(titulo, api_key)
    if datos:
        # Convertir los datos de la API en un DataFrame de una fila
        df_temp = pd.DataFrame([{
            "titulo": datos.get("Title"),
            "director": datos.get("Director"),
            "elenco": datos.get("Actors"),
            "año_lanzamiento": datos.get("Year"),
            "genero": datos.get("Genre"),
            "calificaciones": datos.get("Ratings"),
            "premios": datos.get("Awards"),
            "poster": datos.get("Poster")
        }])
        df_resultados = pd.concat([df_resultados, df_temp], ignore_index=True)

    # Pausa para cumplir con el límite de llamadas por segundo
    sleep(2)

# Mostrar una muestra de los datos obtenidos
print(df_resultados.head())
```

## **Limpieza y Organización de Datos**

### **Extraer Calificaciones**

```python
# Extraer calificaciones de las plataformas IMDb, Rotten Tomatoes y Metacritic
def extraer_calificaciones(calificaciones):
    plataformas = ["Internet Movie Database", "Rotten Tomatoes", "Metacritic"]
    valores = {plataforma: None for plataforma in plataformas}
    if isinstance(calificaciones, list):
        for calificacion in calificaciones:
            plataforma = calificacion.get("Source")
            valor = calificacion.get("Value")
            if plataforma in plataformas:
                valores[plataforma] = valor
    return pd.Series(valores)

# Aplicar la función al DataFrame
df_calificaciones = df_resultados["calificaciones"].apply(extraer_calificaciones)

# Renombrar columnas
df_calificaciones.columns = ["cali_imdb", "cali_rotten", "cali_metacritic"]
```

### **Combinar Datos**

```python
# Combinar el DataFrame de calificaciones con el DataFrame principal
df_final = pd.concat([df_resultados, df_calificaciones], axis=1)

# Eliminar la columna original de calificaciones
df_final.drop(columns=["calificaciones"], inplace=True)

# Mostrar una muestra de los datos finales
print(df_final.head())
```

## **Ideas de Proyectos con los Datos**

1. **Análisis de Calificaciones**:
    - Comparar promedios y desviaciones estándar entre plataformas (IMDb, Rotten Tomatoes, Metacritic).
    - Identificar géneros con mejores o peores calificaciones.
2. **Tendencias de Géneros**:
    - Analizar cambios en la popularidad de géneros a lo largo del tiempo.
    - Relacionar géneros con premios y nominaciones.
3. **Impacto de Directores**:
    - Identificar directores con calificaciones consistentemente altas.
    - Relacionar premios con directores y géneros.