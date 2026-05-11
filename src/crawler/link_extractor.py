from urllib.parse import urljoin, urlparse


def extraer_enlaces(soup, url_base):
    enlaces_validos = []
    enlaces_vistos = set()

    if soup is None:
        return enlaces_validos

    etiquetas = soup.select('a[href]')
    dominio_base = urlparse(url_base).netloc

    for etiqueta in etiquetas:
        enlace_crudo = etiqueta['href']
        enlace_absoluto = urljoin(url_base, enlace_crudo)
        enlace_limpio = enlace_absoluto.split('#')[0]

        if not enlace_limpio.startswith('http'):
            continue

        dominio_actual = urlparse(enlace_limpio).netloc

        if dominio_actual == dominio_base and enlace_limpio not in enlaces_vistos:
            enlaces_vistos.add(enlace_limpio)
            enlaces_validos.append(enlace_limpio)

    return enlaces_validos