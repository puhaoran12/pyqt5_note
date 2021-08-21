import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class HBoxLayoutAlign(QWidget):
    def __init__(self):
        super(HBoxLayoutAlign,self).__init__()
        self.setWindowTitle('水平布局')

        layout=QHBoxLayout()
        layout.addWidget(QLineEdit('1'),6,Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(QPushButton('2'),2,Qt.AlignLeft |Qt.AlignTop)#2表示将布局平分后占2份
        layout.addWidget(QPushButton('3'),1,Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(QPushButton('4'),2, Qt.AlignBottom)
        layout.addWidget(QPushButton('5'),1, Qt.AlignBottom)
        layout.setSpacing(40)#设置按键水平间距
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = HBoxLayoutAlign()
    main.show()
    sys.exit(app.exec_())
