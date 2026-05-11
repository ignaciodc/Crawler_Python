import requests
from bs4 import BeautifulSoup
from crawler.logger_util import configurar_logger

logger = configurar_logger()

def descargar_pagina(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.text
    except requests.RequestException as e:
        logger.error(f"Error al descargar la URL {url}. Detalle: {e}")
        return None

def parsear_html(html):
    if html is None:
        return None
    try:
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except Exception as e:
        logger.error(f"Error al parsear el HTML. Detalle: {e}")
        return None