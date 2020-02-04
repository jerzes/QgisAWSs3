# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(544, 379)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(180, 330, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 511, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.Layers = QtWidgets.QWidget()
        self.Layers.setEnabled(True)
        self.Layers.setObjectName("Layers")
        self.bucket = QtWidgets.QComboBox(self.Layers)
        self.bucket.setGeometry(QtCore.QRect(260, 30, 201, 25))
        self.bucket.setObjectName("bucket")
        self.comboBox = QtWidgets.QComboBox(self.Layers)
        self.comboBox.setGeometry(QtCore.QRect(260, 80, 201, 25))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(self.Layers)
        self.label_4.setGeometry(QtCore.QRect(180, 30, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Layers)
        self.label_5.setGeometry(QtCore.QRect(180, 80, 67, 17))
        self.label_5.setObjectName("label_5")
        self.load = QtWidgets.QPushButton(self.Layers)
        self.load.setGeometry(QtCore.QRect(20, 210, 89, 25))
        self.load.setObjectName("load")
        self.pushButton_2 = QtWidgets.QPushButton(self.Layers)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 210, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.Layers, "")
        self.configuration = QtWidgets.QWidget()
        self.configuration.setObjectName("configuration")
        self.access_key = QtWidgets.QLineEdit(self.configuration)
        self.access_key.setGeometry(QtCore.QRect(140, 30, 201, 25))
        self.access_key.setObjectName("access_key")
        self.secret_key = QtWidgets.QLineEdit(self.configuration)
        self.secret_key.setGeometry(QtCore.QRect(140, 80, 201, 25))
        self.secret_key.setEchoMode(QtWidgets.QLineEdit.Password)
        self.secret_key.setObjectName("secret_key")
        self.region = QtWidgets.QComboBox(self.configuration)
        self.region.setGeometry(QtCore.QRect(140, 130, 201, 25))
        self.region.setObjectName("region")
        self.pushButton = QtWidgets.QPushButton(self.configuration)
        self.pushButton.setGeometry(QtCore.QRect(360, 180, 121, 25))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.configuration)
        self.label.setGeometry(QtCore.QRect(40, 30, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.configuration)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 91, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.configuration)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 67, 17))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.configuration, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Bucket"))
        self.label_5.setText(_translate("Dialog", "Layer"))
        self.load.setText(_translate("Dialog", "Load"))
        self.pushButton_2.setText(_translate("Dialog", "Save layer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Layers), _translate("Dialog", "Layers"))
        self.pushButton.setText(_translate("Dialog", "test connection"))
        self.label.setText(_translate("Dialog", "Access key"))
        self.label_2.setText(_translate("Dialog", "Secret key"))
        self.label_3.setText(_translate("Dialog", "Region"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.configuration), _translate("Dialog", "configuration"))

import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
