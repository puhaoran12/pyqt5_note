'''
使用打印机
'''
from PyQt5 import QtGui,QtWidgets,QtPrintSupport
from PyQt5.QtWidgets import *
import sys

class PrintSupport(QMainWindow):
    def __init__(self):
        super(PrintSupport,self).__init__()
        self.setGeometry(500,200,300,300)
        layout=QVBoxLayout()
        self.button=QPushButton('打印QTextEdit控件中的内容')
        self.button.setGeometry(20,20,60,30)#控件的位置，尺寸
        self.editor=QTextEdit('默认文本',self)
        self.editor.setGeometry(20,60,260,200)



        self.button.clicked.connect(self.print)

    def print(self):
        printer=QtPrintSupport.QPrinter()

        painter=QtGui.QPainter()
        #将绘制的目标重定向到打印机
        painter.begin(printer)
        screen=self.editor.grab()
        painter.drawPixmap(10,10,screen)
        painter.end()
        print('print')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PrintSupport()
    main.show()
    sys.exit(app.exec_())