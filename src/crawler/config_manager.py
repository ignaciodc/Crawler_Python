import configparser
from crawler.logger_util import configurar_logger

logger = configurar_logger()


def cargar_configuracion(ruta_archivo="config.ini"):
    logger.info(f"Leyendo archivo de configuración: {ruta_archivo}...")
    lector = configparser.ConfigParser()

    if not lector.read(ruta_archivo):
        raise FileNotFoundError(f"No se encontró el archivo '{ruta_archivo}'.")

    try:
        url = lector.get('AJUSTES', 'url_inicial')
        profundidad = lector.getint('AJUSTES', 'profundidad_maxima')
        limite = lector.getint('AJUSTES', 'limite_paginas')
        salida = lector.get('AJUSTES', 'archivo_salida').lower()

        texto_palabras = lector.get('AJUSTES', 'palabras_clave', fallback="")
        lista_palabras = [k.strip() for k in texto_palabras.split(',')] if texto_palabras else []

        if profundidad < 3:
            raise ValueError("La profundidad máxima configurada debe ser al menos 3.")
        if limite < 50:
            raise ValueError("El límite de páginas configurado debe ser al menos 50.")
        if lista_palabras and len(lista_palabras) < 3:
            raise ValueError("Si usas palabras clave, debes especificar al menos 3.")
        if salida not in ["csv", "json"]:
            raise ValueError("El archivo de salida debe ser 'csv' o 'json'.")

        logger.info("Configuración validada con éxito.")
        return url, profundidad, limite, lista_palabras, salida

    except configparser.NoSectionError:
        raise ValueError("El archivo config.ini está mal formateado: Falta la sección [AJUSTES].")
    except configparser.NoOptionError as e:
        raise ValueError(f"Falta un parámetro obligatorio en la configuración: {e.option}")