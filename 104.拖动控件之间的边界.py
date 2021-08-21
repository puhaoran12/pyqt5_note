'''
拖动控件之间的边界：QSplitter

'''
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class Splitter(QWidget):
    def __init__(self):
        super(Splitter,self).__init__()
        self.initUI()
    def initUI(self):
        layout=QHBoxLayout(self)
        self.setWindowTitle('QSplitter例子')
        self.setGeometry(300,300,300,200)

        topleft=QFrame()#创建框架
        topleft.setFrameShape(QFrame.StyledPanel)

        bottom=QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1=QSplitter(Qt.Horizontal)#水平拖动
        textedit=QTextEdit()#创建文本框
        splitter1.addWidget(topleft)#将框架放到水平拖动上（Frame不可输入文字）
        splitter1.addWidget(textedit)#将文本框放到谁平拖动上（因为topleft在textedit之前，所以toleft在左边），左右结构
        splitter1.setSizes([100,200])#设置左右两个框的宽度

        splitter2 = QSplitter(Qt.Vertical)#上下拖动
        splitter2.addWidget(splitter1)#上下结构
        splitter2.addWidget(bottom)
        splitter2.setSizes([150,150])

        layout.addWidget(splitter2)#将总的放到布局中
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Splitter()
    main.show()
    sys.exit(app.exec_())