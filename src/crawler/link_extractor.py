def extraer_enlaces (soup):
    # Creamos una lista vacia para los resultados
    enlaces_validos = []
    if soup is None:
        return enlaces_validos
        # Extraemos los enlaces del codigo HTML
    etiquetas = soup.select('a[href]')

    for etiqueta in etiquetas:
        enlace = etiqueta['href']
        
        # Guardamos el enlace ignorando los duplicados
        if enlace not in enlaces_validos:
            enlaces_validos.append(enlace)
    return enlaces_validos
