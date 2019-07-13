import sys

from PyQt5.QtChart import QChart, QChartView, QLineSeries, QScatterSeries, QLogValueAxis, QValueAxis
from PyQt5.QtGui import QPolygonF, QPainter, QColor, QPen
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QPointF

import numpy as np

class MyChartView(QChartView):
	line_series = None

	def __init__(self, parent=None):
		super().__init__(parent)

		self.chart = QChart()
		self.chart.setTitle("Logaritmic Axis Example")
		self.chart.legend().hide()

		self.setData() # This needs to be called before self.line_series is referenced

		
		# Generate the x axis (non-log)
		axisX = QValueAxis()
		axisX.setTitleText("Data Point")
		axisX.setLabelFormat("%.2f")
		axisX.setTickCount(self.line_series.count())

		self.chart.addAxis(axisX, Qt.AlignBottom)

		# Generate the y axis (log)
		axisY = QLogValueAxis()
		axisY.setTitleText("Values")
		axisY.setBase(10.0)
		axisY.setMinorTickCount(-1)

		self.chart.addAxis(axisY, Qt.AlignLeft)

		self.line_series.attachAxis(axisX)
		self.line_series.attachAxis(axisY)

		self.setChart(self.chart)

		self.setRenderHint(QPainter.Antialiasing)
		
	def setData(self):
		self.line_series = QLineSeries()
		pen = QPen(QColor(70,107,170))
		pen.setWidth(2)
		self.line_series.setPen(pen)

		self.line_series.append(QPointF(1.0,1.0))
		self.line_series.append(QPointF(2.0,73.0))
		self.line_series.append(QPointF(3.0,268.0))
		self.line_series.append(QPointF(4.0,17.0))
		self.line_series.append(QPointF(5.0,4325.0))
		self.line_series.append(QPointF(6.0,723.0))

		self.chart.addSeries(self.line_series)


class LogWindow(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)

		myCV = MyChartView(self)

		self.setCentralWidget(myCV)
		self.show()


if __name__ == '__main__':
	import sys
	from PyQt5.QtWidgets import QApplication
	from PyQt5.QtCore import Qt

	app = QApplication(sys.argv)

	window = LogWindow()
	window.resize(500,500)

	sys.exit(app.exec_())