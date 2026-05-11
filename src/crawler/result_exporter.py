import csv
import json
from crawler.logger_util import configurar_logger

logger = configurar_logger()


def exportar_resultados(datos_paginas, formato="csv", nombre_archivo="resultados"):
    """
    Recibe una lista con datos de las páginas visitadas y los escribe en CSV o JSON.
    """
    # Pequeña validación por si el crawler no encontró nada
    if not datos_paginas:
        logger.warning("No hay datos recopilados para exportar.")
        return

    try:
        # Exportar a CSV
        if formato == "csv":
            archivo_salida = f"{nombre_archivo}.csv"
            # Abre el archivo protegiendo los caracteres especiales con utf-8
            with open(archivo_salida, mode='w', newline='', encoding='utf-8') as archivo:
                escritor_csv = csv.writer(archivo)

                # Primera fila: Las cabeceras exactas requeridas
                escritor_csv.writerow(['URL', 'Titulo', 'Num de enlaces', 'Tiempo (ms)'])

                # Recorre los datos y escribe una fila por página
                for pagina in datos_paginas:
                    escritor_csv.writerow([pagina['url'], pagina['titulo'], pagina['num_enlaces'], pagina['ms']])

            logger.info(f"Datos exportados exitosamente a {archivo_salida}")

        # Exportar a JSON
        elif formato == "json":
            archivo_salida = f"{nombre_archivo}.json"
            with open(archivo_salida, mode='w', encoding='utf-8') as archivo:
                # json.dump escribe la lista de diccionarios directamente.
                # indent=4 lo pone bonito y legible, ensure_ascii=False respeta las tildes.
                json.dump(datos_paginas, archivo, indent=4, ensure_ascii=False)

            logger.info(f"Datos exportados exitosamente a {archivo_salida}")

    except OSError as e:
        raise OSError(f"Fallo del sistema al intentar guardar los resultados: {e}")