import os
import glob

def calcular_media_y_porcentaje_negativos(ruta_carpeta):
    total_valores = 0
    total_negativos = 0
    archivos_procesados = 0

    # Buscar todos los archivos en la carpeta especificada
    archivos = glob.glob(os.path.join(ruta_carpeta, "*.dat"))

    for archivo in archivos:
        archivos_procesados += 1
        print(f"Procesando archivo: {archivo}")
        with open(archivo, "r") as f:
            for linea in f:
                # Separar la línea en valores
                try:
                    valores = [float(valor) for valor in linea.split()]
                except ValueError:
                    # Saltar líneas con valores no numéricos
                    continue
                
                # Contar valores procesados y los -999
                total_valores += len(valores)
                total_negativos += valores.count(-999)

    # Calcular estadísticas
    porcentaje_negativos = (total_negativos / total_valores * 100) if total_valores > 0 else 0
    print("\n--- Resultados ---")
    print(f"Archivos procesados: {archivos_procesados}")
    print(f"Total de valores procesados: {total_valores}")
    print(f"Total de -999 encontrados: {total_negativos}")
    print(f"Porcentaje de -999: {porcentaje_negativos:.2f}%")
    return total_valores, total_negativos, porcentaje_negativos

# Ruta a la carpeta que contiene los archivos
ruta_carpeta = "../dades/dades_netas"

# Ejecutar la función
calcular_media_y_porcentaje_negativos(ruta_carpeta)
