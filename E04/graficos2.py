import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# Buscar archivos que coincidan con el patrón
ruta_archivos = "csv/resultats_P*.csv"
archivos = glob.glob(ruta_archivos)  # Encuentra todos los archivos que coincidan con el patrón

if not archivos:
    raise FileNotFoundError(f"No se encontraron archivos que coincidan con el patrón: {ruta_archivos}")

# Procesar cada archivo encontrado
for archivo in archivos:
    # Extraer el prefijo del nombre del archivo (por ejemplo, 'resultats_P1')
    prefijo = os.path.splitext(os.path.basename(archivo))[0]
    print(f"Procesando archivo: {archivo}")
    
    # Leer el archivo CSV
    df = pd.read_csv(archivo, header=None, names=["Tipo", "Col2", "Col3", "Col4"])

    # Filtrar datos para "Mitjana/Precipitació total"
    df_mitjana = df[df["Tipo"] == "Mitjana/Precipitació total"]
    if not df_mitjana.empty:
        años_mitjana = df_mitjana["Col2"].astype(int)  # Convertir a años (int)
        mitjana = df_mitjana["Col3"].astype(float)
        precipitacion_total = df_mitjana["Col4"].astype(float)

    # Filtrar datos para "Taxa de variació interanual"
    df_variacio = df[df["Tipo"] == "Taxa de variació interanual"]
    if not df_variacio.empty:
        años_variacio = df_variacio["Col2"].str.split("-").str[1].astype(int)  # Tomar el segundo año del intervalo
        variacio = df_variacio["Col3"].str.replace("%", "").astype(float)  # Eliminar el símbolo '%' y convertir a float

    # Datos simulados (reemplazar con datos del CSV si es necesario)
    anys_mes_plujosos = [2009, 2016, 2007, 2046, 2042]
    valors_mes_plujosos = [4.72, 4.71, 4.49, 4.44, 4.33]

    anys_menys_plujosos = [2087, 2093, 2081, 2098, 2084]
    valors_menys_plujosos = [1.96, 1.90, 1.79, 1.55, 1.41]

    anys_mes_variacio = [2099, 2039, 2085, 2083, 2025]
    valors_mes_variacio = [96.59, 84.32, 76.09, 73.28, 58.32]

    anys_menys_variacio = [2021, 2062, 2098, 2038, 2084]
    valors_menys_variacio = [-39.09, -39.55, -48.00, -48.18, -64.42]

    # Gráfico 4: Comparación entre "5 anys més plujosos" y "5 anys menys plujosos"
    plt.figure(figsize=(10, 6))
    plt.bar([str(any) for any in anys_mes_plujosos], valors_mes_plujosos, color='blue', label="5 anys més plujosos")
    plt.bar([str(any) for any in anys_menys_plujosos], valors_menys_plujosos, color='red', label="5 anys menys plujosos")
    plt.title("Comparació: Anys més i menys plujosos")
    plt.xlabel("Anys")
    plt.ylabel("Precipitació (mm)")
    plt.grid(axis='y')
    plt.legend()
    nombre_grafico_plujosos = f"img/{prefijo}_grafic_comparacio_plujosos.png"
    plt.savefig(nombre_grafico_plujosos)
    plt.close()

    # Gráfico 5: Comparación entre "Més variació interanual" y "Menys variació interanual"
    plt.figure(figsize=(10, 6))
    plt.bar([str(any) for any in anys_mes_variacio], valors_mes_variacio, color='green', label="Més variació interanual")
    plt.bar([str(any) for any in anys_menys_variacio], valors_menys_variacio, color='orange', label="Menys variació interanual")
    plt.title("Comparació: Variació interanual")
    plt.xlabel("Anys")
    plt.ylabel("Variació (%)")
    plt.grid(axis='y')
    plt.legend()
    nombre_grafico_variacio = f"img/{prefijo}_grafic_comparacio_variacio.png"
    plt.savefig(nombre_grafico_variacio)
    plt.close()

    print(f"Gráficos guardados como imágenes PNG para {archivo}:")
    print(f"  {nombre_grafico_plujosos}")
    print(f"  {nombre_grafico_variacio}")
