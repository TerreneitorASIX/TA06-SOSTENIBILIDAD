import os

def verificar_format_arxius(directori):
    formats = {}
    
    # Verificar si el directorio existe
    if not os.path.exists(directori):
        print(f"El directorio {directori} no existe.")
        return formats
    
    # Iterar sobre los archivos en el directorio
    for arxiu in os.listdir(directori):
        ruta_completa = os.path.join(directori, arxiu)
        if os.path.isfile(ruta_completa):
            ext = arxiu.split('.')[-1]  # Extraer la extensión del archivo
            if ext not in formats:
                formats[ext] = 0
            formats[ext] += 1
    
    return formats

# Definir el directorio en el que buscar los archivos
directori = "/home/stalyn.suarez.7e8/Baixades/precip.MIROC5.RCP60.2006-2100.SDSM_REJ"  # Sustituye con tu directorio real

# Llamar a la función
formats = verificar_format_arxius(directori)

# Imprimir los formatos y sus conteos
print(formats)
