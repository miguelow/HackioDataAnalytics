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
