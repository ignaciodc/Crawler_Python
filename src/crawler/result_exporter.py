import csv
import json
from crawler.logger_util import configurar_logger

logger = configurar_logger()

def exportar_resultados(datos_paginas, formato="csv", nombre_archivo="resultados"):
    if not datos_paginas:
        logger.warning("No hay datos recopilados para exportar.")
        return

    try:
        if formato == "csv":
            archivo_salida = f"{nombre_archivo}.csv"
            with open(archivo_salida, mode='w', newline='', encoding='utf-8') as archivo:
                escritor_csv = csv.writer(archivo)
                escritor_csv.writerow(['URL', 'Titulo', 'Num de enlaces', 'Tiempo (ms)'])
                for pagina in datos_paginas:
                    escritor_csv.writerow([pagina['url'], pagina['titulo'], pagina['num_enlaces'], pagina['ms']])
            logger.info(f"Datos exportados exitosamente a {archivo_salida}")

        elif formato == "json":
            archivo_salida = f"{nombre_archivo}.json"
            with open(archivo_salida, mode='w', encoding='utf-8') as archivo:
                json.dump(datos_paginas, archivo, indent=4, ensure_ascii=False)
            logger.info(f"Datos exportados exitosamente a {archivo_salida}")

    except OSError as e:
        raise OSError(f"Fallo del sistema al intentar guardar los resultados: {e}")