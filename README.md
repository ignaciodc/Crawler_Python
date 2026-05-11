# Crawler_Python

Este proyecto consiste en el desarrollo de un crawler (araña web) modular diseñado para recorrer automáticamente un conjunto de páginas web, extrayendo información relevante de manera estructurada. El sistema permite configurar límites de profundidad, palabras clave y formatos de salida, garantizando un rastreo eficiente y controlado.

## Estructura del Proyecto

Siguiendo las recomendaciones del proyecto, se ha organizado el código de forma modular para facilitar su mantenimiento y escalabilidad:

```text
Crawler_Python/
│
├── docs/                        # Documentación y diagramas
│   ├── uml/                     # Archivos fuente PlantUML
│   └── img/                     # Imágenes de los diagramas
│
├── src/                         # Código fuente del proyecto
│   ├── crawler/                 # Paquete principal del crawler 
│   │   ├── __init__.py          # Marca el directorio como paquete 
│   │   ├── crawler.py           # Orquestador principal del rastreo 
│   │   ├── page_fetcher.py      # Gestión de descargas (requests) 
│   │   ├── link_extractor.py    # Análisis de HTML (BeautifulSoup) 
│   │   ├── result_exporter.py   # Exportación a CSV/JSON 
│   │   ├── config_manager.py    # Lector de configuración 
│   │   └── logger_util.py       # Utilidad de registro de eventos 
│   └── main.py                  # Punto de entrada de la aplicación 
│
├── config.ini                   # Archivo de configuración para el usuario 
├── requirements.txt             # Dependencias del proyecto 
└── README.md                    # Documentación principal
```

## Configuración (config.ini)

El sistema utiliza la librería configparser para gestionar los parámetros de ejecución sin necesidad de modificar el código fuente.

Parámetro | Descripción | Restricción
--- | --- | ---
url_inicial | Punto de partida del rastreo. | URL válida.
profundidad_maxima | Niveles de navegación desde el inicio. | Mínimo 3.
limite_paginas | Número máximo de URLs a visitar. | Mínimo 50.
palabras_clave | Filtro opcional por título/URL. | Mínimo 3 palabras.
archivo_salida | Formato del archivo generado. | CSV o JSON.

## Decisiones de Diseño

En cumplimiento con el requisito de documentación extensiva, se detallan las decisiones técnicas tomadas:

### 1. Gestión de Logs con Doble Salida
Se ha implementado un sistema de logging con dos controladores (handlers) diferenciados en logger_util.py:
- Consola: Muestra información de progreso (INFO) para que el usuario monitoree el estado en tiempo real.
- Archivo (errores.log): Registra exclusivamente errores de conexión o parseo (ERROR), garantizando que los fallos queden documentados de forma persistente sin ensuciar la salida informativa.

### 2. Validación de Configuración mediante Excepciones
Se ha optado por un diseño modular en config_manager.py donde se lanzan excepciones (raise ValueError) si los parámetros no cumplen los mínimos exigidos.

- Justificación: Esto permite que el módulo de configuración sea independiente. Es el flujo principal (main.py) quien captura estas excepciones y decide realizar un cierre limpio, evitando que el crawler inicie con parámetros inválidos.

### 3. Arquitectura Modular y Desacoplada
Cada funcionalidad reside en un archivo específico (descarga, extracción, exportación). Esto cumple con el principio de responsabilidad única, facilitando las pruebas unitarias de cada componente antes de integrarlos en el motor principal.

## Diagramas UML
Los diagramas de arquitectura se encuentran en la carpeta docs/ y describen el flujo lógico del sistema:

- Casos de Uso: Define las interacciones del usuario con el sistema (configurar, ejecutar, monitorear).
- Diagrama de Secuencia: Detalla la comunicación cronológica entre los módulos main, config_manager, fetcher y extractor.

## Instalación y Ejecución

1. Clonar el repositorio:
```bash
git clone https://github.com/ignaciodc/Crawler_Python
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar el archivo config.ini con los valores deseados.

4. Ejecutar el programa:
```bash
python src/main.py
```
