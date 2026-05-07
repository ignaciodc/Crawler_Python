import logging
import sys


def configurar_logger():
    # Creamos el objeto logger principal
    logger = logging.getLogger("CrawlerLogger")

    # Le decimos que procese desde INFO hacia arriba (INFO, WARNING, ERROR, CRITICAL)
    logger.setLevel(logging.INFO)

    # Evitamos que se dupliquen los mensajes si la función se llama varias veces
    if not logger.handlers:
        # SALIDA 1: La terminal (Para el progreso)
        salida_terminal = logging.StreamHandler(sys.stdout)
        salida_terminal.setLevel(logging.INFO)
        formato_terminal = logging.Formatter('%(message)s')  # Formato limpio
        salida_terminal.setFormatter(formato_terminal)

        # SALIDA 2: Archivo .log (Para capturar y registrar errores)
        salida_archivo = logging.FileHandler("errores.log", mode='a', encoding='utf-8')
        salida_archivo.setLevel(logging.ERROR)
        formato_archivo = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  # Formato técnico: incluye la fecha y hora exacta del fallo
        salida_archivo.setFormatter(formato_archivo)

        # Añadimos las dos salidas a nuestro logger
        logger.addHandler(salida_terminal)
        logger.addHandler(salida_archivo)

    return logger