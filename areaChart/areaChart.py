import sys

from PyQt5.QtChart import QChart, QChartView, QLineSeries, QAreaSeries
from PyQt5.QtGui import QPainter, QColor, QPen, QGradient, QLinearGradient
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QPointF

class MyChartView(QChartView):

	series0 = None
	series1 = None

	def __init__(self, parent=None):
		super().__init__(parent)

		self.setRenderHint(QPainter.Antialiasing)

		self.chart = QChart()
		self.chart.setTitle("Simple Area Chart Example")
		self.chart.legend().show()

		self.setData() # This needs to be called before self.line_series is referenced

		# Here is where we generate the QAreaSeries using the two QLineSeries
		area_series = QAreaSeries(self.series0, self.series1)
		area_series.setName("Batman")

		# We can customize the look of the QAreaSeries
		# The pen determines how the surrounding line is drawn
		pen = QPen(QColor(17,26,43))
		pen.setWidth(3)
		area_series.setPen(pen)
		# We can fill the area with a linear gradient
		gradient = QLinearGradient(QPointF(0,0), QPointF(0,1)) # This describes a vertical gradient
		gradient.setColorAt(0.0, QColor(70,107,170))
		gradient.setColorAt(1.0, QColor(35, 53,85))
		gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
		area_series.setBrush(gradient)

		self.chart.addSeries(area_series)

		# Set up the axes
		self.chart.createDefaultAxes()
		# axes() returns a list of axes, the python method of getting the first element from the list
		# is different from the C++ method (.first())
		self.chart.axes(Qt.Horizontal)[0].setRange(0, 20)
		self.chart.axes(Qt.Vertical)[0].setRange(0, 10)

		self.setChart(self.chart)
		
	def setData(self):
		self.series0 = QLineSeries()
		self.series1 = QLineSeries()

		# showing a few methods that can be used to load up the series data
		self.series0.append(1,5)
		self.series0.append(3,7)
		self.series0.append(7,6)
		self.series0.append(9,7)
		self.series0.append(12,6)
		self.series0.append(QPointF(16,7))
		self.series0.append(QPointF(18,5))

		self.series1 << QPointF(1,3) << QPointF(3,4) << QPointF(7,3) << QPointF(8,2) << QPointF(12,3) << QPointF(16,4) << QPointF(18,3)

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