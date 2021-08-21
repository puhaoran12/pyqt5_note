

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QColorDialogdemo(QWidget):
    def __init__(self):
        super(QColorDialogdemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color Dialog例子')
        layout=QVBoxLayout()
        self.colorButton=QPushButton('请选择文字颜色')
        self.colorButton.clicked.connect(self.getColor)
        layout.addWidget(self.colorButton)
        #设置背景色
        self.colorButton1 = QPushButton('请背景选择颜色')
        self.colorButton1.clicked.connect(self.getBJColor)
        layout.addWidget(self.colorButton1)

        self.colorLabel=QLabel('hello,测试颜色例子')
        layout.addWidget(self.colorLabel)

        self.setLayout(layout)
    def getColor(self):
        color=QColorDialog.getColor()
        p=QPalette()
        p.setColor(QPalette.WindowText,color)
        self.colorLabel.setPalette(p)
    def getBJColor(self):
        color=QColorDialog.getColor()
        p=QPalette()
        p.setColor(QPalette.Window,color)
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setPalette(p)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogdemo()
    main.show()
    sys.exit(app.exec_())