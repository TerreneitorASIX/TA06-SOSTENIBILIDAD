import os
import pandas as pd

# Crear una función para procesar y reorganizar los datos
def process_data(file_path, output_folder):
    try:
        # Leer el archivo de datos ignorando encabezados inconsistentes
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Leer los datos y omitir las primeras dos líneas
        data = []
        for line in lines[2:]:  # Comenzar desde la tercera línea
            # Dividir cada línea en columnas según espacios y omitir la primera columna
            parts = line.strip().split()[1:]
            data.append(parts)

        # Crear un DataFrame sin ajustar las filas
        df = pd.DataFrame(data)

        # Asegurarse de que las columnas numéricas sean consistentes
        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            except Exception as e:
                print(f"Error procesando columna {col}: {e}")

        # Contar valores -999
        count_minus_999 = (df == -999).sum().sum()

        # Calcular el porcentaje de -999
        total_values = df.size  # Número total de elementos en el DataFrame
        percent_minus_999 = (count_minus_999 / total_values) * 100 if total_values > 0 else 0

        # Guardar el archivo reorganizado con el conteo y el porcentaje de -999
        base_name = os.path.basename(file_path)
        output_path = os.path.join(output_folder, base_name)

        # Escribir datos en un archivo nuevo, incluyendo las estadísticas
        with open(output_path, 'w') as output_file:
            # Escribir datos del DataFrame
            for row in df.itertuples(index=False, name=None):
                output_file.write('\t'.join(map(str, row)) + '\n')
            # Agregar la línea con el conteo y el porcentaje de -999
            output_file.write(f"# Cantidad de -999: {count_minus_999}\n")
            output_file.write(f"# Porcentaje de -999: {percent_minus_999:.2f}%\n")

        print(f"Archivo procesado y guardado en: {output_path}")

    except Exception as e:
        print(f"Error procesando el archivo {file_path}: {e}")

# Función principal para procesar todos los archivos de una carpeta
def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.dat'):
            file_path = os.path.join(input_folder, file_name)
            process_data(file_path, output_folder)

# Ruta de las carpetas de entrada y salida
input_folder = '../dades/dades_sin_ordenar'  # Ruta original de entrada
output_folder = '../dades/dades_netas'  # Usar una ruta local

# Procesar los archivos
process_folder(input_folder, output_folder)
