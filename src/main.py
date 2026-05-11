import sys
from crawler.logger_util import configurar_logger
from crawler.config_manager import cargar_configuracion
from crawler.crawler import WebCrawler
from crawler.result_exporter import exportar_resultados


def main():
    logger = configurar_logger()

    try:
        # 1. Leer y validar la configuración
        url, profundidad, limite, palabras, salida = cargar_configuracion("../config.ini")

        # 2. Inicializar el Crawler
        mi_crawler = WebCrawler(
            url_inicial=url,
            profundidad_maxima=profundidad,
            limite_paginas=limite,
            palabras_clave=palabras
        )

        # 3. Iniciar el crawler
        datos_recopilados = mi_crawler.iniciar()

        # 4. Guardar los resultados
        exportar_resultados(datos_recopilados, formato=salida)

    except (ValueError, FileNotFoundError, PermissionError, OSError) as error:
        # Si algo catastrófico ocurre en la configuración o el disco duro
        logger.error(f"\n[ERROR CRÍTICO] El programa se detuvo: {error}")
        sys.exit(1)
    except KeyboardInterrupt:
        # Por si el usuario pulsa Ctrl+C para parar el programa a la fuerza
        logger.warning("\n[AVISO] El usuario ha cancelado el rastreo manualmente.")
        sys.exit(0)


if __name__ == "__main__":
    main()