import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

# Descarga la página web. Captura los errores. Devuelve el HTML.
def descargar_pagina(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.text
    except requests.RequestException as e:
        logging.error(f"Error al intentar descargar la URL {url}. Detalle: {e}")
        return None

# Prepara el documento HTML. Lo convierte en objeto. Devuelve sopa.
def parsear_html(html):
    if html is None:
        return None
    soup = BeautifulSoup(html, 'html.parser')
    return soup
