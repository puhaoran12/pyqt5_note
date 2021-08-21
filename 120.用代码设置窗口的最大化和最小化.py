import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#自定义窗口类
class WindowMaxMin(QWidget):
    #构造函数
    def __init__(self):
        #构造函数
        #调用父类构造函数
        super(WindowMaxMin,self).__init__()
        self.resize(300,400)
        self.setWindowTitle('用代码控制窗口的最大化和最小化')
        #括号中三个分别代表了窗口右上角最小化，最大话，关闭。如果设置风格的少了其中一个，窗口右上角相应按钮功能将失效
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        layout=QVBoxLayout()
        maxButton1=QPushButton()
        maxButton1.setText('窗口最大化1')
        maxButton1.clicked.connect(self.maximized1)#使用槽方法
        layout.addWidget(maxButton1)

        maxButton2=QPushButton()
        maxButton2.setText('窗口最大化2')
        maxButton2.clicked.connect(self.showMaximized)#使用了系统提供的最大化方法showMaximized
        layout.addWidget(maxButton2)

        minButton=QPushButton()
        minButton.setText('窗口最小化')
        minButton.clicked.connect(self.showMinimized)
        layout.addWidget(minButton)

        self.setLayout(layout)

    def maximized1(self):
        desktop=QApplication.desktop()#获得桌面
        rect=desktop.availableGeometry()#获得尺寸
        print(rect)
        self.setGeometry(rect)

if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = WindowMaxMin()
        main.show()
        sys.exit(app.exec_())