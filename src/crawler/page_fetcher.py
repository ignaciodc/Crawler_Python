import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

def descargar_pagina(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.text
    except requests.RequestException as e:
        logging.error(f"Error al intentar descargar la URL {url}. Detalle: {e}")
        return None

def parsear_html(html):
    if html is None:
        return None
    sopa = BeautifulSoup(html, 'html.parser')
    return sopa