'''
使用线程类（QThread）编写计数器
QTread（类）

def run(self):
    while True:
          self.sleep(1)
          if sec==5:
            break


用到自定义信号
WorkThread（QThread）

'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
sec=0#全局计数，当前计数从0开始
class WorkThread(QThread):#定义线程类（从QThread继承）
    timer=pyqtSignal()#每隔一秒发送一次信号
    end=pyqtSignal()#计数完成后发送一次信号
    def run(self):
        while True:
            self.sleep(1)#休眠一秒(每一秒循环一次)；如果不休眠则变成死循环（括号中单位为秒）
            if sec==5:#当计数时间到5时
                self.end.emit()#发送end信号
                break
            self.timer.emit()#发送timer信号

class Counter(QWidget):
    def __init__(self,parent=None):
        super(Counter,self).__init__(parent)

        self.setWindowTitle('使用线程类（QTread）编写计数器')
        self.resize(300,120)

        layout=QVBoxLayout()
        self.lcdNumber=QLCDNumber()#创建控件(QLCDNumber模拟LED的显示控件)
        layout.addWidget(self.lcdNumber)

        button=QPushButton('开始计数')
        layout.addWidget(button)

        self.workThread=WorkThread()#创建线程实例

        self.workThread.timer.connect(self.countTime)
        self.workThread.end.connect(self.end)
        button.clicked.connect(self.work)

        self.setLayout(layout)

    def countTime(self):
        global sec#用global声明一下sec是全局变量
        sec+=1
        self.lcdNumber.display(sec)

    def end(self):
        QMessageBox.information(self,'消息','计数结束',QMessageBox.Ok)

    def work(self):
        self.workThread.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Counter()
    main.show()
    sys.exit(app.exec_())