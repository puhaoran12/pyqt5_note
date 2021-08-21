from PyQt5.QtCore import QThread,pyqtSignal,QDateTime
from PyQt5.QtWidgets import QApplication,QDialog,QLineEdit
import time
import sys
class BackendThread(QThread):
    update_date=pyqtSignal(str)

    def run(self):
        while True:
            data=QDateTime.currentDateTime()
            currenTime=data.toString('yyyy-MM-dd hh:mm:ss')
            self.update_date.emit(str(currenTime))
            time.sleep(1)

class ThreadUpdateUI(QDialog):#创建窗口
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('多线程更新UI数据')
        self.resize(400,300)
        self.input=QLineEdit(self)
        self.input.resize(400,100)

        self.initUI()
    def initUI(self):
        self.backend=BackendThread()
        self.backend.update_date.connect(self.handleDisplay)

        self.backend.start()

    def handleDisplay(self,data):
        self.input.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ThreadUpdateUI()
    main.show()
    sys.exit(app.exec_())