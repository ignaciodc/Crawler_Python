import requests
from bs4 import BeautifulSoup
import logging

# Configuramos el registro de problemas.
# Se deben capturar y registrar errores de conexión o parseo[cite: 22].
logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

def descargar_pagina(url):
    """
    Descarga una página web.
    Usa la URL indicada.
    Devuelve el texto HTML.
    """
    try:
        # Usar requests.get(url) para descargar la página[cite: 17].
        respuesta = requests.get(url)
        
        # Verificamos que no haya errores web (como un 404).
        respuesta.raise_for_status()
        
        # Devolvemos el código HTML en texto.
        return respuesta.text
        
    except requests.RequestException as e:
        # Anotamos el fallo si no hay internet o la web cae[cite: 22].
        logging.error(f"Error al intentar descargar la URL {url}. Detalle: {e}")
        return None

def parsear_html(html):
    """
    Prepara el HTML para extraer datos.
    Convierte el texto en un objeto BeautifulSoup.
    """
    # Si la descarga falló, cancelamos el proceso.
    if html is None:
        return None
        
    # Creamos el objeto para manipular documentos HTML[cite: 6].
    # Usamos el motor 'html.parser' recomendado en los apuntes[cite: 18].
    sopa = BeautifulSoup(html, 'html.parser')
    
    # Devolvemos la estructura lista para buscar enlaces.
    return sopa
