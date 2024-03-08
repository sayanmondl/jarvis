from PyQt6.QtWidgets import QPushButton
from PyQt6 import QtGui, QtCore


class HistoryButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

    def make_ui(self, thememode: str):
        self.setGeometry(QtCore.QRect(420, 20, 61, 61))
        self.setText("")
        icon1 = QtGui.QIcon()

        if thememode == "light":
            icon1.addPixmap(
                QtGui.QPixmap("res/icons/light/historylight.svg"),
                QtGui.QIcon.Mode.Normal,
                QtGui.QIcon.State.Off,
            )
        else:
            icon1.addPixmap(
                QtGui.QPixmap("res/icons/dark/historydark.svg"),
                QtGui.QIcon.Mode.Normal,
                QtGui.QIcon.State.Off,
            )

        self.setIcon(icon1)
        self.setIconSize(QtCore.QSize(48, 48))
        self.setMouseTracking(True)
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
