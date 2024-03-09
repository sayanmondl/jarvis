from PyQt6 import QtWidgets, QtGui, QtCore
from .settings import *


class ThemeModeButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

    def make_ui(self, thememode: str):
        self.setGeometry(QtCore.QRect(490, 20, 61, 61))
        self.setText("")
        icon2 = QtGui.QIcon()
        if thememode == "light":
            icon2.addPixmap(
                QtGui.QPixmap("res/icons/light/toggledarkmode.svg"),
                QtGui.QIcon.Mode.Normal,
                QtGui.QIcon.State.Off,
            )
        else:
            icon2.addPixmap(
                QtGui.QPixmap("res/icons/dark/togglelightmode.svg"),
                QtGui.QIcon.Mode.Normal,
                QtGui.QIcon.State.Off,
            )

        self.setIcon(icon2)
        self.setIconSize(QtCore.QSize(48, 48))
        self.setMouseTracking(True)
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))


class Theme:
    def __init__(self):
        self.settings_manager = SettingsManager()
        self.settings = self.settings_manager.load_settings()

    def change_theme(self) -> str:
        if self.settings["theme_mode"] == "light":
            self.settings["theme_mode"] = "dark"
        else:
            self.settings["theme_mode"] = "light"

        self.settings_manager.save_settings(self.settings)
        return self.settings["theme_mode"]


class DropsShadow(QtWidgets.QGraphicsDropShadowEffect):
    def __init__(self):
        super().__init__()
        self.setColor(QtGui.QColor("#BFBFBF"))
        self.setOffset(QtCore.QPointF(0, 4))
        self.setBlurRadius(8)
