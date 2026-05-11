# Crawler_Python

Este proyecto consiste en el desarrollo de un crawler modular diseñado para recorrer automáticamente un conjunto de páginas web, extrayendo información relevante de manera estructurada. El sistema permite configurar límites de profundidad, palabras clave y formatos de salida, garantizando un rastreo eficiente y controlado.

## Estructura del Proyecto

El código se organiza siguiendo los principios de responsabilidad única y modularidad recomendados en la práctica:

```text
Crawler_Python/
│
├── docs/                        # Documentación técnica
│   ├── uml/                     # Archivos fuente PlantUML
│   └── img/                     # Imágenes de los diagramas (Casos de Uso y Secuencia)
│
├── src/                         # Código fuente
│   ├── crawler/                 # Paquete principal
│   │   ├── __init__.py          
│   │   ├── crawler.py           # [EN DESARROLLO] Se encarga de unir todo
│   │   ├── page_fetcher.py      # Descarga y parseo (requests + BeautifulSoup)
│   │   ├── link_extractor.py    # Normalización y filtrado de enlaces
│   │   ├── result_exporter.py   # Exportación flexible a CSV/JSON
│   │   ├── config_manager.py    # Lector de configuración con validación estricta
│   │   └── logger_util.py       # Sistema de logs con doble salida
│   └── main.py                  # Organizador del programa
│
├── config.ini                   # Parámetros del usuario
├── requirements.txt             # Dependencias (requests, beautifulsoup4)
└── README.md                    # Documentación del proyecto
```

## Decisiones de Diseño 

Se detallan las decisiones técnicas tomadas para garantizar la robustez del sistema:

### 1. Gestión de Logs con Doble Salida
Se utiliza la librería nativa logging con dos controladores diferenciados:

- Consola (Nivel INFO): Permite al usuario monitorear el progreso del rastreo en tiempo real.
- Archivo errores.log (Nivel ERROR): Registra de forma persistente los fallos de red o parseo, incluyendo marca de tiempo y detalle del error, tal como exige el enunciado.

### 2. Validación de Configuración mediante Excepciones (raise)
En lugar de forzar el cierre del programa desde el módulo de configuración, config_manager.py lanza excepciones de tipo ValueError o FileNotFoundError.

- Justificación: Esto desacopla el lector del flujo principal. El archivo main.py captura estas excepciones y realiza un cierre limpio, informando al usuario sin mostrar errores de sistema (tracebacks).

### 3. Normalización y Filtrado de Enlaces
Para el extractor de enlaces (link_extractor.py), se han tomado decisiones críticas para evitar bucles infinitos:

- Normalización: Se usa urllib.parse.urljoin para convertir automáticamente enlaces relativos (/contacto) en URLs absolutas válidas.
- Mismo Dominio: El crawler se restringe al dominio de la URL inicial para evitar "fugas" a sitios externos (como redes sociales).
- Eficiencia: Se utiliza un conjunto (set) para el rastreo de duplicados, garantizando un rendimiento óptimo independientemente del número de enlaces encontrados.

### 4. Exportación Multiformato
El módulo result_exporter.py unifica la generación de resultados en una sola función capaz de manejar tanto CSV como JSON, asegurando que se respeten las columnas obligatorias (URL, Título, Enlaces, Tiempo) y el uso de codificación UTF-8 para caracteres especiales.

## Motor del Crawler (crawler.py)

...

## Diagramas UML

Se han desarrollado dos diagramas fundamentales para entender el sistema:

- Diagrama de Casos de Uso: Muestra las funciones que el usuario puede realizar y las dependencias internas (<<include>> y <<extend>>).
- Diagrama de Secuencia: Describe cómo fluyen los datos entre los archivos .py desde que se arranca el programa hasta que se genera el archivo de resultados.

## Instalación y Uso

- Clonar: `git clone https://github.com/ignaciodc/Crawler_Python`
- Instalar: `pip install -r requirements.txt`
- Configurar el archivo config.ini.
- Ejecutar: `python src/main.py`