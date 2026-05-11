<<<<<<< HEAD
def link_extractor (soup):
=======
from urllib.parse import urljoin, urlparse


def extraer_enlaces(soup, url_base):
    """
    Extrae todos los enlaces válidos de un objeto BeautifulSoup.
    Convierte enlaces relativos en absolutos y restringe al mismo dominio.
    """
>>>>>>> d8a937e84756bbb21c5729285c52b94e0ede6ca5
    enlaces_validos = []

    # Usamos un 'set' (conjunto) para llevar el registro de duplicados. 
    enlaces_vistos = set()

    if soup is None:
        return enlaces_validos

    # Extraemos los enlaces del codigo HTML 
    etiquetas = soup.select('a[href]')

    # Extraemos el dominio original (ej: "es.wikipedia.org") para no salirnos de él 
    dominio_base = urlparse(url_base).netloc

    for etiqueta in etiquetas:
        enlace_crudo = etiqueta['href']

        # 1. Convertir relativos a absolutos (ej: "/contacto" -> "https://web.com/contacto")
        enlace_absoluto = urljoin(url_base, enlace_crudo)

        # 2. Limpiar "anclas" internas (ej: pagina.com/index#seccion -> pagina.com/index)
        enlace_limpio = enlace_absoluto.split('#')[0]

        # Ignorar enlaces de correo o javascript (mailto:, javascript:)
        if not enlace_limpio.startswith('http'):
            continue

        # 3. Comprobar que el enlace pertenece al mismo dominio principal 
        dominio_actual = urlparse(enlace_limpio).netloc

        # Guardamos ignorando duplicados (gracias al set) y externos
        if dominio_actual == dominio_base and enlace_limpio not in enlaces_vistos:
            enlaces_vistos.add(enlace_limpio)  # Lo marcamos como visto rápido
            enlaces_validos.append(enlace_limpio)  # Lo guardamos en el orden correcto

    return enlaces_validos