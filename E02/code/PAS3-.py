import pandas as pd
import glob
import os

def cargar_dades(fitxer):
    try:
        # Leer todas las filas ignorando las dos primeras líneas
        df = pd.read_csv(fitxer, sep='\s+', skiprows=2, engine='python')
        print(f"Contenido cargado del archivo {fitxer}:")
        print(df.head(10))  # Mostrar las primeras 10 filas para ver el contenido
    except Exception as e:
        print(f"Error al leer el archivo {fitxer}: {e}")
        return None
    return df

def netejar_dades(df):
    try:
        # Verificar la consistencia de las columnas
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # Reemplazar valores negativos por NaN
        df[df < 0] = float('nan')

        # Gestionar valores nulos: reemplazar NaN en columnas numéricas por la media
        df.fillna(df.mean(numeric_only=True), inplace=True)

        # Eliminar filas duplicadas
        df.drop_duplicates(inplace=True)

        print("Datos limpiados:")
        print(df.head(10))  # Mostrar las primeras 10 filas de los datos limpios

        return df
    except Exception as e:
        print(f"Error al limpiar los datos: {e}")
        return None

def guardar_dades(df, fitxer_destino):
    """
    Guarda el DataFrame limpio en un archivo nuevo.
    """
    try:
        print(f"Guardando el DataFrame limpio en {fitxer_destino} con las siguientes primeras filas:")
        print(df.head(10))  # Mostrar las primeras 10 filas antes de guardar
        df.to_csv(fitxer_destino, sep='\t', index=False)
        print(f"Dades netejades guardades a {fitxer_destino}")
    except Exception as e:
        print(f"Error al guardar el archivo {fitxer_destino}: {e}")

def netejar_dades_directori(carpeta_origen, carpeta_destino):
    # Asegurarse de que la carpeta de destino exista
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
        print(f"Carpeta {carpeta_destino} creada.")

    # Listar todos los archivos .dat en la carpeta de origen
    fitxers = glob.glob(os.path.join(carpeta_origen, '*.dat'))
    print(f"Archivos encontrados en {carpeta_origen}: {fitxers}")

    if not fitxers:
        print(f"No se encontraron archivos .dat en {carpeta_origen}. Verifica la ruta y los archivos.")
        return

    # Procesar cada archivo .dat
    for fitxer in fitxers:
        print(f"Processant el fitxer: {fitxer}")

        # Cargar el archivo
        df = cargar_dades(fitxer)
        if df is not None:
            # Limpiar los datos
            df = netejar_dades(df)

            if df is not None:
                # Guardar el archivo limpio en la carpeta de destino
                fitxer_destino = os.path.join(carpeta_destino, os.path.basename(fitxer))
                guardar_dades(df, fitxer_destino)

# Ejemplo de uso
script_dir = os.path.dirname(os.path.abspath(__file__))
carpeta_origen = os.path.join(script_dir, '../dades/dades_sin_ordenar')
carpeta_destino = os.path.join(script_dir, '../dades/dades_netas')

print(f"Ruta de la carpeta de origen: {carpeta_origen}")
print(f"Ruta de la carpeta de destino: {carpeta_destino}")

netejar_dades_directori(carpeta_origen, carpeta_destino)
