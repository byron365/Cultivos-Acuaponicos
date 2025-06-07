from tools.tools import mayor_dato, menor_dato, promedio,phType, CreateDashboard, ordenarDatos, mediana, moda, varianza

def createProject(pn, paths):    
    create = CreateDashboard(pn, paths)   
    return create[-1]#importa el resultado de la unificación de los archivos
    
def StructData(pn):
    result = ordenarDatos(pn) #El resultado seran los datos en bruto de los archivos ingresado, separados para cada variable
    
    #Estructura de los datos los cuales llevaran, maximo, minimo y el promedio y sus fechas correspondientes
    data = {
        "temperaturaA": {
            "title": "Temperatura Ambiente",
            "Max": {
                "fecha":"",
                "valor":None
            },
            "Min": {
                "fecha":"",
                "valor":None
            },
            "Prom": "",
            "mediana": None,
            "moda": None,
            "varianza":None
        },
        "temperaturaE": {
            "title": "Temperatura Estanque",
            "Max": {
                "fecha":"",
                "valor":None
            },
            "Min": {
                "fecha":"",
                "valor":None
            },
            "Prom": "",
            "mediana": None,
            "moda": None,
            "varianza":None
        },
        "ph": {
            "title": "Ph",
            "Max": {
                "fecha":"",
                "valor":None
            },
            "Min": {
                "fecha":"",
                "valor":None
            },
            "Prom": "",
            "mediana": None,
            "moda": None,
            "varianza":None,
            "type": ""
        },
        "ppm": {
            "title": "PPM",
            "Max": {
                "fecha":"",
                "valor":None
            },
            "Min": {
                "fecha":"",
                "valor":None
            },
            "Prom": "",
            "mediana": None,
            "moda": None,
            "varianza":None
        },
        "humedad": {
            "title": "Humedad",
            "Max": {
                "fecha":"",
                "valor":None
            },
            "Min": {
                "fecha":"",
                "valor":None
            },
            "Prom": "",
            "mediana": None,
            "moda": None,
            "varianza":None
        },
        "luz": {
            "title": "Luz",
            "Max": {
                "fecha":"",
                "valor":None
            },
            "Min": {
                "fecha":"",
                "valor":None
            },
            "Prom": "",
            "mediana": None,
            "moda": None,
            "varianza":None
        }
    }
    
    #Caluclando max, min, prom para cada variable ingresada
    for clave, valor in result.items(): 
        if valor["fechas"] or valor["valores"]:#Si el dic en turno tiene valores se calcularan los datos
            
            maxCalc = mayor_dato(valor["valores"],valor["fechas"])#Calculo del maximo valor
            data[clave]["Max"]["fecha"] = maxCalc["fecha"]
            data[clave]["Max"]["valor"] = maxCalc["valor"]

            promCalc = promedio(valor["valores"])#Calculo del prom valor
            data[clave]["Prom"] = promCalc

            minCalc = menor_dato(valor["valores"],valor["fechas"])#Calculo del min valor
            data[clave]["Min"]["fecha"] = minCalc["fecha"]
            data[clave]["Min"]["valor"] = minCalc["valor"]

            medCalc = mediana(valor["valores"])#Caluculando mediana
            data[clave]["mediana"] = medCalc

            modaCalc = moda(valor["valores"])#Caluculando moda
            data[clave]["moda"] = modaCalc

            varCalc = mediana(valor["valores"])#Caluculando varianza
            data[clave]["varianza"] = varCalc
    return data

            
        



