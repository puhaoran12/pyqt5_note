from PyQt5.QtWidgets import *
import sys
class SignalSlotDemo(QWidget):
    def __init__(self):
        super(SignalSlotDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,500,400)
        self.setWindowTitle('信号(signal)与槽(slot)')
        self.btn=QPushButton('我的按钮',self)#没有创建布局，按钮直接添加到窗口上
        self.btn.clicked.connect(self.onClicked)

    def onClicked(self):
        self.btn.setText('信号已发出')
        self.btn.setStyleSheet('QPushButton(max-width:200px;min-width:200px)')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = SignalSlotDemo()
    main.show()
    sys.exit(app.exec_())