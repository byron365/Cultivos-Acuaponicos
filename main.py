from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QWidget, QDockWidget,QVBoxLayout,QScrollArea
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QDateTimeAxis, QValueAxis
import random
from PySide6.QtCore import Qt,QDateTime,QPointF, QMargins, QSize
from PySide6.QtGui import QPainter,QBrush, QColor
import sys, os
from datetime import datetime
from tools.structure import createProject, StructData
from src.views.newProyectView import Ui_centralCtn
from src.views.dashView import Ui_FormDash
from src.views.components.dataView import Ui_DataView
from src.views.components.graph import Ui_lineGraph
from src.views.mainWindow import Ui_MainWindow
from src.views.mainCtn import Ui_mainCtn
from src.views.components.Dock import Ui_DockWidget
from typing import List, Dict, Union
from tools.tools import ConvertirAnumero, filtroDiaHora


#------------------Clases para las vistas--------------------------
#Clase de la ventana de Crear proyecto nuevo
class NewProyectWindow(QWidget,Ui_centralCtn):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

#Clase para la ventana de Dashboard
class DashView(QWidget,Ui_FormDash):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class MainCtn(QWidget, Ui_mainCtn):#Componente para mostrar el contenido inicial del programa
    def __init__(self):
        super().__init__()
        self.setupUi(self)

#--------------------Clases para los componentes----------------------
class DataView(QWidget, Ui_DataView):#Componente para mostrar informacion de una variable
    def __init__(self,data):
        super().__init__()
        self.setupUi(self)
        self.Title.setTextFormat(Qt.TextFormat.RichText)
        self.maxLb.setTextFormat(Qt.TextFormat.RichText)
        self.minLb.setTextFormat(Qt.TextFormat.RichText)
        self.promLb.setTextFormat(Qt.TextFormat.RichText)
        self.medLb.setTextFormat(Qt.TextFormat.RichText)
        self.modLb.setTextFormat(Qt.TextFormat.RichText)
        self.varLb.setTextFormat(Qt.TextFormat.RichText)
        self.data = data

        #Añadiendo informacion
        self.Title.setText(data["title"])
        self.maxLb.setText(str(data["Max"]["valor"]))
        self.promLb.setText(str(data["Prom"]))
        self.minLb.setText(str(data["Min"]["valor"]))
        self.medLb.setText(str(data["mediana"]))
        self.modLb.setText(str(data["moda"]))
        self.varLb.setText(str(data["varianza"]))

        #Cambiando grafica segun dia por medio de los botones
        self.count = 0
        self.fechasSeparadas = filtroDiaHora(data,"")
        #print(self.fechasSeparadas)
        self.maxDateBtn.clicked.connect(self.changeMaxDate)
        self.minDateBtn.clicked.connect(self.changeMinDate)

        #Mostradno grafico
        self.grafico = self.lineGraph(data,self.fechasSeparadas["fechas"][self.count])
        self.graphView.addWidget(self.grafico)

        

    def changeMaxDate(self):
        if self.count < len(self.fechasSeparadas):
            self.count += 1
            #Mostradno grafico
            self.graphView.removeWidget(self.grafico)#Removemos el grafico anterior
            self.grafico.deleteLater()
            self.grafico = self.lineGraph(self.data,self.fechasSeparadas["fechas"][self.count])#Creamos el nuevo grafico
            self.graphView.addWidget(self.grafico)#Loagregamos
    
    def changeMinDate(self):
        if self.count > 0:
            self.count -= 1    
            #Mostradno grafico
            self.graphView.removeWidget(self.grafico)#Removemos el grafico anterior
            self.grafico.deleteLater()
            self.grafico = self.lineGraph(self.data,self.fechasSeparadas["fechas"][self.count])#Creamos el nuevo grafico
            self.graphView.addWidget(self.grafico)#Loagregamos

    def lineGraph(self,data,objetivo):
        #Todo: Creando el grafico en base a las horas y valores
        #Filtrando fechas por dia especifico
        datosFiltrados = filtroDiaHora(data,objetivo)

        horas = datosFiltrados["tiempo"]
        valores = datosFiltrados["valores"]

        # Crear la serie
        series = QLineSeries()

        # Convertir las cadenas de tiempo a QDateTime y agregarlas a la serie
        for t_str, valor in zip(horas, valores):
            dt = QDateTime.fromString(t_str, "HH:mm:ss")
            dt.setDate(QDateTime.currentDateTime().date())  # Asegurar una fecha válida
            series.append(dt.toMSecsSinceEpoch(), valor)

        # Crear el gráfico y añadir la serie
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(f"Fecha: {objetivo}")

        # Eje X (Tiempo)
        axis_x = QDateTimeAxis()
        axis_x.setFormat("HH:mm:ss")
        axis_x.setTitleText("Tiempo")
        axis_x.setTickCount(8)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        # Eje Y (Valores)
        axis_y = QValueAxis()
        axis_y.setTitleText("Valor")
        axis_y.setTickCount(8)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        chart.setBackgroundVisible(False)          # Quita fondo general
        chart.setBackgroundBrush(Qt.transparent)   # Fondo transparente
        chart.setPlotAreaBackgroundVisible(False)  # Quita fondo del área de dibujo


        # Crear la vista del gráfico
        chart.legend().hide()#Quita la leyenda
        chart.setMargins(QMargins(0, 0, 0, 0))#Quita los margenes
        chart_view = QChartView(chart)
        return chart_view
       
    
