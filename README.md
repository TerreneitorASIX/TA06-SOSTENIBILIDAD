## Exercici1
Para pedir la API nos dirigimos aqui → [https://opendata.aemet.es/centrodedescargas/altaUsuario](https://opendata.aemet.es/centrodedescargas/altaUsuario)
Nos aparecerá lo siguiente

![API](https://github.com/user-attachments/assets/7127f683-0c69-494a-a9fc-4766a76c9fbd)

Introduciremos el correo, y nos llegara un correo, donde deberemos de darle para confirmar la API
![Correo1](https://github.com/user-attachments/assets/01d3a146-eb53-416c-a60c-b86128b90748)

Y nos llegará otro correo con la API
![API_Recibido](https://github.com/user-attachments/assets/34993652-4144-4987-86c5-39100f2ed25f)

Entramos en la página web de predicción climática, filtramos según los datos deseados y nos descargamos el último archivo que es el que nos interesa.
[https://www.aemet.es/es/serviciosclimaticos/cambio_climat/datos_diarios?w=0&w2=0&cm=analogos_rej&mo=MIROC5&es=RCP60&va=precip&pe=2006-2100&b=1
](https://www.aemet.es/es/serviciosclimaticos/cambio_climat/datos_diarios?w=0&w2=0&cm=analogos_rej&mo=MIROC5&es=RCP60&va=precip&pe=2006-2100&b=1)

![Descargar_Datos](https://github.com/user-attachments/assets/9d5776cb-2ea2-402a-8233-40989dfcb0ef)

Lectura de fitxers: Cal assegurar-se que tots els fitxers tenen el mateix format. I les dades són correctes i no provoquen cap mena d’error.
## Exercici2
## PAS1- Revisar les capçaleres, separació entre dades, comentaris …
Saber com estan delimitades les dades (Espais, comes o tabulació)
Quines columnes hi ha i quins tipus de dades

Los datos obtenidos son datos de Precipitaciones Micro etc 
![image](https://github.com/user-attachments/assets/2336598e-70eb-4b58-b2f7-224fa4bb0a29)

## PAS2- Verificar que tots els arxius tenen el mateix format. 
Es pot fer un script de validació bàsica que llegeixi les primeres files de cada arxiu i determini el nombre de columnes i delimitadors.

Al ejecutar el código nos aparece lo siguiente
![image](https://github.com/user-attachments/assets/be8a5ea0-e64c-4d26-935b-ac3b470985d4)

Aquí podemos visualizar como el delimitador hay dos opciones

1. ‘\t’ → El cual nos indica que el delimitador es una tabulación
2. ‘,’ → La coma nos indica que el delimitador es una coma 

Además de poder ver el número de columnas el cual se ha detectado.

## PAS3- Netejar les dades: 
Assegurar que les dades no continguin errors, valors que falten o inconsistències:
Lectura: Utilitzar  pandas per gestionar els fitxers i gestionar errors de lectura.
Verifica la consistència de les columnes: Assegurar que les dades a cada columna tenen el tipus esperat (numèric, data, etc.).
Gestionar valors que falten o corruptes: Identifica i tracta dades nul·les o valors  atípics.

Utilizamos pandas para gestionar toda la carpeta con los archivos que tenemos, y los valores que no corresponden, o son negativos los hemos omitido.
Por ende cuando vemos los datos limpios tras ejecutar el código veremos lo siguiente

![image](https://github.com/user-attachments/assets/3d74a41a-1c3c-4788-a96a-6ed67d47046f)

## PAS4- Documenta tot el procés per si l’has de repetir alguna vegada.
Indica quines decisions has pres, que has fet amb els valors nuls i com has solucionat inconsistències.

Calcular el percentatge de dades mancants (-999)
Utilizamos el código anterior del paso anterior y lo actualizamos para poder sacar las medias de los -999, al final de los archivos.
Para ver el código: [TA06-SOSTENIBILIDAD/E02/code/PAS4-MEDIA-999.py at main · TerreneitorASIX/TA06-SOSTENIBILIDAD  
](https://github.com/TerreneitorASIX/TA06-SOSTENIBILIDAD/blob/main/E02/code/PAS4-MEDIA-999.py)

Calcular estadístiques: de les dades processades.
Mitjanes i totals anuals: Mostra la precipitació total i mitjana per any.
Tendència de canvi: La taxa de variació anual de les precipitacions.
Extrems: Els anys més plujosos i més secs.
Analitzar les dades: pensar quines estadístiques té sentit fer. I afegir com a mínim dues més.
El código procesa datos meteorológicos para calcular estadísticas clave sobre precipitaciones anuales, tendencias y extremos. Utiliza archivos .dat como entrada y genera archivos CSV con los resultados.
Estadísticas Calculadas:
Promedios y Totales Anuales:
Precipitación promedio y total por año.
Tendencias de Cambio:
Tasa de variación interanual (%).
Extremos:
Los 5 años más lluviosos y los 5 menos lluviosos.
Los 5 años con mayor y menor variación interanual.
Flujo del Código:
Procesamiento de Archivos:
Lee datos meteorológicos.
Filtra valores inválidos (-999).
Calcula estadísticas como promedios, totales y tasas de cambio.
Identificación de Extremos:
Ordena años por precipitaciones y variaciones interanuales.
Generación de Resultados:
Crea un archivo CSV para cada archivo procesado.
Verificación:
Muestra el contenido de los CSV generados.



Conclusión de Documentación general:
En general han ido bien estos dos primeros ejercicios, el ultima dia de entrega nos pasó que al momento de subir un último archivo se nos corrompió el repositorio y nos tocó volver a subir todo a un nuevo Repositorio, en el intento a Bryan casi le explota el ordenador al subir más de 30000 archivos. Peto dos veces pero se pudo subir. 😀
Posdata el github del escritorio va muy bien pero hace que el visual studio haga que pete el ordenador.


## Exercici 3:
Para hacer este ejercicio, hemos cogido el codigo del paso anterior que generaba un archivo con las estadisticas que necesitamos como base y con ese mismo codigo ahora genera los datos a partir de los archivos limpios y ademas saca los datos por terminal (estadisticas.py), este script (como el anterior) genera los datos en .csv, tambien imprime errores en un archivo log.

A continuación tendremos la captura de una de las graficas

![image](https://github.com/TerreneitorASIX/TA06-SOSTENIBILIDAD/blob/a29d254c1c0bdb04569400056318873fd1125d93/E04/img/resultats_P10004_grafic_comparacio_plujosos.png)

El siguiente paso (graficos.py) coge el archivo generado por el punto anterior (resultats_PX.csv) y genera 5 graficos; Precipitacio mitjana, total, taxa de variacio, anys més i menys plujosos, mes i menys variació interanual.

## Exercici 4:

En este ejercicio nuestro objetivo es poder publicar una página web funcional mediante el GitHub, teniendo en nuestra página diferentes lenguajes de programación como pueden ser:
- HTML
- CSS
- JavaScript

Los datos utilizados son los datos que hemos ido realizando durante este 

También tenemos un buscador donde puedes buscar por algún archivo en concreto, y al darle clic podrás visualizar diferentes datos como pueden ser los años con más y menos lluvias, ademas de mostrar los años con menos y mas variación interanual, esto quiere decir que mostrará la diferencia en porcentaje sobre las precipitatciones entre un año y el anterior. Estos datos se mostrarán en 4 grupos donde mostraremos 5 años de cada grupo.
Ademas de que en nuestra pagina podras visualziar las graficas de los datos que se muestran en pantalla. 
A continuación pondremos una captura de nuestra pagina

![image](https://github.com/TerreneitorASIX/TA06-SOSTENIBILIDAD/blob/cd84bf44cfa992e7cae0371cc7fb58562f0f5363/E04/img/Captura%20de%20pantalla%20de%202025-02-06%2009-33-12.png)
