import csv

def exportar_csv(archivo_salida, datos_paginas):
    """recibe una lista con datos de las páginas visitadas y los escribe en un archivo csv"""
    
    # abrimos el archivo csv en modo escritura (o lo creamos)
    with open(archivo_salida, mode='w', newline='', encoding='utf8') as archivo:
        escritor_csv = csv.writer(archivo)
        
        # Primera fila, cabeceras
        escritor_csv.writerow(['URL', 'Titulo', 'Num de enlaces', 'ms (tiempo)'])
        
        # Recorre los datos y escribe una fila por pagina 
        for pagina in datos_paginas:
            escritor_csv.writerow([pagina['url'], pagina['titulo'], pagina['num_enlaces'], pagina['ms']])

    print(f"Datos guardados en {archivo_salida}")
