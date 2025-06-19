import csv
import shutil
import os
import pandas as pd
from collections import Counter

# función para abirnuevos archivos .csv, esta funcion copia el archivo con la ruta indicada
# y lo copia en la carpeta Data

dataDir = "./Data" #Ruta donde se almacenara
# Lista para guardar los DataFrames
dataframes = []


#Esta funcion toma tres argumentos, el nombre del proyecto, el nombre del archivo que se guardara y el indice que llevara el archivo
def newFile(projecName,dirPath,indice):
    projectDir = os.path.join(dataDir,projecName)
    

    # #Por precausión se creara la carpeta si no existe
    if not os.path.exists(dataDir):
        os.makedirs(dataDir)
    if not os.path.exists(projectDir):
        os.mkdir(projectDir)

    #Verificando si el archivo .csv existe en la carpeta del usuario
    if os.path.isfile(dirPath) and dirPath.lower().endswith(".csv"):
        #Obteniendo el nombre
        nombre = os.path.basename(dirPath)
        #Ruta de destino
        destino = os.path.join(projectDir,f"{indice}-{nombre}")

        #Copiando el archivo a la carpeta
        shutil.copy(dirPath,destino)
        print(f"Se copio el archivo {nombre} exitosamente")
        return {
            "type":"SUCCESS",
            "msg":f"Se copio el archivo {nombre} exitosamente"
        }
    else:
        return {
            "type":"WARNING",
            "msg":f"El archivo {dirPath} no existe o no es una ruta valida"
        }


def CreateDashboard(pn, paths):
    result = []
    for i,r in enumerate(paths):
         result.append(newFile(pn,r,i))

    #Uniendo datos
    result.append(JoinFiles(pn))

    return result
    

def JoinFiles(pn):
    projectDir = os.path.join(dataDir,pn) 
    uniqueFile = os.path.join(projectDir,f"{pn}.csv")
    if os.listdir(projectDir):
        archivos = sorted([f for f in os.listdir(projectDir) if f.endswith('.csv')])
        # Leer y renombrar columnas por cada archivo
        for i, archivo in enumerate(archivos, start=1):
            ruta = os.path.join(projectDir, archivo)
            df = pd.read_csv(ruta)
            # Renombrar columnas a 'fecha_i' y 'valor_i'
            df.columns = [f'fecha_{archivo[0]}', f'valor_{archivo[0]}']
            dataframes.append(df)
        
        # Unir los dataframes por columnas (horizontalmente)
        df_unido = pd.concat(dataframes, axis=1)
        # Guardar en nuevo CSV
        df_unido.to_csv(uniqueFile, index=False)
        print("Unido correctamente")
        return {
            "type": "SUCCESS",
            "msg": "Se importarón los datos correctamente"
        }
    else: 
        print("No hay archivos para unir!")
        return {
                "type":"WARNING",
                "msg":"No se encontraron archivos .csv para unir"
            }
    

def ordenarDatos(pn):
    datos = {
        "temperaturaA": {
            "fechas":[],
            "valores":[]
        },
        "temperaturaE": {
            "fechas":[],
            "valores":[]
        },
        "ph": {
            "fechas":[],
            "valores":[]
        },
        "ppm": {
            "fechas":[],
            "valores":[]
        },
        "humedad": {
            "fechas":[],
            "valores":[]
        },
        "luz": {
            "fechas":[],
            "valores":[]
        },
    }
    dPath = os.path.join(dataDir,pn)
    fPath = os.path.join(dPath,f"{pn}.csv")
    colExt = extraer_columnas_csv(fPath)
    for c,v in colExt.items():
        print(c)
        if c == "fecha_0":
            datos["temperaturaA"]["fechas"] = colExt["fecha_0"]
            datos["temperaturaA"]["valores"] = colExt["valor_0"]
        elif c == "fecha_1":
            datos["temperaturaE"]["fechas"] = colExt["fecha_1"]
            datos["temperaturaE"]["valores"] = colExt["valor_1"]
        elif c == "fecha_2":
            datos["ph"]["fechas"] = colExt["fecha_2"]
            datos["ph"]["valores"] = colExt["valor_2"]
        elif c == "fecha_3":
            datos["ppm"]["fechas"] = colExt["fecha_3"]
            datos["ppm"]["valores"] = colExt["valor_3"]
        elif c == "fecha_4":
            datos["humedad"]["fechas"] = colExt["fecha_4"]
            datos["humedad"]["valores"] = colExt["valor_4"]
        elif c == "fecha_5":
            datos["luz"]["fechas"] = colExt["fecha_5"]
            datos["luz"]["valores"] = colExt["valor_5"]

    
    return datos

def extraer_columnas_csv(ruta_archivo):#Extrae la informacion de cada columna por separado y retorna un diccionario
    columnas = {}
    
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        
        # Inicializar listas vacías para cada encabezado
        for encabezado in lector.fieldnames:
            columnas[encabezado] = []
        
        # Agregar los datos a cada lista
        for fila in lector:
            for encabezado in lector.fieldnames:
                columnas[encabezado].append(fila[encabezado])
    
    return columnas
