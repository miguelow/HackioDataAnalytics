### **Guía para Trabajar con Más Endpoints de una API: Métodos POST, PUT y DELETE**

En esta guía, trabajaremos con la API JSONPlaceholder, que es una API de prueba ideal para aprender y practicar métodos HTTP como **POST**, **PUT**, y **DELETE**.

---

### **1. Introducción a los Métodos HTTP**

- **GET**: Recuperar datos de la API.
- **POST**: Crear un nuevo recurso.
- **PUT/PATCH**: Actualizar un recurso existente.
    - **PUT** reemplaza completamente un recurso.
    - **PATCH** actualiza parcialmente un recurso.
- **DELETE**: Eliminar un recurso.

---

### **2. Configuración Inicial**

### **a. Crear un Entorno Virtual**

```bash
python -m venv venv
```

Activa el entorno virtual:

- **Windows**:
    
    ```bash
    venv\\Scripts\\activate
    ```
    
- **macOS/Linux**:
    
    ```bash
    source venv/bin/activate
    ```
    

### **b. Instalar Dependencias**

Instala la biblioteca `requests` para manejar las solicitudes HTTP:

```bash
pip install requests
```

### **c. Configura el Archivo de Variables de Entorno**

1. Crea un archivo `.env` en el directorio raíz:
    
    ```
    API_URL=https://jsonplaceholder.typicode.com
    ```
    
2. Asegúrate de ignorar `.env` en tu repositorio:
    
    ```bash
    echo ".env" >> .gitignore
    ```
    

---

### **3. Implementación del Código**

### **a. Estructura del Proyecto**

```
jsonplaceholder_api/
├── api_client.py     # Código para interactuar con la API
├── .env              # Variables de entorno
└── venv/             # Entorno virtual
```

---

### **b. Código para la Interacción con la API**

```python
import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
API_URL = os.getenv("API_URL")

if not API_URL:
    raise ValueError("API_URL no está configurado en el archivo .env")

# Función para crear un nuevo recurso
def crear_post(titulo, cuerpo, user_id):
    """
    Crea un nuevo post usando el método POST.
    Args:
        titulo (str): Título del post.
        cuerpo (str): Contenido del post.
        user_id (int): ID del usuario que crea el post.
    Returns:
        dict: Respuesta de la API.
    """
    url = f"{API_URL}/posts"
    data = {"title": titulo, "body": cuerpo, "userId": user_id}
    response = requests.post(url, json=data)

    if response.status_code == 201:
        return response.json()
    else:
        return {"error": f"Falló la creación: {response.status_code}"}

# Función para actualizar un recurso existente
def actualizar_post(post_id, titulo=None, cuerpo=None):
    """
    Actualiza un post existente usando el método PUT.
    Args:
        post_id (int): ID del post a actualizar.
        titulo (str): Nuevo título del post (opcional).
        cuerpo (str): Nuevo contenido del post (opcional).
    Returns:
        dict: Respuesta de la API.
    """
    url = f"{API_URL}/posts/{post_id}"
    data = {}
    if titulo:
        data["title"] = titulo
    if cuerpo:
        data["body"] = cuerpo

    response = requests.put(url, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Falló la actualización: {response.status_code}"}

# Función para eliminar un recurso
def eliminar_post(post_id):
    """
    Elimina un post existente usando el método DELETE.
    Args:
        post_id (int): ID del post a eliminar.
    Returns:
        dict: Respuesta de la API.
    """
    url = f"{API_URL}/posts/{post_id}"
    response = requests.delete(url)

    if response.status_code == 200:
        return {"message": f"Post con ID {post_id} eliminado con éxito."}
    else:
        return {"error": f"Falló la eliminación: {response.status_code}"}

# Probar las funciones
if __name__ == "__main__":
    print("1. Crear un nuevo post:")
    nuevo_post = crear_post("Mi Nuevo Post", "Este es el contenido del post.", 1)
    print(nuevo_post)

    print("\n2. Actualizar un post existente:")
    post_actualizado = actualizar_post(nuevo_post["id"], titulo="Título Actualizado")
    print(post_actualizado)

    print("\n3. Eliminar un post:")
    resultado_eliminacion = eliminar_post(nuevo_post["id"])
    print(resultado_eliminacion)
```

---

### **4. Explicación del Código**

1. **Cargar Variables de Entorno**:
    - `dotenv` asegura que las URLs sensibles estén ocultas.
    - `os.getenv("API_URL")` obtiene la URL base desde `.env`.
2. **Crear un Nuevo Post (POST)**:
    - Enviaremos datos al endpoint `/posts` con un payload JSON.
    - El código revisa el código de estado `201` para confirmar que el recurso fue creado.
3. **Actualizar un Post (PUT)**:
    - Actualiza un post específico mediante su `ID`.
    - Solo actualiza las claves (`title` o `body`) que se proporcionen.
4. **Eliminar un Post (DELETE)**:
    - Elimina el recurso especificado por el `ID` utilizando el método DELETE.
    - El código verifica el código de estado `200` para confirmar la eliminación.

---

### **5. Cómo Ejecutar el Proyecto**

1. **Ejecutar el Script**:
    
    ```bash
    python api_client.py
    ```
    
2. **Resultados Esperados**:
    - **Crear un Post**:
        
        ```json
        {
          "title": "Mi Nuevo Post",
          "body": "Este es el contenido del post.",
          "userId": 1,
          "id": 101
        }
        
        ```
        
    - **Actualizar un Post**:
        
        ```json
        {
          "id": 101,
          "title": "Título Actualizado",
          "body": "Este es el contenido del post.",
          "userId": 1
        }
        ```
        
    - **Eliminar un Post**:
        
        ```json
        {
          "message": "Post con ID 101 eliminado con éxito."
        }
        
        ```
        

En la actualización del post (`Falló la actualización: 500`) indica que hay un problema al procesar la solicitud en el servidor. En el caso de la API JSONPlaceholder, este error puede ocurrir debido a cómo maneja las solicitudes `PUT`.