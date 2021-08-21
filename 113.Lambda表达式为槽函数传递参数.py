'''
使用Lambda表达式为槽函数传递参数

Lambda表达式：匿名函数，也就是没有名字的函数

fun=lambda :print('hello world')
fun()
fun1=lambda x,y:print(x,y)
fun1('a','b')
'''
from PyQt5.QtWidgets import *
import sys

class LambdaSlotArg(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('使用Lambda表达式为槽函数传递参数')

        button1=QPushButton('按钮1')
        button2=QPushButton('按钮2')
        x=10
        button1.clicked.connect(lambda :self.onButtonClick(x,20))
        button2.clicked.connect(lambda: self.onButtonClick(40, -20))
        button1.clicked.connect(lambda:QMessageBox.information(self,'结果：','单击了button1'))#顺序

        layout=QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        mainFrame=QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onButtonClick(self,m,n):
        print('m+n=',m+n)
        QMessageBox.information(self,'结果：',str(m+n),)#弹出对话框，标题为  结果：  显示：str（m+n）

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LambdaSlotArg()
    main.show()
    sys.exit(app.exec_())