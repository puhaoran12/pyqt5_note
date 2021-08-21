import sys,math
from PyQt5.QtWidgets import *
class HBoxLayout(QWidget):
    def __init__(self):
        super(HBoxLayout,self).__init__()
        self.setWindowTitle('水平布局')

        layout=QHBoxLayout()
        layout.addWidget(QPushButton('1'))
        layout.addWidget(QPushButton('2'))
        layout.addWidget(QPushButton('3'))
        layout.addWidget(QPushButton('4'))
        layout.addWidget(QPushButton('5'))
        layout.setSpacing(40)#设置按键水平间距
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = HBoxLayout()
    main.show()
    sys.exit(app.exec_())
