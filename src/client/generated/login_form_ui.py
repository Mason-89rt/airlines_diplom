# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import resources.res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(724, 578)
        Dialog.setMinimumSize(QtCore.QSize(700, 550))
        Dialog.setMaximumSize(QtCore.QSize(724, 578))
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(400, 0))
        self.frame.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);border:none;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_sign_up = QtWidgets.QWidget()
        self.page_sign_up.setObjectName("page_sign_up")
        self.gridLayout = QtWidgets.QGridLayout(self.page_sign_up)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_sign_up = QtWidgets.QPushButton(self.page_sign_up)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sign_up.sizePolicy().hasHeightForWidth())
        self.btn_sign_up.setSizePolicy(sizePolicy)
        self.btn_sign_up.setMinimumSize(QtCore.QSize(100, 60))
        self.btn_sign_up.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_sign_up.setFont(font)
        self.btn_sign_up.setStyleSheet("\n"
"                                QPushButton {\n"
"                                    color: #0043D4;\n"
"                                    background-color: rgb(255, 255, 255);\n"
"                       border-bottom: 3px solid #0043D4;\n"
"                                }\n"
"                            \n"
"")
        self.btn_sign_up.setCheckable(True)
        self.btn_sign_up.setObjectName("btn_sign_up")
        self.horizontalLayout_2.addWidget(self.btn_sign_up)
        self.btn_sign_in = QtWidgets.QPushButton(self.page_sign_up)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sign_in.sizePolicy().hasHeightForWidth())
        self.btn_sign_in.setSizePolicy(sizePolicy)
        self.btn_sign_in.setMinimumSize(QtCore.QSize(100, 60))
        self.btn_sign_in.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_sign_in.setFont(font)
        self.btn_sign_in.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_sign_in.setCheckable(True)
        self.btn_sign_in.setChecked(False)
        self.btn_sign_in.setObjectName("btn_sign_in")
        self.horizontalLayout_2.addWidget(self.btn_sign_in)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_email = QtWidgets.QLineEdit(self.page_sign_up)
        self.line_email.setMinimumSize(QtCore.QSize(0, 70))
        self.line_email.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.line_email.setFont(font)
        self.line_email.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.line_email.setObjectName("line_email")
        self.gridLayout_2.addWidget(self.line_email, 6, 0, 1, 1)
        self.line_password = QtWidgets.QLineEdit(self.page_sign_up)
        self.line_password.setMinimumSize(QtCore.QSize(0, 70))
        self.line_password.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.line_password.setFont(font)
        self.line_password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.line_password.setText("")
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setObjectName("line_password")
        self.gridLayout_2.addWidget(self.line_password, 5, 0, 1, 1)
        self.line_login = QtWidgets.QLineEdit(self.page_sign_up)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_login.sizePolicy().hasHeightForWidth())
        self.line_login.setSizePolicy(sizePolicy)
        self.line_login.setMinimumSize(QtCore.QSize(0, 70))
        self.line_login.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.line_login.setFont(font)
        self.line_login.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.line_login.setText("")
        self.line_login.setObjectName("line_login")
        self.gridLayout_2.addWidget(self.line_login, 2, 0, 1, 1)
        self.btn_Log_In = QtWidgets.QPushButton(self.page_sign_up)
        self.btn_Log_In.setMinimumSize(QtCore.QSize(0, 70))
        self.btn_Log_In.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_Log_In.setFont(font)
        self.btn_Log_In.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"                                stop:0 rgba(0, 24, 130, 255),\n"
"                                stop:1 rgba(2, 54, 155, 255));\n"
"                border: 2px solid #1E90FF;\n"
"                border-radius: 10px;\n"
"                color: white;\n"
"                padding: 10px;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_Log_In.setObjectName("btn_Log_In")
        self.gridLayout_2.addWidget(self.btn_Log_In, 8, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.page_sign_up)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 149))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("border-image: url(:/icon/icons/1681546293_papik-pro-p-samolet-logotip-vektor-8.png);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_sign_up)
        self.gridLayout_4.addWidget(self.stackedWidget, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(300, 0))
        self.label_2.setStyleSheet("border-image: url(:/icon/icons/gora-fudziyama-ochen-zavorazhivayushhe-vyglyadit.jpg);"
        " border-radius: 90px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_sign_up.setText(_translate("Dialog", "Регистрация"))
        self.btn_sign_in.setText(_translate("Dialog", "Вход"))
        self.line_email.setPlaceholderText(_translate("Dialog", "Почта"))
        self.line_password.setPlaceholderText(_translate("Dialog", "Пароль"))
        self.line_login.setPlaceholderText(_translate("Dialog", "Логин"))
        self.btn_Log_In.setText(_translate("Dialog", "Зарегистрироваться"))