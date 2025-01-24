import os
import csv

def verificar_format_arxius(directori):
    formatos = {}  # Almacenar el formato de cada archivo
    
    # Verificar si el directorio existe
    if not os.path.exists(directori):
        print(f"El directorio {directori} no existe.")
        return formatos
    
    # Iterar sobre los archivos en el directorio
    for arxiu in os.listdir(directori):
        ruta_completa = os.path.join(directori, arxiu)
        if os.path.isfile(ruta_completa):
            try:
                # Intentar abrir el archivo con diferentes codificaciones
                for encoding in ['utf-8', 'iso-8859-1', 'windows-1252']:
                    try:
                        with open(ruta_completa, 'r', encoding=encoding) as f:
                            # Leer las primeras filas para analizar el formato
                            primera_fila = f.readline()
                            delimitador = detectar_delimitador(primera_fila)
                            columnas = len(primera_fila.split(delimitador))
                            
                            # Guardar el formato detectado
                            formatos[arxiu] = {'delimitador': delimitador, 'columnas': columnas}
                            break  # Salir del bucle si se abre correctamente
                    except UnicodeDecodeError:
                        continue  # Intentar con la siguiente codificación
                else:
                    # Si ninguna codificación funcionó, lanzar una excepción
                    raise UnicodeDecodeError(f"No se pudo leer el archivo {arxiu} con ninguna codificación soportada.")
            except Exception as e:
                print(f"Error leyendo el archivo {arxiu}: {e}")
    
    return formatos

def detectar_delimitador(fila):
    # Detectar delimitador común (puedes ajustar según los requisitos)
    delimitadores = [',', ';', '\t', '|']
    for delimitador in delimitadores:
        if delimitador in fila:
            return delimitador
    return ','  # Por defecto, suponer coma si no se detecta ninguno

def validar_formato_unico(formatos):
    if not formatos:
        print("No hay archivos o no se pudo leer su formato.")
        return False
    
    # Obtener el primer formato como referencia
    formatos_valores = list(formatos.values())
    referencia = formatos_valores[0]
    
    # Comparar todos los formatos con la referencia
    for formato in formatos_valores[1:]:
        if formato != referencia:
            return False
    return True

# Definir el directorio en el que buscar los archivos
directori = "../dades/dades_sin_ordenar"  # Sustituye con tu directorio real

# Llamar a la función para verificar formatos
formatos_detectados = verificar_format_arxius(directori)
print("Formatos detectados por archivo:")
for archivo, formato in formatos_detectados.items():
    print(f"{archivo}: {formato}")

# Validar si todos los formatos son iguales
if validar_formato_unico(formatos_detectados):
    print("Todos los archivos tienen el mismo formato.")
else:
    print("Los archivos no tienen el mismo formato.")
