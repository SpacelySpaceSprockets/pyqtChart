import sys

from PyQt5.QtChart import QChart, QChartView, QLineSeries, QScatterSeries
from PyQt5.QtGui import QPolygonF, QPainter
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QPointF

import numpy as np

class myChartView(QChartView):
	scatter_series1 = None
	scatter_series2 = None

	def __init__(self, parent=None):
		super().__init__(parent)

		self.chart = QChart()
		self.chart.setTitle("I like cake")
		self.chart.legend().hide()
		self.setData()
		self.chart.createDefaultAxes()
		self.chart.axisX().setRange(0, 4.5)
		self.chart.axisY().setRange(0, 4.5)

		self.setChart(self.chart)

		self.setRenderHint(QPainter.Antialiasing)
		
		self.scatter_series1.clicked.connect(self.handleClickedPoint)
		self.scatter_series2.clicked.connect(self.handleClickedPoint)
		
	def setData(self):
		self.scatter_series1 = QScatterSeries()
		self.scatter_series2 = QScatterSeries()

		# scatter_series.setName("scatter1")
		self.scatter_series1.setColor(Qt.blue)
		self.scatter_series2.setColor(Qt.red)

		for x in np.arange(0.5, 4.5, 0.5): 
			for y in np.arange(0.5, 4.5, 0.5):
				self.scatter_series1.append(QPointF(x,y))

		self.chart.addSeries(self.scatter_series1)
		self.chart.addSeries(self.scatter_series2)

	def handleClickedPoint(self, point):
		MAX_INT = sys.maxsize
		MIN_INT = -MAX_INT
		distance1 = MAX_INT
		distance2 = MAX_INT

		clicked_point = point
		closest1 = QPointF(MAX_INT, MAX_INT)
		closest2 = QPointF(MAX_INT, MAX_INT)

		point_list1 = self.scatter_series1.pointsVector()
		point_list2 = self.scatter_series2.pointsVector()
		
		for current_point1 in point_list1:
			current_distance1 = self.distance(current_point1, clicked_point)
			if current_distance1 < distance1:
				distance1 = current_distance1
				closest1 = current_point1

		for current_point2 in point_list2:
			current_distance2 = self.distance(current_point2, clicked_point)
			if current_distance2 < distance2:
				distance2 = current_distance2
				closest2 = current_point2

		if distance1 < distance2:
			self.scatter_series1.remove(closest1)
			self.scatter_series2.append(closest1)
		else:
			self.scatter_series2.remove(closest2)
			self.scatter_series1.append(closest2)


	def distance(self, a, b):
		return np.sqrt((a.x()-b.x())*(a.x()-b.x()) + (a.y()-b.y())*(a.y()-b.y()))





class ScatterWindow(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)

		myCV = myChartView(self)


		self.setCentralWidget(myCV)
		self.show()


if __name__ == '__main__':
	import sys
	from PyQt5.QtWidgets import QApplication
	from PyQt5.QtCore import Qt

	app = QApplication(sys.argv)

	window = ScatterWindow()
	window.resize(500,500)

	sys.exit(app.exec_())