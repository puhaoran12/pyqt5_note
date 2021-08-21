from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *
class WindowPattern(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500,260)
        self.setWindowTitle('设置窗口样式')

        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint)
        self.setObjectName('MainWindow')
        self.setStyleSheet('#MainWindow{border-image:url(book1.jpg);}')

if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = WindowPattern()
        main.show()
        sys.exit(app.exec_())