import os

def llegir_primers_100_línies(fitxer):
    try:
        with open(fitxer, 'r') as file:
            lines = [file.readline().strip() for _ in range(100)]
        for i, line in enumerate(lines):
            print(f"Línia {i+1}: {line}")
        return lines
    except Exception as e:
        print(f"Error al llegir el fitxer {fitxer}: {e}")
        return None

def processar_arxius(directori_origen, directori_destí):
    try:
        # Crear el directorio de destino si no existe
        os.makedirs(directori_destí, exist_ok=True)

        # Obtener todos los archivos .dat del directorio de origen
        arxius_dat = [f for f in os.listdir(directori_origen) if f.endswith('.dat')]
        
        for arxiu in arxius_dat:
            ruta_fitxer = os.path.join(directori_origen, arxiu)
            print(f"Processant l'arxiu: {ruta_fitxer}")
            
            # Leer las primeras 100 líneas del archivo
            lines = llegir_primers_100_línies(ruta_fitxer)
            
            if lines:
                # Crear un nuevo nombre para el archivo con "REGRESION"
                nom_nou_fitxer = arxiu.replace('.dat', '.REGRESION.dat')
                ruta_nou_fitxer = os.path.join(directori_destí, nom_nou_fitxer)
                
                # Guardar el nuevo archivo
                with open(ruta_nou_fitxer, 'w') as nou_fitxer:
                    nou_fitxer.write('\n'.join(lines))
                
                print(f"Nou fitxer creat: {ruta_nou_fitxer}")
    except Exception as e:
        print(f"Error en processar els arxius: {e}")

# Exemple d'ús
directori_origen = "../dades/dades_sin_ordenar"
directori_destí = "../dades/dades_procesades"
processar_arxius(directori_origen, directori_destí)
