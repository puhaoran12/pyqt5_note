'''
绘制各种图形
弧
圆形
矩形
多边形
'''
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine,self).__init__()
        self.resize(300,600)
        self.setWindowTitle('绘制各种图形')
    def paintEvent(self,event):
        qp=QPainter()
        qp.begin(self)

        qp.setPen(Qt.blue)
        #绘制弧
        rect=QRect(0,10,100,100)#左上角左边，宽度，高度(绘图区域范围)
        #alen:1个alen等于1/16度
        qp.drawArc(rect,0,50*16)
        #通过弧绘制圆
        qp.setPen(Qt.red)
        qp.drawArc(120,10,100,100,0,360*16)#左上角左边，宽度，高度（前三项为绘图区域），起始度数，终止角度
        #绘制带弦的弧
        qp.drawChord(10,120,100,100,12,130*16)
        #绘制扇形
        qp.drawPie(10,240,100,100,12,130*16)
        #绘制椭圆
        qp.drawEllipse(120,120,150,100)
        #绘制多边形:需绘制多个点
        point1=QPoint(140,380)
        point2 = QPoint(270, 420)
        point3 = QPoint(290, 512)
        point4 = QPoint(290, 588)
        point5 = QPoint(200, 533)
        #创建多边形对象
        polygon=QPolygon([point1,point2,point3,point4,point5])
        qp.drawPolygon(polygon)

        #绘制图像
        image=QImage('book1.png')
        rect=QRect(10,400,image.width()/10,image.height()/10)
        qp.drawImage(rect,image)


        qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawMultiLine()
    main.show()
    sys.exit(app.exec_())
