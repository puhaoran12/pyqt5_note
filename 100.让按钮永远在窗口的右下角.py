import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class RightBottonBotton(QWidget):
    def __init__(self):
        super(RightBottonBotton,self).__init__()
        self.setWindowTitle('让按钮永远在右下角')
        self.resize(400,300)

        okbotton=QPushButton('确定')
        cancelbotton=QPushButton('取消')

        layout1=QHBoxLayout()
        layout1.addStretch(0)
        layout1.addWidget(okbotton)
        layout1.addWidget(cancelbotton)



        layout=QVBoxLayout()
        btn1=QPushButton('1')
        btn2=QPushButton('2')
        btn3=QPushButton('3')
        layout.addStretch(1)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        layout.addLayout(layout1)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = RightBottonBotton()
    main.show()
    sys.exit(app.exec_())
