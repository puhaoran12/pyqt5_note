'''
A.setDragEnabled(True):A可拖动
B.setAcceptDrops(True):B控件能接收其他控件拖过来的动作
B需要两个事件
1.dragEnterEvent：将A拖到B触发
2.drogEvent:在B的区域放下A触发
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyComboBox(QComboBox):
    def __init__(self):
        super(MyComboBox,self).__init__()
        self.setAcceptDrops(True)#接收其他控件
    def dragEnterEvent(self,e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()
    def dropEvent(self, e):
        self.addItem(e.mimeData().text())

class DrapDrogDemo(QWidget):
    def __init__(self):
        super(DrapDrogDemo,self).__init__()
        formLayout=QFormLayout()
        formLayout.addRow(QLabel('请将左边的文本拖拽到右边的下拉列表中'))
        lineEdit=QLineEdit()
        lineEdit.setDragEnabled(True)#让QlineEdit可拖动

        combo=MyComboBox()#
        formLayout.addRow(lineEdit,combo)
        self.setLayout(formLayout)
        self.setWindowTitle('拖拽案例')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrapDrogDemo()
    main.show()
    sys.exit(app.exec_())
