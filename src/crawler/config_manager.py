import configparser

def leer_configuracion(ruta_archivo):
    config = configparser.ConfigParser()
    config.read(ruta_archivo)

    url = config.get('Ajustes', 'url_inicial', fallback='')
    salida = config.get('Ajustes', 'salida', fallback='resultados.csv')

    profundidad = config.getint('Ajustes', 'profundidad_maxima', fallback=3)
    if profundidad < 3:
        profundidad = 3

    paginas = config.getint('Ajustes', 'paginas_maxima', fallback=50)
    if paginas < 50:
        paginas = 50

    return {
        'url_inicial': url,
        'profundidad_maxima': profundidad,
        'max_paginas': paginas,
        'archivo_salida': salida
    }