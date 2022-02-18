from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import webbrowser
import json
import os
import warnings

warnings.filterwarnings("ignore")

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(718, 440)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui_images/Icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(-130, -110, 971, 621))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("ui_images/logo.png"))
        self.logo.setObjectName("logo")
        self.BackGround = QtWidgets.QLabel(self.centralwidget)
        self.BackGround.setGeometry(QtCore.QRect(360, 0, 371, 441))
        self.BackGround.setStyleSheet("background-color: rgb(255, 230, 38);")
        self.BackGround.setText("")
        self.BackGround.setPixmap(QtGui.QPixmap("ui_images/background.jpg"))
        self.BackGround.setObjectName("BackGround")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(410, 200, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.StartButton.setFont(font)
        self.StartButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartButton.setStyleSheet("QPushButton {\n"
                                       "    color: #333;\n"
                                       "   font: 30pt \"Agency FB\";\n"
                                       "background-color: rgb(255, 252, 205);\n"
                                       "    border: 6px solid;\n"
                                       "border-color: rgb(5, 99, 80);\n"
                                       "    border-radius: 0px;\n"
                                       "    border-style: outset;\n"
                                       "\n"
                                       "    }\n"
                                       "\n"
                                       "QPushButton:hover {    \n"
                                       "    background-color: rgb(221, 222, 169);\n"
                                       "    }\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    border-style: inset;\n"
                                       "    background: qradialgradient(\n"
                                       "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                       "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                       "        );\n"
                                       "    }")
        self.StartButton.setObjectName("StartButton")
        self.ChooseDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChooseDataButton.setGeometry(QtCore.QRect(410, 20, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ChooseDataButton.setFont(font)
        self.ChooseDataButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ChooseDataButton.setStyleSheet("QPushButton {\n"
                                            "    color: #333;\n"
                                            "   \n"
                                            "    font: 16pt \"Agency FB\";\n"
                                            "background-color: rgb(255, 252, 205);\n"
                                            "    border: 6px solid;\n"
                                            "border-color: rgb(5, 99, 80);\n"
                                            "    border-radius: 0px;\n"
                                            "    border-style: outset;\n"
                                            "\n"
                                            "    }\n"
                                            "\n"
                                            "QPushButton:hover {    \n"
                                            "    background-color: rgb(221, 222, 169);\n"
                                            "    }\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "    border-style: inset;\n"
                                            "    background: qradialgradient(\n"
                                            "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                            "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                            "        );\n"
                                            "    }")
        self.ChooseDataButton.setObjectName("ChooseDataButton")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(410, 110, 261, 61))
        self.SaveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SaveButton.setStyleSheet("QPushButton {\n"
                                      "    color: #333;\n"
                                      "      font: 16pt \"Agency FB\";\n"
                                      "background-color: rgb(255, 252, 205);\n"
                                      "    border: 6px solid;\n"
                                      "border-color: rgb(5, 99, 80);\n"
                                      "    border-radius: 0px;\n"
                                      "    border-style: outset;\n"
                                      "\n"
                                      "    }\n"
                                      "\n"
                                      "QPushButton:hover {    \n"
                                      "    background-color: rgb(221, 222, 169);\n"
                                      "    }\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    border-style: inset;\n"
                                      "    background: qradialgradient(\n"
                                      "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                      "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                      "        );\n"
                                      "    }")
        self.SaveButton.setObjectName("SaveButton")
        self.ChooseFormat = QtWidgets.QComboBox(self.centralwidget)
        self.ChooseFormat.setGeometry(QtCore.QRect(590, 200, 81, 31))
        self.ChooseFormat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ChooseFormat.setStyleSheet("color: #333;\n"
                                        "   font: 16pt \"Agency FB\";\n"
                                        "background-color: rgb(255, 252, 205);\n"
                                        "    border: 6px solid;\n"
                                        "border-color: rgb(5, 99, 80);\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "")
        self.ChooseFormat.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.ChooseFormat.setObjectName("ChooseFormat")
        self.ChooseFormat.addItem("")
        self.ChooseFormat.addItem("")
        self.Results = QtWidgets.QLabel(self.centralwidget)
        self.Results.setGeometry(QtCore.QRect(410, 290, 261, 131))
        self.Results.setStyleSheet(" color: #333;\n"
                                   "   font: 30pt \"Agency FB\";\n"
                                   "background-color: rgb(255, 252, 205);\n"
                                   "    border: 6px solid;\n"
                                   "border-color: rgb(5, 99, 80);\n"
                                   "    border-radius: 0px;\n"
                                   "    border-style: outset;\n"
                                   "")
        self.Results.setAlignment(QtCore.Qt.AlignCenter)
        self.Results.setObjectName("Results")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wheat Detector"))
        self.StartButton.setText(_translate("MainWindow", "START"))
        self.ChooseDataButton.setText(_translate("MainWindow", "CHOOSE FOLDER WITH DATA"))
        self.SaveButton.setText(_translate("MainWindow", "CHOOSE FOLDER TO SAVE PHOTOS"))
        self.ChooseFormat.setItemText(0, _translate("MainWindow", "  PNG"))
        self.ChooseFormat.setItemText(1, _translate("MainWindow", "  JPG"))
        self.Results.setText(_translate("MainWindow", "RESULTS"))


class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)

        self.setupUi(self)
        self.dir_data = 'data_example'
        self.dir_detected = 'detected_images'

        self.ChooseDataButton.clicked.connect(self.get_dir_from)
        self.SaveButton.clicked.connect(self.get_dir_to)

        self.StartButton.clicked.connect(self.make_predictions)

    def get_dir_from(self):
        self.dir_data = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

    def get_dir_to(self):
        self.dir_detected = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

    def get_field_coords(self):
        webbrowser.open(r"txt_files\field_coords.txt")

    def get_photos_coords(self):
        webbrowser.open(r"txt_files\photos_coords.txt")

    def make_predictions(self):
        self.Results.setStyleSheet(" color: #333;\n"
                                   "   font: 23pt \"Agency FB\";\n"
                                   "background-color: rgb(255, 252, 205);\n"
                                   "    border: 6px solid;\n"
                                   "border-color: rgb(5, 99, 80);\n"
                                   "    border-radius: 0px;\n"
                                   "    border-style: outset;\n"
                                   "")
        self.Results.setText('Predicting...\n(this may take some time)')
        QtGui.QGuiApplication.processEvents()

        img_format = str(self.ChooseFormat.currentText()).strip().lower()

        try:

            with open(f'{self.dir_data}\info.json', 'r') as file:
                data = json.load(file)


            corners = data['mapContour']
            photos = []
            for img in data:
                photos.append([data[img][0], data[img][1]])
                if img != 'mapContour':
                    os.rename(f'{self.dir_data}/{img}', f'{self.dir_data}/{img.split(".")[0]}_{data[img][2]}.{img_format}')
            photos = photos[1:]
            os.remove(f'{self.dir_data}/info.json')

            area = calculate_field_area(corners)

            field_lst = make_predictions(img_format, self.dir_data, self.dir_detected)

            total_wheat, total_density = make_calculations(field_lst, area)

            with open(f'{self.dir_data}/info.json', 'w') as file:
                json.dump(data, file)

            for img in data:
                if img != 'mapContour':
                    os.rename(f'{self.dir_data}/{img.split(".")[0]}_{data[img][2]}.{img_format}', f'{self.dir_data}/{img}')

            self.Results.setText(f'field area = {area}\n'
                                 f'wheat on field = {int(total_wheat)}\n'
                                 f'wheat per meter = {round(total_density, 2)}')
            self.Results.setStyleSheet(" color: #333;\n"
                                       "   font: 19pt \"Agency FB\";\n"
                                       "background-color: rgb(255, 252, 205);\n"
                                       "    border: 6px solid;\n"
                                       "border-color: rgb(5, 99, 80);\n"
                                       "    border-radius: 0px;\n"
                                       "    border-style: outset;\n"
                                       "")

            create_points_plot(corners, photos, field_lst)
        except:
            self.Results.setText('ERROR\n'
                                 'please check the input data\n'
                                 'or instruction')
            self.Results.setStyleSheet(" color: #333;\n"
                                       "   font: 19pt \"Agency FB\";\n"
                                       "background-color: rgb(255, 252, 205);\n"
                                       "    border: 6px solid;\n"
                                       "border-color: rgb(5, 99, 80);\n"
                                       "    border-radius: 0px;\n"
                                       "    border-style: outset;\n"
                                       "")


if __name__ == "__main__":
    webbrowser.open(r"INSTRUCTION_ИНСТРУКЦИЯ.txt")

    import sys
    from scripts_and_functions.model import *
    from scripts_and_functions.field import *

    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = '2'
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_DisableHighDpiScaling)
    app.setAttribute(QtCore.Qt.AA_Use96Dpi)
    nextGui = mainProgram()
    nextGui.show()
    sys.exit(app.exec_())
