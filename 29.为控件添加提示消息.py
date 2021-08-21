import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget,QToolTip
from PyQt5.QtGui import QFont


class TooltipFrom(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('Sanserif',12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(400,400,400,400)
        self.setWindowTitle('设置控件提示消息')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipFrom()
    main.show()
    sys.exit(app.exec_())

