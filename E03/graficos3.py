import matplotlib.pyplot as plt
import glob
import os

# Ruta donde están los CSV
ruta_archivos = "csv/resultats_P*.csv"
archivos = glob.glob(ruta_archivos)  # Encuentra todos los archivos que coincidan con el patrón

if not archivos:
    raise FileNotFoundError(f"No se encontraron archivos que coincidan con el patrón: {ruta_archivos}")

# Procesar cada archivo encontrado
for archivo in archivos:
    print(f"Procesando archivo: {archivo}")
    
    # Inicializar variables para almacenar datos
    anys_mes_plujosos = []
    valors_mes_plujosos = []
    anys_menys_plujosos = []
    valors_menys_plujosos = []
    anys_mes_variacio = []
    valors_mes_variacio = []
    anys_menys_variacio = []
    valors_menys_variacio = []

    # Leer el archivo línea por línea
    with open(archivo, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    # Variables de control
    seccion_actual = None

    # Procesar línea por línea
    for linea in lineas:
        linea = linea.strip()
        if "5 anys més plujosos" in linea:
            seccion_actual = "mes_plujosos"
        elif "5 anys menys plujosos" in linea:
            seccion_actual = "menys_plujosos"
        elif "5 anys amb més variació interanual" in linea:
            seccion_actual = "mes_variacio"
        elif "5 anys amb menys variació interanual" in linea:
            seccion_actual = "menys_variacio"
        elif linea:  # Procesar datos si no es una línea vacía
            try:
                any, valor = linea.split(",")
                any = any.strip()
                valor = float(valor.strip().replace("%", ""))  # Convertir a float, eliminando '%'
                if seccion_actual == "mes_plujosos":
                    anys_mes_plujosos.append(any)
                    valors_mes_plujosos.append(valor)
                elif seccion_actual == "menys_plujosos":
                    anys_menys_plujosos.append(any)
                    valors_menys_plujosos.append(valor)
                elif seccion_actual == "mes_variacio":
                    anys_mes_variacio.append(any)
                    valors_mes_variacio.append(valor)
                elif seccion_actual == "menys_variacio":
                    anys_menys_variacio.append(any)
                    valors_menys_variacio.append(valor)
            except ValueError:
                print(f"Error procesando línea: {linea}")

    # Crear gráficos para este archivo
    # Obtener el prefijo del nombre del archivo (por ejemplo, 'resultats_P1')
    prefijo = os.path.splitext(os.path.basename(archivo))[0]

    # Gráfico 1: Comparación entre "5 anys més plujosos" y "5 anys menys plujosos"
    plt.figure(figsize=(10, 6))
    plt.bar([str(any) for any in anys_mes_plujosos], valors_mes_plujosos, color='blue', label="5 anys més plujosos")
    plt.bar([str(any) for any in anys_menys_plujosos], valors_menys_plujosos, color='red', label="5 anys menys plujosos")
    plt.title(f"{prefijo}: Comparació Anys més i menys plujosos")
    plt.xlabel("Anys")
    plt.ylabel("Precipitació (mm)")
    plt.grid(axis='y')
    plt.legend()
    nombre_grafico_plujosos = f"img/{prefijo}_grafic_comparacio_plujosos.png"
    plt.savefig(nombre_grafico_plujosos)
    plt.close()

    # Gráfico 2: Comparación entre "Més variació interanual" y "Menys variació interanual"
    plt.figure(figsize=(10, 6))
    plt.bar([str(any) for any in anys_mes_variacio], valors_mes_variacio, color='green', label="Més variació interanual")
    plt.bar([str(any) for any in anys_menys_variacio], valors_menys_variacio, color='orange', label="Menys variació interanual")
    plt.title(f"{prefijo}: Comparació Variació interanual")
    plt.xlabel("Anys")
    plt.ylabel("Variació (%)")
    plt.grid(axis='y')
    plt.legend()
    nombre_grafico_variacio = f"img/{prefijo}_grafic_comparacio_variacio.png"
    plt.savefig(nombre_grafico_variacio)
    plt.close()

    print(f"Gráficos generados para {archivo}:")
    print(f"  {nombre_grafico_plujosos}")
    print(f"  {nombre_grafico_variacio}")
