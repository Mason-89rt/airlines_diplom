# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ticket_passenger.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UiTicketPassenger(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(618, 300)
        Form.setMaximumSize(QtCore.QSize(16777215, 300))
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setContentsMargins(-1, 9, 9, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.buy_ticket_6 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buy_ticket_6.sizePolicy().hasHeightForWidth())
        self.buy_ticket_6.setSizePolicy(sizePolicy)
        self.buy_ticket_6.setMinimumSize(QtCore.QSize(600, 250))
        self.buy_ticket_6.setMaximumSize(QtCore.QSize(3424242, 7688768))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buy_ticket_6.setFont(font)
        self.buy_ticket_6.setStyleSheet("QPushButton{\n"
"    border-style:solid;\n"
"border-width:2px;\n"
"    background-color: rgb(222, 222, 222);\n"
"    height:40px;\n"
"    text-align:left;\n"
"    padding-left:10px;\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"    border-top-right-radius:10px;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"\n"
"}\n"
"QWidget{\n"
"border-style:solid;\n"
"border-width:2px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QLabel{\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"}")
        self.buy_ticket_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buy_ticket_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buy_ticket_6.setObjectName("buy_ticket_6")
        self.gridLayout = QtWidgets.QGridLayout(self.buy_ticket_6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 5, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.buy_ticket_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.buy_ticket_6)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.gridLayout.addLayout(self.verticalLayout_5, 2, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.buy_ticket_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.buy_ticket_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 4, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.buy_ticket_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.label_3 = QtWidgets.QLabel(self.buy_ticket_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.gridLayout.addLayout(self.verticalLayout_7, 0, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.buy_ticket_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.buy_ticket_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.gridLayout.addLayout(self.verticalLayout_4, 2, 2, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.buy_ticket_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.label_time_start_buy_ticket_7 = QtWidgets.QLabel(self.buy_ticket_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_time_start_buy_ticket_7.sizePolicy().hasHeightForWidth())
        self.label_time_start_buy_ticket_7.setSizePolicy(sizePolicy)
        self.label_time_start_buy_ticket_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_time_start_buy_ticket_7.setMaximumSize(QtCore.QSize(786868, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_time_start_buy_ticket_7.setFont(font)
        self.label_time_start_buy_ticket_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_time_start_buy_ticket_7.setObjectName("label_time_start_buy_ticket_7")
        self.verticalLayout_8.addWidget(self.label_time_start_buy_ticket_7)
        self.gridLayout.addLayout(self.verticalLayout_8, 4, 1, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_15 = QtWidgets.QLabel(self.buy_ticket_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_10.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.buy_ticket_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_10.addWidget(self.label_16)
        self.gridLayout.addLayout(self.verticalLayout_10, 0, 0, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.buy_ticket_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_9.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.buy_ticket_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_9.addWidget(self.label_14)
        self.gridLayout.addLayout(self.verticalLayout_9, 4, 2, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_17 = QtWidgets.QLabel(self.buy_ticket_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_11.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.buy_ticket_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_11.addWidget(self.label_18)
        self.gridLayout.addLayout(self.verticalLayout_11, 4, 4, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.buy_ticket_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_time_end_buy_ticket_7 = QtWidgets.QLabel(self.buy_ticket_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_time_end_buy_ticket_7.sizePolicy().hasHeightForWidth())
        self.label_time_end_buy_ticket_7.setSizePolicy(sizePolicy)
        self.label_time_end_buy_ticket_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_time_end_buy_ticket_7.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_time_end_buy_ticket_7.setFont(font)
        self.label_time_end_buy_ticket_7.setStyleSheet("")
        self.label_time_end_buy_ticket_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_time_end_buy_ticket_7.setObjectName("label_time_end_buy_ticket_7")
        self.verticalLayout_2.addWidget(self.label_time_end_buy_ticket_7)
        self.gridLayout.addLayout(self.verticalLayout_2, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.buy_ticket_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.label_2 = QtWidgets.QLabel(self.buy_ticket_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.buy_ticket_6, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "Пассажир"))
        self.label_9.setText(_translate("Form", ""))
        self.label_4.setText(_translate("Form", "Место"))
        self.label_5.setText(_translate("Form", ""))
        self.label_10.setText(_translate("Form", "От"))
        self.label_3.setText(_translate("Form", ""))
        self.label_6.setText(_translate("Form", "Класс"))
        self.label_7.setText(_translate("Form", ""))
        self.label_12.setText(_translate("Form", "Время вылета"))
        self.label_time_start_buy_ticket_7.setText(_translate("Form", ""))
        self.label_15.setText(_translate("Form", "Рейс"))
        self.label_16.setText(_translate("Form", ""))
        self.label_13.setText(_translate("Form", "Посадка заканчивается"))
        self.label_14.setText(_translate("Form", ""))
        self.label_17.setText(_translate("Form", "Выход"))
        self.label_18.setText(_translate("Form", ""))
        self.label.setText(_translate("Form", "Дата"))
        self.label_time_end_buy_ticket_7.setText(_translate("Form", ""))
        self.label_11.setText(_translate("Form", "До"))
        self.label_2.setText(_translate("Form", ""))
