from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon
from PyQt6 import QtGui, QtCore
from theme_library import *


class JarvisButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

    def make_ui(self, thememode: str):
        self.setGeometry(QtCore.QRect(220, 140, 200, 200))
        self.setText("")
        icon4 = QIcon()
        if thememode == "light":
            icon4.addPixmap(
                QtGui.QPixmap("res/icons/light/miclight.svg"),
                QIcon.Mode.Normal,
                QIcon.State.Off,
            )
            self.setStyleSheet(
                """
                *{
                    border:none;
                    background-color: transparent;
                }
                """
            )
            dropshadow_effect = DropsShadow()
            self.setGraphicsEffect(dropshadow_effect)
        else:
            icon4.addPixmap(
                QtGui.QPixmap("res/icons/dark/micdark.svg"),
                QtGui.QIcon.Mode.Normal,
                QtGui.QIcon.State.Off,
            )

        self.setIcon(icon4)
        self.setIconSize(QtCore.QSize(180, 180))
        self.setMouseTracking(True)
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

    # def start_jarvis(self):
    #     self
