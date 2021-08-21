from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
class OverrideSlot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Override()覆盖槽函数')
    def keyPressEvent(self, e):#keyPressEvent是系统的槽；系统的槽已经连接上，不需要在进行连接
        if e.key()==Qt.Key_Escape:
            self.close()
        elif e.key()==Qt.Key_Alt:
            self.setWindowTitle('按下Alt键')

if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = OverrideSlot()
        main.show()
        sys.exit(app.exec_())