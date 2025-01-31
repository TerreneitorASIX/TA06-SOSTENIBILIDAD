import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
archivo = "../E02/dades/resultats/resultats_P1.csv"
df = pd.read_csv(archivo, header=None, names=["Tipo", "Col2", "Col3", "Col4"])

# Filtrar datos para "Mitjana/Precipitació total"
df_mitjana = df[df["Tipo"] == "Mitjana/Precipitació total"]
años_mitjana = df_mitjana["Col2"].astype(int)  # Convertir a años (int)
mitjana = df_mitjana["Col3"].astype(float)
precipitacion_total = df_mitjana["Col4"].astype(float)

# Filtrar datos para "Taxa de variació interanual"
df_variacio = df[df["Tipo"] == "Taxa de variació interanual"]
años_variacio = df_variacio["Col2"].str.split("-").str[1].astype(int)  # Tomar el segundo año del intervalo
variacio = df_variacio["Col3"].str.replace("%", "").astype(float)  # Eliminar el símbolo '%' y convertir a float

# Datos simulados basados en la imagen (debe ser reemplazado con los datos del CSV si es necesario)
anys_mes_plujosos = [2009, 2016, 2007, 2046, 2042]
valors_mes_plujosos = [4.72, 4.71, 4.49, 4.44, 4.33]

anys_menys_plujosos = [2087, 2093, 2081, 2098, 2084]
valors_menys_plujosos = [1.96, 1.90, 1.79, 1.55, 1.41]

anys_mes_variacio = [2099, 2039, 2085, 2083, 2025]
valors_mes_variacio = [96.59, 84.32, 76.09, 73.28, 58.32]

anys_menys_variacio = [2021, 2062, 2098, 2038, 2084]
valors_menys_variacio = [-39.09, -39.55, -48.00, -48.18, -64.42]

# Gráfico 1: Mitjana
plt.figure(figsize=(8, 6))
plt.plot(años_mitjana, mitjana, marker='o', color='blue', label="Mitjana")
plt.title("Mitjana/Precipitació Total")
plt.xlabel("Años")
plt.ylabel("Mitjana")
plt.grid()
plt.legend()
plt.savefig("Imatges/grafico_mitjana.png")  # Guardar como imagen PNG
plt.close()

# Gráfico 2: Precipitació total
plt.figure(figsize=(8, 6))
plt.plot(años_mitjana, precipitacion_total, marker='o', color='orange', label="Precipitació Total")
plt.title("Precipitació Total")
plt.xlabel("Años")
plt.ylabel("Precipitació (mm)")
plt.grid()
plt.legend()
plt.savefig("Imatges/grafic_precipitacio_total.png")  # Guardar como imagen PNG
plt.close()

# Gráfico 3: Taxa de variació interanual
plt.figure(figsize=(8, 6))
plt.plot(años_variacio, variacio, marker='o', color='green', label="Taxa de Variació")
plt.title("Taxa de Variació Interanual")
plt.xlabel("Años")
plt.ylabel("Variació (%)")
plt.grid()
plt.legend()
plt.savefig("Imatges/grafic_variacio_interanual.png")  # Guardar como imagen PNG
plt.close()


# Gráfico 4: Comparación entre "5 anys més plujosos" y "5 anys menys plujosos" (Barras)
plt.figure(figsize=(10, 6))
plt.bar([str(any) for any in anys_mes_plujosos], valors_mes_plujosos, color='blue', label="5 anys més plujosos")
plt.bar([str(any) for any in anys_menys_plujosos], valors_menys_plujosos, color='red', label="5 anys menys plujosos")
plt.title("Comparació: Anys més i menys plujosos")
plt.xlabel("Anys")
plt.ylabel("Precipitació (mm)")
plt.grid(axis='y')
plt.legend()
plt.savefig("Imatges/grafic_comparacio_plujosos.png")
plt.close()

# Gráfico 5: Comparación entre "Més variació interanual" y "Menys variació interanual" (Barras)
plt.figure(figsize=(10, 6))
plt.bar([str(any) for any in anys_mes_variacio], valors_mes_variacio, color='green', label="Més variació interanual")
plt.bar([str(any) for any in anys_menys_variacio], valors_menys_variacio, color='orange', label="Menys variació interanual")
plt.title("Comparació: Variació interanual")
plt.xlabel("Anys")
plt.ylabel("Variació (%)")
plt.grid(axis='y')
plt.legend()
plt.savefig("Imatges/grafic_comparacio_variacio.png")
plt.close()

print("Gráficos guardados como imágenes PNG:")
print("1. grafic_mitjana.png")
print("2. grafic_precipitacio_total.png")
print("3. grafic_variacio_interanual.png")
print("4. grafic_comparacio_plujosos.png")
print("5. grafic_comparacio_variacio.png")