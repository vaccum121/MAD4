# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(463, 299)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 51, 199, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.function_type = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.function_type.setObjectName("function_type")
        self.function_type.addItem("")
        self.function_type.addItem("")
        self.function_type.addItem("")
        self.verticalLayout.addWidget(self.function_type)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 120, 160, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.hid_disp = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.hid_disp.setObjectName("hid_disp")
        self.horizontalLayout.addWidget(self.hid_disp)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 160, 160, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.iter_count = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.iter_count.setMaximum(200)
        self.iter_count.setProperty("value", 50)
        self.iter_count.setObjectName("iter_count")
        self.horizontalLayout_2.addWidget(self.iter_count)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(180, 160, 160, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.interval_len = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.interval_len.setMaximum(500)
        self.interval_len.setProperty("value", 80)
        self.interval_len.setObjectName("interval_len")
        self.horizontalLayout_3.addWidget(self.interval_len)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(230, 60, 160, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.calc_btn = QtWidgets.QPushButton(Form)
        self.calc_btn.setGeometry(QtCore.QRect(290, 220, 161, 51))
        self.calc_btn.setObjectName("calc_btn")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 10, 371, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.object_function = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.object_function.setObjectName("object_function")
        self.horizontalLayout_4.addWidget(self.object_function)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "n(u,a)"))
        self.function_type.setItemText(0, _translate("Form", "a1+a2*(u-u_)"))
        self.function_type.setItemText(1, _translate("Form", "a1+a2*u1+a2*u2"))
        self.function_type.setItemText(2, _translate("Form", "nu+a1(u1-u1_)+a2(u2-u2_)"))
        self.label_2.setText(_translate("Form", "Dпом."))
        self.hid_disp.setText(_translate("Form", "5"))
        self.label_3.setText(_translate("Form", "Iter"))
        self.label_4.setText(_translate("Form", "Interval"))
        self.pushButton.setText(_translate("Form", "Graph1"))
        self.pushButton_2.setText(_translate("Form", "Graph"))
        self.calc_btn.setText(_translate("Form", "calc"))
        self.label_5.setText(_translate("Form", "Function"))
