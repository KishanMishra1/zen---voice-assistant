# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ZEN_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ZEN(object):
    def setupUi(self, ZEN):
        ZEN.setObjectName("ZEN")
        ZEN.resize(978, 600)
        self.centralwidget = QtWidgets.QWidget(ZEN)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2= QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 981, 601))
        self.label_2.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: rgb(255, 255, 0);\n"
"color: rgb(255, 0, 0);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../SciFi_LoaderBlue.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(670, 460, 301, 131))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../initiating.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 281, 281))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../1a7d825b332de7940e2a13e87cdd89c9.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(760, 210, 201, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../Credits.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(550, 20, 256, 61))
        self.textBrowser.setStyleSheet("background: transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(730, 20, 256, 61))
        self.textBrowser_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_2.setStyleSheet("background: transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(870, 340, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(840, 380, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 85, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        ZEN.setCentralWidget(self.centralwidget)

        self.retranslateUi(ZEN)
        QtCore.QMetaObject.connectSlotsByName(ZEN)

    def retranslateUi(self, ZEN):
        _translate = QtCore.QCoreApplication.translate
        ZEN.setWindowTitle(_translate("ZEN", "MainWindow"))
        self.pushButton.setText(_translate("ZEN", "RUN"))
        self.pushButton_2.setText(_translate("ZEN", "TERMINATE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ZEN = QtWidgets.QMainWindow()
    ui = Ui_ZEN()
    ui.setupUi(ZEN)
    ZEN.show()
    sys.exit(app.exec_())

