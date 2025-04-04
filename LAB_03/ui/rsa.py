# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os 
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "C:/Users/Administrator/AppData/Local/Programs/Python/Python312/Lib/site-packages/PyQt5/Qt5/plugins/platforms"

class Ui_RSACipher(object):
    def setupUi(self, RSACipher):
        RSACipher.setObjectName("RSACipher")
        RSACipher.resize(801, 601)
        self.centralwidget = QtWidgets.QWidget( )
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 321, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 260, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 260, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btn_GenerateKey = QtWidgets.QPushButton(self.centralwidget)
        self.btn_GenerateKey.setGeometry(QtCore.QRect(520, 50, 91, 31))
        self.btn_GenerateKey.setObjectName("btn_GenerateKey")
        self.btn_Encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Encrypt.setGeometry(QtCore.QRect(60, 370, 91, 31))
        self.btn_Encrypt.setObjectName("btn_Encrypt")
        self.btn_Decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Decrypt.setGeometry(QtCore.QRect(200, 370, 91, 31))
        self.btn_Decrypt.setObjectName("btn_Decrypt")
        self.btn_Sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Sign.setGeometry(QtCore.QRect(440, 370, 91, 31))
        self.btn_Sign.setObjectName("btn_Sign")
        self.btn_Verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Verify.setGeometry(QtCore.QRect(600, 370, 91, 31))
        self.btn_Verify.setObjectName("btn_Verify")
        self.txt_PlainText = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_PlainText.setGeometry(QtCore.QRect(200, 130, 201, 51))
        self.txt_PlainText.setObjectName("txt_PlainText")
        self.txt_CipherText = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_CipherText.setGeometry(QtCore.QRect(200, 250, 201, 51))
        self.txt_CipherText.setObjectName("txt_CipherText")
        self.txt_Informatin = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_Informatin.setGeometry(QtCore.QRect(560, 130, 201, 51))
        self.txt_Informatin.setObjectName("txt_Informatin")
        self.txt_Signature = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_Signature.setGeometry(QtCore.QRect(560, 250, 201, 51))
        self.txt_Signature.setObjectName("txt_Signature")
        RSACipher.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RSACipher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        RSACipher.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RSACipher)
        self.statusbar.setObjectName("statusbar")
        RSACipher.setStatusBar(self.statusbar)

        self.retranslateUi(RSACipher)
        QtCore.QMetaObject.connectSlotsByName(RSACipher)

    def retranslateUi(self, RSACipher):
        _translate = QtCore.QCoreApplication.translate
        RSACipher.setWindowTitle(_translate("RSACipher", "RSACipher"))
        self.label.setText(_translate("RSACipher", "RSA CIPHER"))
        self.label_2.setText(_translate("RSACipher", "Plain Text:"))
        self.label_3.setText(_translate("RSACipher", "Cipher Text:"))
        self.label_4.setText(_translate("RSACipher", "Information:"))
        self.label_5.setText(_translate("RSACipher", "Signature:"))
        self.btn_GenerateKey.setText(_translate("RSACipher", "Generate Keys"))
        self.btn_Encrypt.setText(_translate("RSACipher", "Encrypt"))
        self.btn_Decrypt.setText(_translate("RSACipher", "Decrypt"))
        self.btn_Sign.setText(_translate("RSACipher", "Sign"))
        self.btn_Verify.setText(_translate("RSACipher", "Verify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RSACipher = QtWidgets.QMainWindow()
    ui = Ui_RSACipher()
    ui.setupUi(RSACipher)
    RSACipher.show()
    sys.exit(app.exec_())
