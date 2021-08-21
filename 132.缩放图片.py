'''
缩放图片
QImage.scaled
'''
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtCore import Qt
import sys
class ScaleImage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('图片大小放缩例子')
        filename='./zhuomian.png'
        img=QImage(filename)#创建img
        label1=QLabel(self)
        label1.setFixedWidth(600)
        label1.setFixedHeight(600)
        #设置比例：图像大小跟label大小一样
        result=img.scaled(label1.width(),label1.height(),Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        label1.setPixmap(QPixmap.fromImage(result))

        layout=QVBoxLayout()
        layout.addWidget(label1)

        self.setLayout(layout)

if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = ScaleImage()
        main.show()
        sys.exit(app.exec_())
