import sys
from PySide import QtGui

class PySideUI(QtGui.QMainWindow):

	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.resize(400,400)
		self.setupUI()
		self.setWindowTitle('Window Title')
		self.show()


	def setupUI(self):
		self.centralWidget = QtGui.QWidget(self)
		self.main_layout = QtGui.QVBoxLayout(self.centralWidget)
		self.main_layout.setSpacing(4)

		self.button = QtGui.QPushButton(self)
		self.button.setText('Click Here')
		self.main_layout.addWidget(self.button)

		self.setCentralWidget(self.centralWidget)



if __name__ == "__main__":
	application = QtGui.QApplication(sys.argv)
	mainWindow = PySideUI()
	QtGui.QApplication.processEvents()
sys.exit(application.exec_())