class DockComponent(QDockWidget, Ui_DockWidget):#Componente para mostrar informacion en un Dock
    def __init__(self,titulo,data, LR="Right"):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(titulo)

        #Filtrando informacion para construir los graficos
        #Cambiando grafica segun dia por medio de los botones
        self.data = data
        self.count = 0
        self.fechasSeparadas = []
        for c,v in data.items():
            if v["fechas"]:
                self.fechasSeparadas = filtroDiaHora(v,"")
                break

        self.nextDateBtn.clicked.connect(self.changeMaxDate)
        self.prevDateBtn.clicked.connect(self.changeMinDate)
        self.dataX = []
        self.dataY = []
        self.titulo = []
        self.objetivo = self.fechasSeparadas["fechas"][self.count]
        self.dateLB.setText(self.objetivo)
        #Filtrando para generar graficos
        if LR == "Right":#Dock lado derecho
           self.GraficosRight(self.data)#Generando los graficos del dock derecho
        elif LR == "Left":#Dock Lado izquierdo
            if (self.data["temperaturaA"]["valores"] and self.data["temperaturaE"]["valores"]):
                print("Tenemos ambas temperaturas")
                #Generando grafico de TempE Vs TempA
                self.dataX.append(filtroDiaHora(self.data["temperaturaA"],self.objetivo))#Devovlera los valores,fechas filtradas por hora de la fecha colocada como objetivo
                self.dataY.append(filtroDiaHora(self.data["temperaturaE"],self.objetivo))
                self.titulo.append(f"{self.data["temperaturaA"]["title"]} VS {self.data["temperaturaE"]["title"]} - {self.objetivo}")

        # #Anadiendo graficos al dock
        self.graficos = []
        for i,g in enumerate(self.dataX):
            self.graficos.append(self.crearGraficoDock(self.dataX[i]["valores"], self.dataY[i]["valores"],self.titulo[i]))
            self.scrollItems.addWidget(self.graficos[i])

    def crearGraficoDock(self,xD, yD, titulo) -> QChartView:
        # Crear series
        series = QLineSeries()
        for x, y in zip(xD, yD):
            series.append(x, y)

        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setTitle(titulo)
        chart.legend().hide()#Quita la leyenda

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        widget = QWidget()
        widget.setMinimumSize(QSize(400,400))
        layout = QVBoxLayout(widget)
        layout.addWidget(chart_view)

        return widget
     
    def changeMaxDate(self):
        if self.count < len(self.fechasSeparadas):
            self.count += 1
            self.objetivo = self.fechasSeparadas["fechas"][self.count]
            self.GraficosRight(self.data)
            #Mostradno grafico
            for i,g in enumerate(self.graficos):
                self.scrollItems.removeWidget(self.graficos[i])#Removemos los graficos anteriores
                self.graficos[i].deleteLater()
                self.graficos[i] = self.crearGraficoDock(self.dataX[i]["valores"], self.dataY[i]["valores"],self.titulo[i])#Creamos el nuevo grafico
                self.scrollItems.addWidget(self.graficos[i])#Loagregamos
            
            self.dateLB.setText(self.objetivo)
    
    def changeMinDate(self):
        if self.count > 0:
            self.count -= 1    
            self.objetivo = self.fechasSeparadas["fechas"][self.count]
            self.GraficosRight(self.data)
            #Mostradno grafico
            for i,g in enumerate(self.graficos):
                self.scrollItems.removeWidget(self.graficos[i])#Removemos los graficos anteriores
                self.graficos[i].deleteLater()
                self.graficos[i] = self.crearGraficoDock(self.dataX[i]["valores"], self.dataY[i]["valores"],self.titulo[i])#Creamos el nuevo grafico
                self.scrollItems.addWidget(self.graficos[i])#Loagregamos
            
            self.dateLB.setText(self.objetivo)
    def GraficosRight(self,data):#Actualiza los graficos del dock derecho
         #---------TempA Vs TempE--------
        if (data["temperaturaA"]["valores"] and data["temperaturaE"]["valores"]):
            self.dataX.append(filtroDiaHora(data["temperaturaA"],self.objetivo))#Devovlera los valores,fechas filtradas por hora de la fecha colocada como objetivo
            self.dataY.append(filtroDiaHora(data["temperaturaE"],self.objetivo))
            self.titulo.append(f"{data["temperaturaA"]["title"]} VS {data["temperaturaE"]["title"]} - {self.objetivo}")
        #---------TempA Vs Humedad--------
        if (data["temperaturaA"]["valores"] and data["humedad"]["valores"]):
            self.dataX.append(filtroDiaHora(data["temperaturaA"],self.objetivo))#Devovlera los valores,fechas filtradas por hora de la fecha colocada como objetivo
            self.dataY.append(filtroDiaHora(data["humedad"],self.objetivo))
            self.titulo.append(f"{data["temperaturaA"]["title"]} VS {data["humedad"]["title"]} - {self.objetivo}")
            #---------TempE Vs Ph--------
        if (data["temperaturaE"]["valores"] and data["ph"]["valores"]):
            self.dataX.append(filtroDiaHora(data["temperaturaE"],self.objetivo))#Devovlera los valores,fechas filtradas por hora de la fecha colocada como objetivo
            self.dataY.append(filtroDiaHora(data["ph"],self.objetivo))
            self.titulo.append(f"{data["temperaturaE"]["title"]} VS {data["ph"]["title"]} - {self.objetivo}")
            #---------ppm Vs ph--------
        if (data["ppm"]["valores"] and data["ph"]["valores"]):
            self.dataX.append(filtroDiaHora(data["ppm"],self.objetivo))#Devovlera los valores,fechas filtradas por hora de la fecha colocada como objetivo
            self.dataY.append(filtroDiaHora(data["ph"],self.objetivo))
            self.titulo.append(f"{data["ppm"]["title"]} VS {data["ph"]["title"]} - {self.objetivo}")
        #---------luz Vs ph--------
        if (data["luz"]["valores"] and data["ph"]["valores"]):
            self.dataX.append(filtroDiaHora(data["luz"],self.objetivo))#Devovlera los valores,fechas filtradas por hora de la fecha colocada como objetivo
            self.dataY.append(filtroDiaHora(data["ph"],self.objetivo))
            self.titulo.append(f"{data["luz"]["title"]} VS {data["ph"]["title"]} - {self.objetivo}")
        #---------TempE Vs ppm--------
        if (data["temperaturaE"]["valores"] and data["ppm"]["valores"]):
            self.dataX.append(filtroDiaHora(data["temperaturaE"],self.objetivo))#Devovlera los valores,fechas filtradas por hora de la fecha colocada como objetivo
            self.dataY.append(filtroDiaHora(data["ppm"],self.objetivo))
            self.titulo.append(f"{data["temperaturaE"]["title"]} VS {data["ppm"]["title"]} - {self.objetivo}")

        
        

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Cultivos Acuaponicos")

        self.mainCtn = MainCtn()#Contenido inicial, al comenzar el programa
        #Eventos de botones
        self.mainCtn.createBtn.clicked.connect(self.openNewP)
        self.mainCtn.RecentBtn.clicked.connect(self.openRecentP)
        self.centralCtn.addWidget(self.mainCtn)


    def openNewP(self):
        #Funcion para crear dashboards
        self.createView = NewProyectWindow()
        self.centralCtn.removeWidget(self.mainCtn)#Eliminado contenido inicial
        self.mainCtn.setParent(None)
        self.mainCtn.deleteLater()
        self.centralCtn.addWidget(self.createView)#Agregando contenido de la vista de crear dashboard
        self.resize(780,650)
        self.setWindowTitle("Cultivos Acuaponicos - Nuevo Proyecto")

        self.createView.createDashBtn.clicked.connect(self.dashBoardCreate)

        #Botones para buscar archivos
        self.createView.fTaBtn.clicked.connect(self.searchPath1)
        self.createView.fTeBtn.clicked.connect(self.searchPath2)
        self.createView.fPhBtn.clicked.connect(self.searchPath3)
        self.createView.fPpmBtn.clicked.connect(self.searchPath4)
        self.createView.fHumBtn.clicked.connect(self.searchPath5)
        self.createView.fLuzBtn.clicked.connect(self.searchPath6)

    def openRecentP(self):
        print("Abriendo proyecto reciente")

    def dashBoardCreate(self):#Funcion que evalua si se puede crear el dashboard al precionar el boton
        projectName = self.createView.nameLE.text()
        if os.path.exists(os.path.join("./Data")):
            if not projectName.strip() or projectName in os.listdir(os.path.join("./Data")):
                QMessageBox.warning(self,"Nombre inválido", "El nombre ya existe o se encuentra vacío")
            else:
                paths = [self.createView.LeTa.text(), self.createView.LeTe.text(),
                    self.createView.LePh.text(),self.createView.LePpm.text(),
                    self.createView.LeHum.text(),self.createView.LeLuz.text()]
                
                self.valido = False

                for p in paths:#Filtrando, si alguna url no se encuentra vacia se puede crear el dashboard
                    if p.strip():
                        self.valido = True
                        break

            
                if self.valido:
                    result = createProject(projectName,paths)

                    if result['type'] == 'SUCCESS':
                        #Abriendo dashboard
                        self.dashView = DashView()
                        self.centralCtn.removeWidget(self.createView)#Eliminado contenido inicial
                        self.createView.setParent(None)
                        self.createView.deleteLater()
                        self.centralCtn.addWidget(self.dashView)#Agregando contenido de la vista de crear dashboard
                        self.showMaximized()#Se coloca la ventana al ancho de la pantalla
                        self.setWindowTitle(f"Cultivos Acuaponicos - [{projectName}]")

                        #Estructurando datos para enviarlos al dashView
                        data = StructData(projectName)

                        #Agregando componentes al dashView
                        for de,val in data.items():
                            if val["Max"]["valor"]:
                                self.dashView.centralCtn.addWidget(DataView(val))#Agregando informacion basica
                                #Creando dokcs
                        
                        self.addDockWidget(Qt.RightDockWidgetArea,DockComponent("Información relacionada",data,"Right"))#anadiendo dock de datos relacionados
                        self.addDockWidget(Qt.LeftDockWidgetArea,DockComponent("Información varia",data,"Left"))#dock de datos varios
                        
                    elif result['type'] == "WARNING":
                        QMessageBox.warning(self,"Ocurrio un error", result['msg'])
                else:
                    QMessageBox.warning(self,"Rutas invalidadas", "Las rutas a los archivos .csv se encuentran vacías")
        else:
            os.mkdir(os.path.join("./Data"))#Si no existe la carpeta la creara
            QMessageBox.warning(self,"Carpeta de datos no encontrada", "La carapeta [Data] no se encontro, por lo que se creo, intenta de nuevo")

    def searchPath1(self):
        ruta = QFileDialog.getOpenFileName(self,"Selecciona un archivo .csv","","Archivos CSV (*.csv)")
        self.createView.LeTa.setText(ruta[0])
    
    def searchPath2(self):
        ruta = QFileDialog.getOpenFileName(self,"Selecciona un archivo .csv","","Archivos CSV (*.csv)")
        self.createView.LeTe.setText(ruta[0])
    
    def searchPath3(self):
        ruta = QFileDialog.getOpenFileName(self,"Selecciona un archivo .csv","","Archivos CSV (*.csv)")
        self.createView.LePh.setText(ruta[0])

    def searchPath4(self):
        ruta = QFileDialog.getOpenFileName(self,"Selecciona un archivo .csv","","Archivos CSV (*.csv)")
        self.createView.LePpm.setText(ruta[0])

    def searchPath5(self):
        ruta = QFileDialog.getOpenFileName(self,"Selecciona un archivo .csv","","Archivos CSV (*.csv)")
        self.createView.LeHum.setText(ruta[0])

    def searchPath6(self):
        ruta = QFileDialog.getOpenFileName(self,"Selecciona un archivo .csv","","Archivos CSV (*.csv)")
        self.createView.LeLuz.setText(ruta[0])


    def docksCreate(self,title, data, LR="Right"): #Esta funcion creara los docks para colocar graficos relevantes al dashboard
        dock = DockComponent()
        dock.setWindowTitle(title)
        
        # dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        # dock.resize(400,400)
        # dock.setMinimumSize(QSize(400, 400))
        # dock.setMaximumSize(QSize(400, 1000))
        # dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable|QDockWidget.DockWidgetFeature.DockWidgetMovable)

        #Filtrando informacion para construir los graficos
        self.dataX = []
        self.dataY = []
        titulo = []
        objetivo = "2024-11-06"
        #Filtrando para generar graficos
        # if LR == "Right":#Dock lado derecho
        #     #---------TempA Vs TempE--------
        #     if (data["temperaturaA"]["valores"] and data["temperaturaE"]["valores"]):
        #         self.dataX.append(filtroDiaHora(data["temperaturaA"],objetivo))#Devovlera los valores,fechas filtradas por hora de la fecha colocada como objetivo
        #         self.dataY.append(filtroDiaHora(data["temperaturaE"],objetivo))
        #         titulo.append(f"{data["temperaturaA"]["title"]} VS {data["temperaturaE"]["title"]} - {objetivo}")

        #     #---------TempA Vs Humedad--------
        #     if (data["temperaturaA"]["valores"] and data["humedad"]["valores"]):
        #         self.dataX.append(filtroDiaHora(data["temperaturaA"],objetivo))#Devovlera los valores,fechas filtradas por hora de la fecha colocada como objetivo
        #         self.dataY.append(filtroDiaHora(data["humedad"],objetivo))
        #         titulo.append(f"{data["temperaturaA"]["title"]} VS {data["humedad"]["title"]} - {objetivo}")

        #      #---------TempE Vs Ph--------
        #     if (data["temperaturaE"]["valores"] and data["ph"]["valores"]):
        #         self.dataX.append(filtroDiaHora(data["temperaturaE"],objetivo))#Devovlera los valores,fechas filtradas por hora de la fecha colocada como objetivo
        #         self.dataY.append(filtroDiaHora(data["ph"],objetivo))
        #         titulo.append(f"{data["temperaturaE"]["title"]} VS {data["ph"]["title"]} - {objetivo}")

        #      #---------ppm Vs ph--------
        #     if (data["ppm"]["valores"] and data["ph"]["valores"]):
        #         self.dataX.append(filtroDiaHora(data["ppm"],objetivo))#Devovlera los valores,fechas filtradas por hora de la fecha colocada como objetivo
        #         self.dataY.append(filtroDiaHora(data["ph"],objetivo))
        #         titulo.append(f"{data["ppm"]["title"]} VS {data["ph"]["title"]} - {objetivo}")

        #     #---------luz Vs ph--------
        #     if (data["luz"]["valores"] and data["ph"]["valores"]):
        #         self.dataX.append(filtroDiaHora(data["luz"],objetivo))#Devovlera los valores,fechas filtradas por hora de la fecha colocada como objetivo
        #         self.dataY.append(filtroDiaHora(data["ph"],objetivo))
        #         titulo.append(f"{data["luz"]["title"]} VS {data["ph"]["title"]} - {objetivo}")

        #     #---------TempE Vs ppm--------
        #     if (data["temperaturaE"]["valores"] and data["ppm"]["valores"]):
        #         self.dataX.append(filtroDiaHora(data["temperaturaE"],objetivo))#Devovlera los valores,fechas filtradas por hora de la fecha colocada como objetivo
        #         self.dataY.append(filtroDiaHora(data["ppm"],objetivo))
        #         titulo.append(f"{data["temperaturaE"]["title"]} VS {data["ppm"]["title"]} - {objetivo}")

        # elif LR == "Left":#Dock Lado izquierdo
        #     if (data["temperaturaA"]["valores"] and data["temperaturaE"]["valores"]):
        #         print("Tenemos ambas temperaturas")
        #         #Generando grafico de TempE Vs TempA
        #         self.dataX.append(filtroDiaHora(data["temperaturaA"],objetivo))#Devovlera los valores,fechas filtradas por hora de la fecha colocada como objetivo
        #         self.dataY.append(filtroDiaHora(data["temperaturaE"],objetivo))
        #         titulo.append(f"{data["temperaturaA"]["title"]} VS {data["temperaturaE"]["title"]} - {objetivo}")
              
        # scrollDock = QScrollArea()#Creando el scrollArea para colocar los graficos del dock
        # scrollDock.setWidgetResizable(True)
        # scrollAreaWidgetContents = QWidget()
        # layout = QVBoxLayout(scrollDock)
        # layout.setContentsMargins(0, 0, 0, 0)

        # #Anadiendo graficos al dock
        # for i,g in enumerate(self.dataX):
        #     layout.addWidget(self.crearGraficoDock(self.dataX[i]["valores"], self.dataY[i]["valores"],titulo[i])) 

        # dock.setWidget(scrollDock)
        return dock
        
    
    
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())