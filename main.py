from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QWidget
from PySide6.QtCore import Qt
import sys, os
from src.views.mainWindow import Ui_MainWindow
from tools.structure import createProject, StructData
from src.views.newProyectWindow import Ui_Form
from src.views.dashWindow import Ui_FormDash
from src.views.components.dataView import Ui_dataView


#------------------Clases para las subventanas--------------------------
#Clase de la ventana de Crear proyecto nuevo
class NewProyectWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

#Clase para la ventana de Dashboard
class DashWindow(QWidget,Ui_FormDash):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

#--------------------Clases para los componentes----------------------
class DataView(QWidget, Ui_dataView):
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

        #Añadiendo informacion
        self.Title.setText(data["title"])
        self.maxLb.setText(str(data["Max"]["valor"]))
        self.promLb.setText(str(data["Prom"]))
        self.minLb.setText(str(data["Min"]["valor"]))
        self.medLb.setText(str(data["mediana"]))
        self.modLb.setText(str(data["moda"]))
        self.varLb.setText(str(data["varianza"]))

        


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Eventos de botones
        self.createBtn.clicked.connect(self.openNewP)
        self.RecentBtn.clicked.connect(self.openRecentP)

    def openNewP(self):
        #Funcion para crear dashboards
        self.createWindow = NewProyectWindow()
        self.createWindow.show()

        self.createWindow.createDashBtn.clicked.connect(self.dashBoardCreate)

        #Botones para buscar archivos
        self.createWindow.fTaBtn.clicked.connect(self.searchPath1)
        self.createWindow.fTeBtn.clicked.connect(self.searchPath2)
        self.createWindow.fPhBtn.clicked.connect(self.searchPath3)
        self.createWindow.fPpmBtn.clicked.connect(self.searchPath4)
        self.createWindow.fHumBtn.clicked.connect(self.searchPath5)
        self.createWindow.fLuzBtn.clicked.connect(self.searchPath6)
        self.close()

    def openRecentP(self):
        print("Abriendo proyecto reciente")

    def dashBoardCreate(self):#Funcion que evalua si se puede crear el dashboard al precionar el boton
        projectName = self.createWindow.nameLE.text()
        if not projectName.strip():
            QMessageBox.warning(self,"Nombre inválido", "El nombre ya existe o se encuentra vacío")
        else:
            paths = [self.createWindow.LeTa.text(), self.createWindow.LeTe.text(),
                 self.createWindow.LePh.text(),self.createWindow.LePpm.text(),
                 self.createWindow.LeHum.text(),self.createWindow.LeLuz.text()]
            result = createProject(projectName,paths)

            if result['type'] == 'SUCCESS':
                #Abriendo dashboard
                self.dashWindow = DashWindow()

                #Estructurando datos para enviarlos al dashWindow
                data = StructData(projectName)

                #Agregando componentes al dashWindow
                for de,val in data.items():
                    if val["Max"]["valor"]:
                        self.dashWindow.centralCtn.addWidget(DataView(val))
                self.dashWindow.show()
                self.createWindow.close() #Cerrando ventana de proyectos
            elif result['type'] == "WARNING":
                QMessageBox.warning(self,"Ocurrio un error", result['msg'])


    def searchPath1(self):
        ruta = QFileDialog.getOpenFileName(self,"Selecciona un archivo .csv","","Archivos CSV (*.csv)")
        self.createWindow.LeTa.setText(ruta[0])
    
    def searchPath2(self):
        ruta = QFileDialog.getOpenFileName(self,"Selecciona un archivo .csv","","Archivos CSV (*.csv)")
        self.createWindow.LeTe.setText(ruta[0])
    
    def searchPath3(self):
        ruta = QFileDialog.getOpenFileName(self,"Selecciona un archivo .csv","","Archivos CSV (*.csv)")
        self.createWindow.LePh.setText(ruta[0])

    def searchPath4(self):
        ruta = QFileDialog.getOpenFileName(self,"Selecciona un archivo .csv","","Archivos CSV (*.csv)")
        self.createWindow.LePpm.setText(ruta[0])

    def searchPath5(self):
        ruta = QFileDialog.getOpenFileName(self,"Selecciona un archivo .csv","","Archivos CSV (*.csv)")
        self.createWindow.LeHum.setText(ruta[0])

    def searchPath6(self):
        ruta = QFileDialog.getOpenFileName(self,"Selecciona un archivo .csv","","Archivos CSV (*.csv)")
        self.createWindow.LeLuz.setText(ruta[0])



       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())