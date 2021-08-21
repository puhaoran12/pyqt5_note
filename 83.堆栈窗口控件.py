'''
堆栈窗口控件：QStackedWidget
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample,self).__init__()
        self.setGeometry(300,50,10,10)
        self.setWindowTitle('堆栈窗口控件：QStackedWidget')

        self.list=QListWidget()
        self.list.insertItem(0,'联系方式')
        self.list.insertItem(1,'个人信息')
        self.list.insertItem(2,'教育程度')
        self.list.setSpacing(100)  #设置按键距离

        self.stack1=QWidget()
        self.stack2=QWidget()
        self.stack3=QWidget()

        self.tab1UI()  # 调用(如果没有则不能使用对应的方法)
        self.tab2UI()#通过UI往每一个QWidget中添加控件
        self.tab3UI()

        self.stack=QStackedWidget()#堆栈窗口控件对象

        self.stack.addWidget(self.stack1)#将小窗口放到大窗口中
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        hbox=QHBoxLayout()#在整个窗口创建布局
        hbox.addWidget(self.list,1)#将列表控件放一侧
        hbox.addWidget(self.stack,5)#将堆栈控件放一侧//这两行中的1，5表示各自区域所对应宽度的比例
        self.setLayout(hbox)

        self.list.currentRowChanged.connect(self.display)
    def tab1UI(self):
        layout = QFormLayout()  # 在tab1中设置布局（小窗口布局）
        layout.addRow('姓名', QLineEdit())
        layout.addRow('住址', QLineEdit())
        self.stack1.setLayout(layout)  # 装载

    def tab2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow(QLabel('性别'), sex)
        layout.addRow('生日', QLineEdit())
        self.stack2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('科目:'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))
        self.stack3.setLayout(layout)

    def display(self,index):
        self.stack.setCurrentIndex(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main =StackedExample()
    main.show()
    sys.exit(app.exec_())