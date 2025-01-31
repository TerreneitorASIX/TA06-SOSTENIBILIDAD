import numpy as np
import os
import glob
import csv

# Mapeig dels mesos al català
mesos = ["gener", "febrer", "març", "abril", "maig", "juny", 
         "juliol", "agost", "setembre", "octubre", "novembre", "desembre"]

# Funció per processar un arxiu i generar els resultats
def processar_arxiu(entrada):
    resultats = []
    mitjanes_annuals = {}  # Diccionari per emmagatzemar les mitjanes mensuals de cada any
    precipitacions_annuals = {}  # Diccionari per emmagatzemar la precipitació total de cada any
    taxes_variacio = {}  # Diccionari per emmagatzemar les taxes de variació interanual

    # Obrir el fitxer d'entrada i processar cada línia
    with open(entrada, "r") as arxiu:
        lines = arxiu.readlines()

    # Processar les línies de dades
    for line in lines:
        dades = line.split()
        
        # Comprovem que la línia tingui dades vàlides
        if len(dades) < 3:
            continue
        
        # Extraiem l'any i el mes
        try:
            any = int(dades[0])
            mes = int(dades[1]) - 1  # Ajustem perquè l'índex de mesos comença a 0
        except ValueError:
            continue  # Si hi ha un error en convertir any o mes, ignorem la línia
        
        # Construïm l'etiqueta del mes/any
        etiqueta = f"{mesos[mes]}{any}"
        
        # Extraiem els valors per calcular la mitjana i la precipitació total
        valors = dades[2:]
        
        # Convertir els valors a float per manejar decimals
        try:
            valors_float = [float(v) for v in valors]
        except ValueError:
            continue  # Si hi ha un error en convertir a float, ignorem la línia
        
        # Filtrarem els -999
        valors_valids = [v for v in valors_float if v != -999]
        
        # Calculem la mitjana
        mitjana = np.mean(valors_valids) if valors_valids else 0  # Si no hi ha valors vàlids, considerem la mitjana com 0
        
        # Afegim la mitjana al diccionari per calcular la mitjana anual després
        if any not in mitjanes_annuals:
            mitjanes_annuals[any] = []
            precipitacions_annuals[any] = 0  # Inicialitzem la precipitació total per any
        
        mitjanes_annuals[any].append(mitjana)
        precipitacions_annuals[any] += sum(valors_valids)  # Sumar la precipitació total per l'any

    # Calcular la mitjana anual per cada any i afegir la precipitació total
    for any, mitjanes in mitjanes_annuals.items():
        mitjana_anual = np.mean(mitjanes)
        precipitacio_total = precipitacions_annuals[any]
        
        mitjanes_annuals[any] = mitjana_anual  # Guardem la mitjana anual
        resultats.append([f"Mitjana/Precipitació total", str(any), f"{mitjana_anual:.2f}", f"{precipitacio_total:.2f}"])

    # Calcular la taxa de variació interanual i afegir-la als resultats
    anys_ordenats = sorted(mitjanes_annuals.keys())
    for i in range(1, len(anys_ordenats)):
        any_actual = anys_ordenats[i]
        any_previ = anys_ordenats[i - 1]
        
        mitjana_actual = mitjanes_annuals[any_actual]
        mitjana_previa = mitjanes_annuals[any_previ]
        
        taxa_variacio = ((mitjana_actual - mitjana_previa) / mitjana_previa) * 100
        taxes_variacio[(any_previ, any_actual)] = taxa_variacio  # Guardem la taxa de variació entre els anys consecutius
        
        resultats.append(["Taxa de variació interanual", f"{any_previ}-{any_actual}", f"{taxa_variacio:.2f}%"])

    # Obtenir els 5 anys més plujosos i menys plujosos
    anys_mitjanes_ordenades = sorted(mitjanes_annuals.items(), key=lambda x: x[1], reverse=True)

    # 5 anys més plujosos
    mesos_mes_plujosos = anys_mitjanes_ordenades[:5]
    resultats.append(["5 anys més plujosos:"])
    for any, mitjana in mesos_mes_plujosos:
        resultats.append([str(any), f"{mitjana:.2f}"])

    # 5 anys menys plujosos
    mesos_menos_plujosos = anys_mitjanes_ordenades[-5:]
    resultats.append(["5 anys menys plujosos:"])
    for any, mitjana in mesos_menos_plujosos:
        resultats.append([str(any), f"{mitjana:.2f}"])

    # Obtenir els 5 anys amb més i menys variació interanual
    # Ordenem les taxes de variació interanual de major a menor
    taxes_variacio_ordenades = sorted(taxes_variacio.items(), key=lambda x: x[1], reverse=True)

    # 5 anys amb més variació interanual
    mesos_mes_variacio = taxes_variacio_ordenades[:5]
    resultats.append(["5 anys amb més variació interanual:"])
    for (any_previ, any_actual), taxa in mesos_mes_variacio:
        resultats.append([f"{any_previ}-{any_actual}", f"{taxa:.2f}%"])

    # 5 anys amb menys variació interanual
    mesos_menos_variacio = taxes_variacio_ordenades[-5:]
    resultats.append(["5 anys amb menys variació interanual:"])
    for (any_previ, any_actual), taxa in mesos_menos_variacio:
        resultats.append([f"{any_previ}-{any_actual}", f"{taxa:.2f}%"])

    # Crear el nom del fitxer de sortida basat en el nom del fitxer d'entrada
    nom_sortida = f"../dades/resultats/resultats_{os.path.basename(entrada).split('.')[1]}.csv"

    # Crear el directorio de sortida si no existe
    os.makedirs(os.path.dirname(nom_sortida), exist_ok=True)

    # Guardem els resultats en un fitxer CSV
    with open(nom_sortida, "w", newline='') as fitxer_sortida:
        writer = csv.writer(fitxer_sortida)
        for resultat in resultats:
            writer.writerow(resultat)

    print(f"Els resultats s'han guardat al fitxer '{nom_sortida}'.")

# Busquem tots els fitxers que segueixen el patró "*.dat" a la carpeta dades_netas
arxius = glob.glob("../dades/dades_netas/*.dat")

# Processar cada arxiu trobat
for arxiu in arxius:
    processar_arxiu(arxiu)
