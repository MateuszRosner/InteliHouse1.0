# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InteliHouse.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1026, 520)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1021, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tabEnergy = QtWidgets.QWidget()
        self.tabEnergy.setObjectName("tabEnergy")
        self.progressBar5 = QtWidgets.QProgressBar(self.tabEnergy)
        self.progressBar5.setGeometry(QtCore.QRect(210, 220, 181, 16))
        self.progressBar5.setProperty("value", 0)
        self.progressBar5.setObjectName("progressBar5")
        self.progressBar9 = QtWidgets.QProgressBar(self.tabEnergy)
        self.progressBar9.setGeometry(QtCore.QRect(210, 380, 181, 16))
        self.progressBar9.setProperty("value", 0)
        self.progressBar9.setObjectName("progressBar9")
        self.progressBar8 = QtWidgets.QProgressBar(self.tabEnergy)
        self.progressBar8.setGeometry(QtCore.QRect(210, 340, 181, 16))
        self.progressBar8.setProperty("value", 0)
        self.progressBar8.setObjectName("progressBar8")
        self.checkBox10 = QtWidgets.QCheckBox(self.tabEnergy)
        self.checkBox10.setGeometry(QtCore.QRect(30, 420, 70, 17))
        self.checkBox10.setObjectName("checkBox10")
        self.checkBox9 = QtWidgets.QCheckBox(self.tabEnergy)
        self.checkBox9.setGeometry(QtCore.QRect(30, 380, 70, 17))
        self.checkBox9.setObjectName("checkBox9")
        self.progressBar4 = QtWidgets.QProgressBar(self.tabEnergy)
        self.progressBar4.setGeometry(QtCore.QRect(210, 180, 181, 16))
        self.progressBar4.setProperty("value", 0)
        self.progressBar4.setObjectName("progressBar4")
        self.progressBar10 = QtWidgets.QProgressBar(self.tabEnergy)
        self.progressBar10.setGeometry(QtCore.QRect(210, 420, 181, 16))
        self.progressBar10.setProperty("value", 0)
        self.progressBar10.setObjectName("progressBar10")
        self.checkBox1 = QtWidgets.QCheckBox(self.tabEnergy)
        self.checkBox1.setGeometry(QtCore.QRect(30, 60, 70, 17))
        self.checkBox1.setObjectName("checkBox1")
        self.progressBar1 = QtWidgets.QProgressBar(self.tabEnergy)
        self.progressBar1.setGeometry(QtCore.QRect(210, 60, 181, 16))
        self.progressBar1.setProperty("value", 0)
        self.progressBar1.setObjectName("progressBar1")
        self.checkBox8 = QtWidgets.QCheckBox(self.tabEnergy)
        self.checkBox8.setGeometry(QtCore.QRect(30, 340, 70, 17))
        self.checkBox8.setObjectName("checkBox8")
        self.checkBox7 = QtWidgets.QCheckBox(self.tabEnergy)
        self.checkBox7.setGeometry(QtCore.QRect(30, 300, 70, 17))
        self.checkBox7.setObjectName("checkBox7")
        self.checkBox4 = QtWidgets.QCheckBox(self.tabEnergy)
        self.checkBox4.setGeometry(QtCore.QRect(30, 180, 70, 17))
        self.checkBox4.setObjectName("checkBox4")
        self.progressBar2 = QtWidgets.QProgressBar(self.tabEnergy)
        self.progressBar2.setGeometry(QtCore.QRect(210, 100, 181, 16))
        self.progressBar2.setProperty("value", 0)
        self.progressBar2.setObjectName("progressBar2")
        self.checkBox2 = QtWidgets.QCheckBox(self.tabEnergy)
        self.checkBox2.setGeometry(QtCore.QRect(30, 100, 70, 17))
        self.checkBox2.setObjectName("checkBox2")
        self.checkBox6 = QtWidgets.QCheckBox(self.tabEnergy)
        self.checkBox6.setGeometry(QtCore.QRect(30, 260, 70, 17))
        self.checkBox6.setObjectName("checkBox6")
        self.label = QtWidgets.QLabel(self.tabEnergy)
        self.label.setGeometry(QtCore.QRect(30, 30, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.checkBox3 = QtWidgets.QCheckBox(self.tabEnergy)
        self.checkBox3.setGeometry(QtCore.QRect(30, 140, 70, 17))
        self.checkBox3.setObjectName("checkBox3")
        self.progressBar6 = QtWidgets.QProgressBar(self.tabEnergy)
        self.progressBar6.setGeometry(QtCore.QRect(210, 260, 181, 16))
        self.progressBar6.setProperty("value", 0)
        self.progressBar6.setObjectName("progressBar6")
        self.progressBar7 = QtWidgets.QProgressBar(self.tabEnergy)
        self.progressBar7.setGeometry(QtCore.QRect(210, 300, 181, 16))
        self.progressBar7.setProperty("value", 0)
        self.progressBar7.setObjectName("progressBar7")
        self.checkBox5 = QtWidgets.QCheckBox(self.tabEnergy)
        self.checkBox5.setGeometry(QtCore.QRect(30, 220, 70, 17))
        self.checkBox5.setObjectName("checkBox5")
        self.progressBar3 = QtWidgets.QProgressBar(self.tabEnergy)
        self.progressBar3.setGeometry(QtCore.QRect(210, 140, 181, 16))
        self.progressBar3.setProperty("value", 0)
        self.progressBar3.setObjectName("progressBar3")
        self.label_2 = QtWidgets.QLabel(self.tabEnergy)
        self.label_2.setGeometry(QtCore.QRect(530, 390, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.progressBarTotalCurr = QtWidgets.QProgressBar(self.tabEnergy)
        self.progressBarTotalCurr.setGeometry(QtCore.QRect(530, 420, 271, 16))
        self.progressBarTotalCurr.setProperty("value", 0)
        self.progressBarTotalCurr.setObjectName("progressBarTotalCurr")
        self.label_9 = QtWidgets.QLabel(self.tabEnergy)
        self.label_9.setGeometry(QtCore.QRect(130, 30, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.spinBox = QtWidgets.QSpinBox(self.tabEnergy)
        self.spinBox.setGeometry(QtCore.QRect(130, 60, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(5)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tabEnergy)
        self.spinBox_2.setGeometry(QtCore.QRect(130, 100, 42, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(5)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.tabEnergy)
        self.spinBox_3.setGeometry(QtCore.QRect(130, 140, 42, 22))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(5)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.tabEnergy)
        self.spinBox_4.setGeometry(QtCore.QRect(130, 180, 42, 22))
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(5)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(self.tabEnergy)
        self.spinBox_5.setGeometry(QtCore.QRect(130, 220, 42, 22))
        self.spinBox_5.setMinimum(1)
        self.spinBox_5.setMaximum(5)
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_6 = QtWidgets.QSpinBox(self.tabEnergy)
        self.spinBox_6.setGeometry(QtCore.QRect(130, 260, 42, 22))
        self.spinBox_6.setMinimum(1)
        self.spinBox_6.setMaximum(5)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(self.tabEnergy)
        self.spinBox_7.setGeometry(QtCore.QRect(130, 300, 42, 22))
        self.spinBox_7.setMinimum(1)
        self.spinBox_7.setMaximum(5)
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox_8 = QtWidgets.QSpinBox(self.tabEnergy)
        self.spinBox_8.setGeometry(QtCore.QRect(130, 340, 42, 22))
        self.spinBox_8.setMinimum(1)
        self.spinBox_8.setMaximum(5)
        self.spinBox_8.setObjectName("spinBox_8")
        self.spinBox_9 = QtWidgets.QSpinBox(self.tabEnergy)
        self.spinBox_9.setGeometry(QtCore.QRect(130, 380, 42, 22))
        self.spinBox_9.setMinimum(1)
        self.spinBox_9.setMaximum(5)
        self.spinBox_9.setObjectName("spinBox_9")
        self.spinBox_10 = QtWidgets.QSpinBox(self.tabEnergy)
        self.spinBox_10.setGeometry(QtCore.QRect(130, 420, 42, 22))
        self.spinBox_10.setMinimum(1)
        self.spinBox_10.setMaximum(5)
        self.spinBox_10.setObjectName("spinBox_10")
        self.label_10 = QtWidgets.QLabel(self.tabEnergy)
        self.label_10.setGeometry(QtCore.QRect(820, 390, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tabEnergy)
        self.label_11.setGeometry(QtCore.QRect(820, 420, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.dateEdit = QtWidgets.QDateEdit(self.tabEnergy)
        self.dateEdit.setGeometry(QtCore.QRect(620, 20, 110, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 6, 18), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.tabEnergy)
        self.dateEdit_2.setGeometry(QtCore.QRect(770, 20, 110, 22))
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 6, 22), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_19 = QtWidgets.QLabel(self.tabEnergy)
        self.label_19.setGeometry(QtCore.QRect(640, 0, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tabEnergy)
        self.label_20.setGeometry(QtCore.QRect(800, 0, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.GraphPower = CustomWidget(self.tabEnergy)
        self.GraphPower.setGeometry(QtCore.QRect(510, 60, 491, 321))
        self.GraphPower.setObjectName("GraphPower")
        self.tabWidget.addTab(self.tabEnergy, "")
        self.tabZasoby = QtWidgets.QWidget()
        self.tabZasoby.setObjectName("tabZasoby")
        self.label_3 = QtWidgets.QLabel(self.tabZasoby)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.progressBarWB = QtWidgets.QProgressBar(self.tabZasoby)
        self.progressBarWB.setGeometry(QtCore.QRect(130, 80, 181, 16))
        self.progressBarWB.setProperty("value", 0)
        self.progressBarWB.setObjectName("progressBarWB")
        self.label_6 = QtWidgets.QLabel(self.tabZasoby)
        self.label_6.setGeometry(QtCore.QRect(40, 110, 61, 16))
        self.label_6.setObjectName("label_6")
        self.progressBarFU_2 = QtWidgets.QProgressBar(self.tabZasoby)
        self.progressBarFU_2.setGeometry(QtCore.QRect(130, 170, 181, 16))
        self.progressBarFU_2.setProperty("value", 0)
        self.progressBarFU_2.setObjectName("progressBarFU_2")
        self.label_5 = QtWidgets.QLabel(self.tabZasoby)
        self.label_5.setGeometry(QtCore.QRect(40, 80, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.tabZasoby)
        self.label_7.setGeometry(QtCore.QRect(40, 140, 61, 16))
        self.label_7.setObjectName("label_7")
        self.progressBarFU = QtWidgets.QProgressBar(self.tabZasoby)
        self.progressBarFU.setGeometry(QtCore.QRect(130, 140, 181, 16))
        self.progressBarFU.setProperty("value", 0)
        self.progressBarFU.setObjectName("progressBarFU")
        self.label_8 = QtWidgets.QLabel(self.tabZasoby)
        self.label_8.setGeometry(QtCore.QRect(40, 170, 61, 16))
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.tabZasoby)
        self.label_4.setGeometry(QtCore.QRect(40, 50, 61, 16))
        self.label_4.setObjectName("label_4")
        self.progressBarSZ = QtWidgets.QProgressBar(self.tabZasoby)
        self.progressBarSZ.setGeometry(QtCore.QRect(130, 110, 181, 16))
        self.progressBarSZ.setProperty("value", 0)
        self.progressBarSZ.setObjectName("progressBarSZ")
        self.progressBarWP = QtWidgets.QProgressBar(self.tabZasoby)
        self.progressBarWP.setGeometry(QtCore.QRect(130, 50, 181, 16))
        self.progressBarWP.setProperty("value", 0)
        self.progressBarWP.setObjectName("progressBarWP")
        self.label_12 = QtWidgets.QLabel(self.tabZasoby)
        self.label_12.setGeometry(QtCore.QRect(40, 230, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tabZasoby)
        self.label_13.setGeometry(QtCore.QRect(40, 260, 61, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tabZasoby)
        self.label_14.setGeometry(QtCore.QRect(40, 290, 61, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tabZasoby)
        self.label_15.setGeometry(QtCore.QRect(40, 320, 61, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tabZasoby)
        self.label_16.setGeometry(QtCore.QRect(120, 260, 61, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tabZasoby)
        self.label_17.setGeometry(QtCore.QRect(120, 290, 61, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tabZasoby)
        self.label_18.setGeometry(QtCore.QRect(120, 320, 61, 16))
        self.label_18.setObjectName("label_18")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.tabZasoby)
        self.doubleSpinBox.setGeometry(QtCore.QRect(190, 260, 62, 22))
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMinimum(18.0)
        self.doubleSpinBox.setMaximum(25.0)
        self.doubleSpinBox.setSingleStep(0.5)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.tabZasoby)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(190, 290, 62, 22))
        self.doubleSpinBox_2.setDecimals(1)
        self.doubleSpinBox_2.setMinimum(18.0)
        self.doubleSpinBox_2.setMaximum(25.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.tabZasoby)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(190, 320, 62, 22))
        self.doubleSpinBox_3.setDecimals(1)
        self.doubleSpinBox_3.setMinimum(18.0)
        self.doubleSpinBox_3.setMaximum(25.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.tabZasoby)
        self.dateEdit_3.setGeometry(QtCore.QRect(580, 20, 110, 22))
        self.dateEdit_3.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 6, 18), QtCore.QTime(0, 0, 0)))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.label_21 = QtWidgets.QLabel(self.tabZasoby)
        self.label_21.setGeometry(QtCore.QRect(600, 0, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.dateEdit_4 = QtWidgets.QDateEdit(self.tabZasoby)
        self.dateEdit_4.setGeometry(QtCore.QRect(730, 20, 110, 22))
        self.dateEdit_4.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 6, 22), QtCore.QTime(0, 0, 0)))
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.label_22 = QtWidgets.QLabel(self.tabZasoby)
        self.label_22.setGeometry(QtCore.QRect(760, 0, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.GraphResources = CustomWidget(self.tabZasoby)
        self.GraphResources.setGeometry(QtCore.QRect(510, 60, 491, 321))
        self.GraphResources.setObjectName("GraphResources")
        self.tabWidget.addTab(self.tabZasoby, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1026, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DNW Panel"))
        self.checkBox10.setText(_translate("MainWindow", "wyjście 10"))
        self.checkBox9.setText(_translate("MainWindow", "wyjście 9"))
        self.checkBox1.setText(_translate("MainWindow", "wyjście 1"))
        self.checkBox8.setText(_translate("MainWindow", "wyjście 8"))
        self.checkBox7.setText(_translate("MainWindow", "wyjście 7"))
        self.checkBox4.setText(_translate("MainWindow", "wyjście 4"))
        self.checkBox2.setText(_translate("MainWindow", "wyjście 2"))
        self.checkBox6.setText(_translate("MainWindow", "wyjście 6"))
        self.label.setText(_translate("MainWindow", "Wyjścia"))
        self.checkBox3.setText(_translate("MainWindow", "wyjście 3"))
        self.checkBox5.setText(_translate("MainWindow", "wyjście 5"))
        self.label_2.setText(_translate("MainWindow", "Pobór energii"))
        self.label_9.setText(_translate("MainWindow", "Priorytet"))
        self.label_10.setText(_translate("MainWindow", "Zużycie całkowite"))
        self.label_11.setText(_translate("MainWindow", "3,42 kWh"))
        self.label_19.setText(_translate("MainWindow", "początek"))
        self.label_20.setText(_translate("MainWindow", "koniec"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEnergy), _translate("MainWindow", "Energia"))
        self.label_3.setText(_translate("MainWindow", "Płyny"))
        self.label_6.setText(_translate("MainWindow", "szambo"))
        self.label_5.setText(_translate("MainWindow", "woda brudna"))
        self.label_7.setText(_translate("MainWindow", "paliwo"))
        self.label_8.setText(_translate("MainWindow", "paliwo2"))
        self.label_4.setText(_translate("MainWindow", "woda pitna"))
        self.label_12.setText(_translate("MainWindow", "Temperatura"))
        self.label_13.setText(_translate("MainWindow", "salon"))
        self.label_14.setText(_translate("MainWindow", "kuchnia"))
        self.label_15.setText(_translate("MainWindow", "pokład"))
        self.label_16.setText(_translate("MainWindow", "25,5 *C"))
        self.label_17.setText(_translate("MainWindow", "23,5 *C"))
        self.label_18.setText(_translate("MainWindow", "21,0 *C"))
        self.label_21.setText(_translate("MainWindow", "początek"))
        self.label_22.setText(_translate("MainWindow", "koniec"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabZasoby), _translate("MainWindow", "Zasoby"))
from plotter import CustomWidget
