from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt
from gui.start_jarvis import *
from gui.theme_library import *
from gui.settings import *
from gui.history import *
from gui.execute import *
import json


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.displaytext = "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe."
        self.setting_manager = SettingsManager()
        self.settings = self.setting_manager.load_settings()
        self.make_ui(self.settings["theme_mode"])

    def make_ui(self, thememode):
        self.setObjectName("MainWindow")
        self.resize(640, 480)

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("res/images/jarvis.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.setWindowIcon(icon)

        if thememode == "light":
            self.setStyleSheet(
                """
                *{
                    border:none;
                    background-color: #FFFFFF;
                }
                """
            )
        else:
            self.setStyleSheet(
                """
                *{
                    border:none;
                    background-color: #202124;
                }
                """
            )

        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")

        self.mainframeLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainframeLayout.setContentsMargins(0, 0, 0, 0)
        self.mainframeLayout.setSpacing(0)
        self.mainframeLayout.setObjectName("mainframeLayout")

        self.header = QtWidgets.QWidget(parent=self.centralwidget)
        self.header.setMaximumSize(QtCore.QSize(16777215, 70))
        self.header.setObjectName("header")

        self.body = QtWidgets.QWidget(parent=self.centralwidget)
        self.body.setObjectName("body")

        self.mainframeLayout.addWidget(self.header)
        self.mainframeLayout.addWidget(self.body)

        self.topbarLayout = QtWidgets.QHBoxLayout(self.header)
        self.topbarLayout.setContentsMargins(0, 0, 0, 0)
        self.topbarLayout.setSpacing(0)
        self.topbarLayout.setObjectName("topbarLayout")

        self.topbar_space = QtWidgets.QWidget(parent=self.header)
        self.topbar_space.setObjectName("topbar_space")

        self.button_holder = QtWidgets.QWidget(parent=self.header)
        self.button_holder.setMaximumSize(QtCore.QSize(250, 16777215))
        self.button_holder.setObjectName("button_holder")

        self.topbarLayout.addWidget(self.topbar_space)
        self.topbarLayout.addWidget(self.button_holder)

        self.buttonLayout = QtWidgets.QHBoxLayout(self.button_holder)
        self.buttonLayout.setObjectName("buttonLayout")

        self.body_layout = QtWidgets.QVBoxLayout(self.body)
        self.body_layout.setObjectName("body_layout")

        self.label_holder = QtWidgets.QWidget(parent=self.body)
        self.label_holder.setObjectName("label_holder")

        self.startButton_holder = QtWidgets.QWidget(parent=self.body)
        self.startButton_holder.setObjectName("startButton_holder")

        self.controlButton_holder = QtWidgets.QWidget(parent=self.body)
        self.controlButton_holder.setObjectName("controlButton_holder")

        self.body_layout.addWidget(self.label_holder)
        self.body_layout.addWidget(self.startButton_holder, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.body_layout.addWidget(self.controlButton_holder)

        self.labelHolder_layout = QtWidgets.QVBoxLayout(self.label_holder)
        self.labelHolder_layout.setContentsMargins(-1, 0, -1, 0)
        self.labelHolder_layout.setObjectName("labelHolder_layout")

        self.startButton_layout = QtWidgets.QGridLayout(self.startButton_holder)
        self.startButton_layout.setObjectName("startButton_layout")

        self.controlButton_layout = QtWidgets.QHBoxLayout(self.controlButton_holder)
        self.controlButton_layout.setObjectName("controlButton_layout")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        # Label
        self.set_label(thememode, self.displaytext)

        # History button
        self.historyButton = HistoryButton(parent=self.button_holder)
        self.historyButton.setObjectName("historyButton")
        self.historyButton.make_ui(thememode)
        self.buttonLayout.addWidget(self.historyButton)
        sizePolicy.setHeightForWidth(self.historyButton.sizePolicy().hasHeightForWidth())
        self.historyButton.setSizePolicy(sizePolicy)

        # Thememode button
        self.themeButton = ThemeModeButton(parent=self.button_holder)
        self.themeButton.setObjectName("themeButton")
        self.themeButton.make_ui(thememode)
        self.buttonLayout.addWidget(self.themeButton)
        sizePolicy.setHeightForWidth(self.themeButton.sizePolicy().hasHeightForWidth())
        self.themeButton.setSizePolicy(sizePolicy)
        self.themeButton.clicked.connect(self.reload_window)

        # Settings button
        self.settingsButton = SettingsButton(parent=self.button_holder)
        self.settingsButton.setObjectName("settingsButton")
        self.settingsButton.make_ui(thememode)
        self.buttonLayout.addWidget(self.settingsButton)
        sizePolicy.setHeightForWidth(self.settingsButton.sizePolicy().hasHeightForWidth())
        self.settingsButton.setSizePolicy(sizePolicy)
        
        # Execute button
        self.executeButton = ExecuteButton(parent=self.controlButton_holder)
        self.executeButton.setObjectName("executeButton")
        self.executeButton.make_ui(thememode)
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.controlButton_layout.addItem(spacerItem)
        self.controlButton_layout.addWidget(self.executeButton)
        sizePolicy.setHeightForWidth(self.executeButton.sizePolicy().hasHeightForWidth())
        self.executeButton.setSizePolicy(sizePolicy)
        self.executeButton.clicked.connect(lambda: self.executeButton.execute(self.startButton))

        # Button to start Jarvis
        self.startButton = JarvisButton(parent=self.startButton_holder)
        self.startButton.setObjectName("startButton")
        self.startButton.make_ui(thememode)
        self.startButton_layout.addWidget(self.startButton, 0, 0, 1, 1)
        self.startButton.clicked.connect(lambda: self.startButton.start_jarvis(self.executeButton))

        self.setCentralWidget(self.centralwidget)

        self.retranslate_ui()

    def set_label(self, thememode, text: str):
        font_id = QFontDatabase.addApplicationFont("res/fonts/josefin.ttf")
        if font_id == -1:
            print("Font loading failed!")
        font_family = QFontDatabase.applicationFontFamilies(font_id)

        font = QFont("Segoe UI", 12)
        font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
        font.setWeight(550)

        self.label = QtWidgets.QLabel(parent=self.label_holder)
        self.label.setWordWrap(True)
        self.label.setFont(font)
        self.label.setText(f"{text}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        if thememode == "light":
            self.label.setStyleSheet("color: #444444")
        else:
            self.label.setStyleSheet("color: #d9d9d9")

        self.labelHolder_layout.addWidget(self.label)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "jarvis"))


    def reload_window(self):
        self.theme = Theme()
        self.settings["theme_mode"] = self.theme.change_theme()
        self.make_ui(self.settings["theme_mode"])