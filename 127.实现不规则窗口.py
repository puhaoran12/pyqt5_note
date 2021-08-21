'''
通过mask实现异性窗口
需要一张透明的png图，透明部分被扣出，形成一个非矩形的区域
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class AbnormityWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('异性窗口')
        self.pix=QBitmap('./book1.png')
        self.resize(self.pix.size())
        self.setMask(self.pix)
    def painEvent(self,event):
        painter=QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),QPixmap('./screen.jpg'))

if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = AbnormityWindow()
        main.show()
        sys.exit(app.exec_())