#Funcion para encontrar el mayor dato y su o sus correspondientes fechas
def mayor_dato(dataList, dateList):
    if not dataList:
        return "Por favor ingresa una lista valida!"
    
    datos = []
    control = False
    for d in dataList[1:]:
        try:
            float(d)
            control = True
        except:
            control = False

        if control:
            datos.append(float(d))
    
    maxNum = max(datos)
    # Buscar todos los índices donde aparece el valor
    indices = [i for i, val in enumerate(dataList) if val == maxNum]

    # Obtener fechas correspondientes
    fechas = [dateList[i] for i in indices]

    return {
        "fecha": fechas,
        "valor" : round(float(maxNum),2)
    }

#Funcion para encontrar el menor dato
def menor_dato(dataList, dateList):
    if not dataList:
        return "Por favor ingresa una lista valida!"
    
    datos = []
    control = False
    for d in dataList[1:]:
        try:
            float(d)
            control = True
        except:
            control = False

        if control:
            datos.append(float(d))

    minNum = min(datos)
    # Buscar todos los índices donde aparece el valor
    indices = [i for i, val in enumerate(dataList) if val == minNum]

    # Obtener fechas correspondientes
    fechas = [dateList[i] for i in indices]

    return {
        "fecha": fechas,
        "valor" : round(minNum,2)
    }

#Funcion para dar el valor promedio de una lista
def promedio(lista):
    if not lista:
        return "Por favor ingresa una lista valida!"
    else:
        numero = 0
        count = 0
        for num in lista[1:]:
            if num.strip() != '':
                numero = numero + round(float(num),2)
                count = count + 1

        if count == 0:
            return 0
        else:
            return round(numero / count,2)
    
def phType(ph):
    if ph < 7: #Ph acido
        return "ACIDO"
    elif ph > 7: #Ph alcalino
        return "ALCALINO"
    else:
        return "NEUTRO"


def mediana(lista):
    med = 0
    if not lista:
        return 0
    else:
        datos = []
        control = False
        for d in lista[1:]:
            try:
                float(d)
                control = True
            except:
                control = False

            if control:
                datos.append(float(d))


        ordenada = sorted(datos) #Ordenando de menor a mayor
        n = len(ordenada)
        if n % 2 == 0: #n es par, la mediana es el promedio de los 2 números centrales
            med = (float(ordenada[int(n/2)]) + float(ordenada[int((n/2)) - 1])) / 2
        else: #n es impar
            med = float(ordenada[int((n/2) - 0.5)])
        return round(med,2)

def moda(lista):
    if not lista:
        return 0
    else:
        datos = []
        control = False
        for d in lista[1:]:
            try:
                float(d)
                control = True
            except:
                control = False

            if control:
                datos.append(float(d))
                
        # Contamos la frecuencia de cada elemento
        frecuencias = Counter(datos)

        # Obtenemos la frecuencia máxima
        max_frecuencia = max(frecuencias.values())

        # Buscamos todos los elementos con esa frecuencia (puede haber más de una moda)
        modas = [k for k, v in frecuencias.items() if v == max_frecuencia]

        # Si hay una sola moda, la devolvemos como valor simple
        if len(modas) == 1:
            return round(float(modas[0]))
        else:
            return modas  # Si hay múltiples modas, se devuelven en una lista


def varianza(lista):
    if len(lista) == 0:
        return 0  # Evita división entre cero
    else:
        datos = []
        control = False
        for d in lista[1:]:
            try:
                float(d)
                control = True
            except:
                control = False

            if control:
                datos.append(float(d))
                
        media = sum(datos) / len(datos)
        suma_cuadrados = sum((x - media) ** 2 for x in datos)
        varianza = suma_cuadrados / len(datos)  # Para población completa

        return round(varianza,2)
    
def ConvertirAnumero(valores):#Esta funcion convierte texto a numeros
        datos = []
        control = False
        for d in valores:
            try:
                float(d)
                control = True
            except:
                control = False

            if control:
                datos.append(float(d))
            else:
                datos.append(0)
        return datos

def filtroDiaHora(data, objetivo): #Funcion para filtrar fechas por dia, obteniendo como se comporta los valores cada hora
        fechas = data["fechas"][1:]
        valores = data["valores"][1:]
        datos = ConvertirAnumero(valores)
        
        tiemposHora =[]
        tiempos = []
        valorEnTiempo = []
        fechasFiltradas = []
        
        #Separando fechas repetidas
        for f in fechas:
            if not f[0:10] in fechasFiltradas and not "fecha_" in f[0:10]:
                fechasFiltradas.append(f[0:10])
                #print(f[0:10])

        #Filtrando fechas segun objetivo
        for i, f in enumerate(fechas):
            if f[0:10] == objetivo and not "fecha_" in f[0:10]:
               if not f[11:13] in tiemposHora:#Filtrando por hora minutos
                tiemposHora.append(f[11:13])
                tiempos.append(f[11:19])
                valorEnTiempo.append(round(datos[i],2))
                #print(f"datos:  {datos[i]} fechas: {len(fechas)} valores: {len(valores)}")
                #print(f"{f[0:10]} --- {f[11:13]}---{f[11:19]}---{round(float(valores[i]),2)}")
        
        return {
            "tiempo": tiempos,
            "valores": valorEnTiempo,
            "fechas": fechasFiltradas
        }
