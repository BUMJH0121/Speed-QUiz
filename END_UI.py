# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hadee\OneDrive\바탕 화면\speed_quiz\speed_quiz\end_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1128, 852)
        Dialog.setMinimumSize(QtCore.QSize(1128, 852))
        Dialog.setMaximumSize(QtCore.QSize(1128, 852))
        Dialog.setStyleSheet("")
        self.getsu = QtWidgets.QLineEdit(Dialog)
        self.getsu.setGeometry(QtCore.QRect(40, 120, 1031, 91))
        self.getsu.setAutoFillBackground(False)
        self.getsu.setStyleSheet("font: 36pt \"상상토끼 신비는일곱살\";\n"
"color: rgb(76, 126, 161);\n"
"")
        self.getsu.setText("")
        self.getsu.setFrame(False)
        self.getsu.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.getsu.setDragEnabled(True)
        self.getsu.setReadOnly(True)
        self.getsu.setObjectName("getsu")
        self.score = QtWidgets.QLineEdit(Dialog)
        self.score.setGeometry(QtCore.QRect(40, 250, 1031, 101))
        self.score.setAutoFillBackground(False)
        self.score.setStyleSheet("font: 36pt \"상상토끼 신비는일곱살\";\n"
"color: rgb(76, 126, 161);")
        self.score.setText("")
        self.score.setFrame(False)
        self.score.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.score.setDragEnabled(True)
        self.score.setReadOnly(True)
        self.score.setObjectName("score")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1128, 852))
        self.graphicsView.setMinimumSize(QtCore.QSize(1128, 852))
        self.graphicsView.setMaximumSize(QtCore.QSize(1128, 852))
        self.graphicsView.setStyleSheet("background-image: url(:/newPrefix/background.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.getsu.raise_()
        self.score.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
import background_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())