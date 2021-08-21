from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
class WindowPattern(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500,260)
        self.setWindowTitle('设置窗口样式')
        #该窗口没有最小化和关闭窗口按钮。加上| Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint就有了
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint )#设置窗口样式
        self.setObjectName('MainWindow')#设置窗口id：MainWindow
        self.setStyleSheet('#MainWindow{border-image:url(QQ.png)}')#设置背景图（#MainWindow引用窗口id）

        btn=QPushButton(self)
        btn.setText('关闭窗口')

        btn.clicked.connect(self.close)

if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = WindowPattern()
        main.show()
        sys.exit(app.exec_())