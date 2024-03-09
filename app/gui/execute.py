from PyQt6.QtWidgets import QPushButton
from PyQt6 import QtGui, QtCore
from ..jarvis.get_voice_input import *

class ExecuteButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

    def make_ui(self, thememode: str):
        self.setGeometry(QtCore.QRect(560, 20, 61, 61))
        self.setText("")
        icon3 = QtGui.QIcon()
        if thememode == "light":
            icon3.addPixmap(
                QtGui.QPixmap("res/icons/light/executelight.svg"),
                QtGui.QIcon.Mode.Normal,
                QtGui.QIcon.State.Off,
            )
        else:
            icon3.addPixmap(
                QtGui.QPixmap("res/icons/dark/executedark.svg"),
                QtGui.QIcon.Mode.Normal,
                QtGui.QIcon.State.Off,
            )

        self.setIcon(icon3)
        self.setIconSize(QtCore.QSize(48, 48))
        self.setMouseTracking(True)
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

    def execute(self, jarvisButton):
        self.recorder = AudioRecorder()
        self.recorder.stop_recording(self, jarvisButton)