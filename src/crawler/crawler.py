import time
from collections import deque
from crawler.logger_util import configurar_logger
from crawler.page_fetcher import descargar_pagina, parsear_html
from crawler.link_extractor import extraer_enlaces

logger = configurar_logger()


class WebCrawler:
    def __init__(self, url_inicial, profundidad_maxima, limite_paginas, palabras_clave):
        self.url_inicial = url_inicial
        self.profundidad_maxima = profundidad_maxima
        self.limite_paginas = limite_paginas
        # Guardamos las palabras clave en minúsculas para facilitar la búsqueda
        self.palabras_clave = [pc.lower() for pc in palabras_clave]

        # 'set' para páginas ya vistas (evita bucles) y lista para los resultados finales
        self.paginas_visitadas = set()
        self.resultados = []

    def cumple_filtros(self, url, titulo):
        """Comprueba si la página contiene alguna palabra clave en el título o la URL."""
        if not self.palabras_clave:
            return True  # Si el usuario no puso palabras clave, todo pasa el filtro

        texto_busqueda = f"{url} {titulo}".lower()
        return any(palabra in texto_busqueda for palabra in self.palabras_clave)

    def iniciar(self):
        cola = deque([(self.url_inicial, 0)])

        logger.info(f"\n️ INICIANDO RASTREO: {self.url_inicial}")
        logger.info(f"   Profundidad: {self.profundidad_maxima} | Límite: {self.limite_paginas}\n")

        # El bucle se detiene si nos quedamos sin enlaces o si llegamos al límite de páginas
        while cola and len(self.resultados) < self.limite_paginas:
            # Sacamos el primer elemento de la cola
            url_actual, profundidad = cola.popleft()

            # Reglas de parada de seguridad
            if url_actual in self.paginas_visitadas:
                continue
            if profundidad > self.profundidad_maxima:
                continue

            # 1. Medir tiempo y descargar
            inicio_tiempo = time.time()
            html = descargar_pagina(url_actual)

            if not html:
                self.paginas_visitadas.add(url_actual)  # La marcamos como visitada aunque falle
                continue

            # 2. Parsear el HTML
            sopa = parsear_html(html)
            if not sopa:
                self.paginas_visitadas.add(url_actual)
                continue

            # Calculamos el tiempo que ha tardado en milisegundos
            tiempo_ms = int((time.time() - inicio_tiempo) * 1000)

            # 3. Extraer el Título
            etiqueta_titulo = sopa.find('title')
            # Usamos split() y join() para aniquilar los \n y espacios extra en medio del texto
            titulo = " ".join(
                etiqueta_titulo.text.split()) if etiqueta_titulo and etiqueta_titulo.text else "Sin título"
            
            # 4. Filtrar por palabras clave
            if not self.cumple_filtros(url_actual, titulo):
                self.paginas_visitadas.add(url_actual)
                continue  # Si no cumple, la ignoramos y pasamos a la siguiente de la cola

            # 5. Extraer enlaces limpios
            enlaces = extraer_enlaces(sopa, url_actual)

            # 6. Guardar los datos
            self.resultados.append({
                'url': url_actual,
                'titulo': titulo,
                'num_enlaces': len(enlaces),
                'ms': tiempo_ms
            })

            self.paginas_visitadas.add(url_actual)

            logger.info(
                f"✅ [{len(self.resultados)}/{self.limite_paginas}] Nivel {profundidad} | {tiempo_ms}ms | {url_actual}")

            if profundidad < self.profundidad_maxima:
                for enlace in enlaces:
                    if enlace not in self.paginas_visitadas:
                        # Los metemos al final de la cola, sumando 1 al nivel de profundidad
                        cola.append((enlace, profundidad + 1))

        logger.info(f"\n  RASTREO FINALIZADO. Páginas extraídas con éxito: {len(self.resultados)}")
        return self.resultados