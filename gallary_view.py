# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\doron\Documents\py projects\Image_editor\gallary view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_gallery(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1348, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Image1 = QtWidgets.QLabel(self.centralwidget)
        self.Image1.setGeometry(QtCore.QRect(10, 130, 300, 300))
        self.Image1.setObjectName("Image1")
        self.Image2 = QtWidgets.QLabel(self.centralwidget)
        self.Image2.setGeometry(QtCore.QRect(650, 130, 300, 300))
        self.Image2.setObjectName("Image2")
        self.Image3 = QtWidgets.QLabel(self.centralwidget)
        self.Image3.setGeometry(QtCore.QRect(330, 130, 300, 300))
        self.Image3.setObjectName("Image3")
        self.Image4 = QtWidgets.QLabel(self.centralwidget)
        self.Image4.setGeometry(QtCore.QRect(970, 130, 300, 300))
        self.Image4.setObjectName("Image4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(390, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(690, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1000, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1348, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Gallary view class:"))
        self.Image1.setText(_translate("MainWindow", "TextLabel"))
        self.Image2.setText(_translate("MainWindow", "TextLabel"))
        self.Image3.setText(_translate("MainWindow", "TextLabel"))
        self.Image4.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Defect 1"))
        self.label_7.setText(_translate("MainWindow", "Defect 2"))
        self.label_8.setText(_translate("MainWindow", "Defect 3"))
        self.label_9.setText(_translate("MainWindow", "Defect 4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_gallery()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())