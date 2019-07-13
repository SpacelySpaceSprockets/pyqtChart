import sys

from PyQt5.QtChart import QChart, QChartView, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from PyQt5.QtGui import QPolygonF, QPainter, QColor, QPen
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QPointF

import numpy as np

class MyChartView(QChartView):
	bar_series = None

	def __init__(self, parent=None):
		super().__init__(parent)

		self.setRenderHint(QPainter.Antialiasing)

		self.chart = QChart()
		self.chart.setTitle("Simple Bar Chart Example")
		self.chart.legend().show()

		self.setData() # This needs to be called before self.bar_series is referenced
		
		self.chart.addSeries(self.bar_series)

		# Now lets generate custom axes
		categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

		axisX = QBarCategoryAxis()
		axisX.append(categories)

		axisY = QValueAxis()
		axisY.setRange(0, 15)

		self.chart.addAxis(axisX, Qt.AlignBottom)
		self.chart.addAxis(axisY, Qt.AlignLeft)

		self.bar_series.attachAxis(axisX)
		self.bar_series.attachAxis(axisY)

		# add the chart to the ChartView and we are done
		self.setChart(self.chart)
		
	def setData(self):
		self.bar_series = QBarSeries()

		set0 = QBarSet("Jane")
		set1 = QBarSet("John")
		set2 = QBarSet("Axel")
		set3 = QBarSet("Mary")
		set4 = QBarSet("Samantha")

		set0 << 1 << 2 << 3 << 4 << 5 << 6
		set1 << 5 << 0 << 0 << 4 << 0 << 7
		set2 << 3 << 5 << 8 << 13 << 8 << 5
		set3 << 5 << 6 << 7 << 3 << 4 << 5
		set4 << 9 << 7 << 5 << 3 << 1 << 2

		self.bar_series.append(set0)
		self.bar_series.append(set1)
		self.bar_series.append(set2)
		self.bar_series.append(set3)
		self.bar_series.append(set4)

class BarChartWindow(QMainWindow):
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

	window = BarChartWindow()
	window.resize(500,500)

	sys.exit(app.exec_())