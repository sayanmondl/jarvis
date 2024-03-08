from PyQt6.QtWidgets import QPushButton
from PyQt6 import QtGui, QtCore
import json


class SettingsManager:
    def __init__(self):
        pass

    def load_settings(self):
        with open("data/settings.json", "r") as file:
            return json.load(file)

    def save_settings(self, settings):
        with open("data/settings.json", "w") as file:
            json.dump(settings, file)


class SettingsButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

    def make_ui(self, thememode: str):
        self.setGeometry(QtCore.QRect(560, 20, 61, 61))
        self.setText("")
        icon3 = QtGui.QIcon()
        if thememode == "light":
            icon3.addPixmap(
                QtGui.QPixmap("res/icons/light/settingslight.svg"),
                QtGui.QIcon.Mode.Normal,
                QtGui.QIcon.State.Off,
            )
        else:
            icon3.addPixmap(
                QtGui.QPixmap("res/icons/dark/settingsdark.svg"),
                QtGui.QIcon.Mode.Normal,
                QtGui.QIcon.State.Off,
            )

        self.setIcon(icon3)
        self.setIconSize(QtCore.QSize(48, 48))
        self.setMouseTracking(True)
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
