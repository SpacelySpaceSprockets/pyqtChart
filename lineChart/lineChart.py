import sys

from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtGui import QPolygonF, QPainter, QColor, QPen
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QPointF

import numpy as np

class MyChartView(QChartView):
	line_series = None

	def __init__(self, parent=None):
		super().__init__(parent)

		self.setRenderHint(QPainter.Antialiasing)

		self.chart = QChart()
		self.chart.setTitle("Simple Line Chart Example")
		self.chart.legend().hide()

		self.setData() # This needs to be called before self.line_series is referenced
		
		self.chart.addSeries(self.line_series)
		self.chart.createDefaultAxes()

		self.setChart(self.chart)

		
		
	def setData(self):
		self.line_series = QLineSeries()

		self.line_series.append(0,6)
		self.line_series.append(2,4)
		self.line_series.append(3,8)
		self.line_series.append(7,4)
		self.line_series.append(10,5)
		self.line_series.append(QPointF(11,1))
		self.line_series.append(QPointF(13,3))

		

class PlotWindow(QMainWindow):
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

	window = PlotWindow()
	window.resize(500,500)

	sys.exit(app.exec_())