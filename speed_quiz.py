
import sys
import os
import time
import START_UI
import SPEED_QUIZ_UI
import END_UI

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

with open("title.txt", "r", encoding = 'utf-8') as t:
    Title = t.readlines()

with open("answer.txt", "r", encoding = 'utf-8') as ans:
    answer = ans.readlines()

def read_question(a):
    with open("{0}.txt".format(a), "r", encoding = 'utf-8') as f:
        return f.read()

total_score = 0
correct_num = 0
question_num = 10

class S_Dialog(QDialog, START_UI.Ui_Dialog):
    def __init__(self):
        super().__init__()
        QDialog.__init__(self, None)
        self.setupUi(self)

        self.start.clicked.connect(self.Next)
        
    def Next(self):
        self.close()
        self.main = Q_Dialog()
        self.main.show()


class Q_Dialog(QDialog, SPEED_QUIZ_UI.Ui_Dialog):
    def __init__(self):
        super().__init__()
        QDialog.__init__(self, None)
        self.setupUi(self)

        self.count = 0
        self.i = 1
        self.question_num = 10
        self.title.setText(''.join(Title))
        if self.i <= question_num:
            self.question.setText(''.join(read_question(self.i)))
        self.answer.returnPressed.connect(self.lineeditTextFunction)
        self.timerVar = QTimer(self)
        self.timerVar.start()
        self.timerVar.setInterval(1000)
        self.timerVar.timeout.connect(self.times)

        self.p.setStyleSheet('image:url(./답.png);')

    def lineeditTextFunction(self):
        text = self.answer.text()
        if text == answer[self.i-1][:-1]:
            global total_score
            global correct_num
            total_score += 100/question_num
            correct_num += 1
        self.answer.clear()
        self.i = self.i+1
        self.count = 0
        if self.i > question_num:
            self.close()
            self.main = E_Dialog()
            self.main.show()
        else:
            self.question.setText(''.join(read_question(self.i)))

    def times(self):
        if 30 - self.count == 0:
            self.lineeditTextFunction()
        self.count = self.count+1
        self.time.setText(str(30 - self.count))
        

class E_Dialog(QDialog, END_UI.Ui_Dialog):
    def __init__(self):
        super().__init__()
        QDialog.__init__(self, None)
        self.setupUi(self)

        self.getsu.setText("{0}문제 맞추셨습니다!".format(correct_num))
        self.score.setText("{0}점!".format(total_score))


app = QApplication(sys.argv)
myWindow = S_Dialog()
myWindow.show()
app.exec_()
