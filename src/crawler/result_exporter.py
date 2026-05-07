import csv

class ExportarResultados:
    def __init__(self, archivo_salida):
        self.archivo_salida = archivo_salida
        
"""recibe una lista con  datos de las páginas visitadas y los escribe en u archivo csv"""
    
    def exportar_csv(self, datos_paginas):
        
        # abrimos el archivo csv en modo escritura (o lo creamos)
        
        with open(self.archivo_salida, mode='w', newline='', encoding='utf8') as archivo:
            escritor_csv = csv.writer(archivo)
            
            # Primera fila, cabeceras
            escritor_csv.writerow(['URL', 'Titulo', 'Num de enlaces', 'ms (tiempo)'])
            
            # Recorre los datos y escribe una fila por pagina 
            for pagina in datos_paginas:
                escritor_csv.writerow([pagina['url'], pagina['titulo'], pagina['num_enlaces'], pagina['ms']])

        print(f"Datos guardados en {self.archivo_salida}")
