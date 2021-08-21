'''
句对布局：通过坐标X，Y控制组件位置的(move方法)
'''
import sys,math
from PyQt5.QtWidgets import *
class AbsoluteLayout(QWidget):
    def __init__(self):
        super(AbsoluteLayout,self).__init__()
        self.setWindowTitle('绝对布局')

        self.label1=QLabel('欢迎',self)
        self.label1.move(15,20)

        self.label2=QLabel('学习',self)
        self.label2.move(35,40)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AbsoluteLayout()
    main.show()
    sys.exit(app.exec_())