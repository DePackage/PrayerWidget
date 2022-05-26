import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
							QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QPoint

class MyApp(QWidget):
	def __init__(self):
		super().__init__()
		self.window_width, self.window_height = 150, 50
		self.setMinimumSize(self.window_width, self.window_height)
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setStyleSheet('''
			QWidget {
                background-color: #333333;
				font-size: 60px;
			}
		''')		
        
		#self.lineEdit = QLineEdit(self)
		#self.lineEdit.setGeometry(200, 50, 200, 50)

		#self.btn = QPushButton('Hello', self)
		#self.btn.setGeometry(250, 250, 300, 300)
			
	# action #1
	def mousePressEvent(self, event):
		self.oldPosition = event.globalPos()

	# action #2
	def mouseMoveEvent(self, event):
		delta = QPoint(event.globalPos() - self.oldPosition)
		self.move(self.x() + delta.x(), self.y() + delta.y())
		self.oldPosition = event.globalPos()


if __name__ == '__main__':
	# don't auto scale when drag app to a different monitor.
	# QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
	
	app = QApplication(sys.argv)
	
	myApp = MyApp()
	myApp.show()

	try:
		sys.exit(app.exec_())
	except SystemExit:
		print('Closing Window...')
