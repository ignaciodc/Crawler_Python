def link_extractor (soup):
    enlaces_validos = []
    if soup is None:
        return enlaces_validos
    etiquetas = soup.select('a[href]')

    for etiqueta in etiquetas:
        enlace = etiqueta['href']

        if enlace not in enlaces_validos:
            enlaces_validos.append(enlace)
    return enlaces_validos