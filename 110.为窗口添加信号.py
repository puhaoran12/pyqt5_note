from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
class WinSignal(QWidget):
    button_clicked_signal=pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('为窗口添加信号')
        self.resize(300,100)

        btn=QPushButton('关闭窗口',self)#
        btn.clicked.connect(self.btn_clicked)#将按钮和方法btn_clicked关联（将button_clicked_signal信号发送）
        self.button_clicked_signal.connect(self.btn_close)#将信号和方法关联

    def btn_clicked(self):
        self.button_clicked_signal.emit()#将信号发送

    def btn_close(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WinSignal()
    main.show()
    sys.exit(app.exec_())