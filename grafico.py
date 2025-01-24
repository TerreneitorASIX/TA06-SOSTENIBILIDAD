import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
archivo = "resultats_P1.csv"
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

# Gráfico 1: Mitjana
plt.figure(figsize=(8, 6))
plt.plot(años_mitjana, mitjana, marker='o', color='blue', label="Mitjana")
plt.title("Mitjana/Precipitació Total")
plt.xlabel("Años")
plt.ylabel("Mitjana")
plt.grid()
plt.legend()
plt.savefig("grafico_mitjana.png")  # Guardar como imagen PNG
plt.close()

# Gráfico 2: Precipitació total
plt.figure(figsize=(8, 6))
plt.plot(años_mitjana, precipitacion_total, marker='o', color='orange', label="Precipitació Total")
plt.title("Precipitació Total")
plt.xlabel("Años")
plt.ylabel("Precipitació (mm)")
plt.grid()
plt.legend()
plt.savefig("grafico_precipitacion_total.png")  # Guardar como imagen PNG
plt.close()

# Gráfico 3: Taxa de variació interanual
plt.figure(figsize=(8, 6))
plt.plot(años_variacio, variacio, marker='o', color='green', label="Taxa de Variació")
plt.title("Taxa de Variació Interanual")
plt.xlabel("Años")
plt.ylabel("Variació (%)")
plt.grid()
plt.legend()
plt.savefig("grafico_variacio_interanual.png")  # Guardar como imagen PNG
plt.close()

print("Gráficos guardados como imágenes PNG:")
print("1. grafico_mitjana.png")
print("2. grafico_precipitacion_total.png")
print("3. grafico_variacio_interanual.png")
