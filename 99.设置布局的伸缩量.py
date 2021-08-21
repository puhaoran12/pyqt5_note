#伸缩量设置：addStretch
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class HBoxLayoutAlign(QWidget):
    def __init__(self):
        super(HBoxLayoutAlign,self).__init__()
        self.setWindowTitle('设置伸缩量')

        btn1=QPushButton()
        btn2 = QPushButton()
        btn3 = QPushButton()
        btn1.setText('1')
        btn2.setText('2')
        btn3.setText('3')

        layout=QHBoxLayout()
        #伸缩量是设置到布局的，后面添加的控件都是沿用最近的伸缩量
        layout.addStretch(0)#改变成大于0的数对比
        layout.addWidget(btn1)
        layout.addStretch(2)
        layout.addWidget(btn2)#3个按钮默认为右对齐
        layout.addStretch(0)
        layout.addWidget(btn3,1, Qt.AlignBottom)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = HBoxLayoutAlign()
    main.show()
    sys.exit(app.exec_())
