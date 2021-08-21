'''
QApplicatioin.setStyle()
'''
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

print(QStyleFactory.keys())#显示所有风格


class WindowStyle(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('设置窗口风格')
        layout=QHBoxLayout()
        self.styleLabel=QLabel('设置窗口风格：')
        self.styleComboBox=QComboBox()#创建下拉列表
        self.styleComboBox.addItems(QStyleFactory.keys())

        #获取当前窗口风格
        print(QApplication.style().objectName())#objectName()作用是返回QStyleFactory.keys()中的内容之一
        index=self.styleComboBox.findText(QApplication.style().objectName(),QtCore.Qt.MatchFixedString)

        self.styleComboBox.setCurrentIndex(index)

        self.styleComboBox.activated[str].connect(self.handleStyleChanged)#改变styleComboBox来改变风格
        layout.addWidget(self.styleLabel)
        layout.addWidget(self.styleComboBox)
        self.setLayout(layout)
    def handleStyleChanged(self,style):#style就是styleComboBox中的每一个值
        QApplication.setStyle(style)



if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = WindowStyle()
        main.show()
        sys.exit(app.exec_())