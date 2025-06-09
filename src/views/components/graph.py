from PySide6.QtWidgets import QApplication
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QDateTimeAxis, QValueAxis
from PySide6.QtCore import QDateTime, Qt, QSize
from PySide6.QtGui import QPainter
import sys
import datetime

class Ui_lineGraph(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(100, 200)
        Main.setMaximumSize(QSize(600, 450))

        # Datos de ejemplo
        fechas = []
        valores = []

        # Crear la serie de datos
        series = QLineSeries()
        for f_str, v in zip(fechas, valores):
            dt = datetime.datetime.strptime(f_str, "%Y-%m-%d")
            qdt = QDateTime(dt)
            # QDateTimeAxis usa milisegundos desde epoch
            msec = qdt.toMSecsSinceEpoch()
            series.append(msec, v)

        # Crear el chart y añadir la serie
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Valores a lo largo del tiempo")
        chart.legend().hide()

        # Eje X: Fecha/Hora
        axis_x = QDateTimeAxis()
        axis_x.setFormat("dd MMM yyyy")
        axis_x.setTitleText("Fecha")
        axis_x.setTickCount(len(fechas) + 1)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        # Eje Y: Valores numéricos
        axis_y = QValueAxis()
        axis_y.setLabelFormat("%d")
        axis_y.setTitleText("Valor")
        min_val, max_val = min(valores), max(valores)
        axis_y.setRange(min_val - 5, max_val + 5)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        # Crear la vista del chart y asignar
        chart_view = QChartView(chart)
        # Habilitar antialiasing correctamente
        chart_view.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chart_view)
