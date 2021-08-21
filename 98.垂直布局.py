import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class VBoxLayout(QWidget):
    def __init__(self):
        super(VBoxLayout,self).__init__()
        self.setWindowTitle('垂直布局')

        layout=QVBoxLayout()
        layout.addWidget(QPushButton('1'))
        layout.addWidget(QPushButton('2'))
        layout.addWidget(QPushButton('3'))
        layout.addWidget(QPushButton('4'))
        layout.addWidget(QPushButton('5'))

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = VBoxLayout()
    main.show()
    sys.exit(app.exec_())
