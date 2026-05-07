import csv

class exportarResultados:
    def __init__(self, archivo_salida):
        self.archivo_salida = archivo_salida

    def exportar_csv(self, datos_paginas):
        with open(self.archivo_salida, mode='w', newline='', encoding='utf8') as archivo:
            escritor_csv = csv.writer(archivo)

            escritor_csv.writerow(['URL', 'Titulo', 'Num de enlaces', 'ms (tiempo)'])

            for pagina in datos_paginas:
                escritor_csv.writerow([pagina['url'], pagina['titulo'], pagina['num_enlaces'], pagina['ms']])

        print(f"Datos guardados en {self.archivo_salida}")