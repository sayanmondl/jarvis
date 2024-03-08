import sys
from PyQt6 import QtWidgets
from main_window import MainWindow

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())