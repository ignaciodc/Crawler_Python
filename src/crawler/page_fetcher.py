import requests
from bs4 import BeautifulSoup

from crawler.logger_util import configurar_logger

logger = configurar_logger()


def descargar_pagina(url):
    """
    Descarga una página web usando la URL indicada.
    Devuelve el texto HTML.
    """
    try:
        # Usar requests.get(url) para descargar la página.
        respuesta = requests.get(url)

        # Verificamos que no haya errores web (como un 404).
        respuesta.raise_for_status()

        return respuesta.text

    except requests.RequestException as e:
        # Capturamos y registramos errores de conexión.
        logger.error(f"Error al intentar descargar la URL {url}. Detalle: {e}")
        return None


def parsear_html(html):
    """
    Prepara el HTML para extraer datos.
    Convierte el texto en un objeto BeautifulSoup.
    """
    if html is None:
        return None

    # Creamos el objeto para manipular documentos HTML.
    try:
        sopa = BeautifulSoup(html, 'html.parser')
        return sopa

    except Exception as e:
        logger.error(f"Error al parsear el documento HTML. Detalle: {e}")
        return None