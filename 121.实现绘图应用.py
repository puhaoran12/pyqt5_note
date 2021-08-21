'''
项目实战：实现绘图应用
需要解决三个核心问题：
1.如何让绘图

在paintEvent方法中绘图，通过调用update方法触发paintEvent的调用

2.在那里绘图

在百色背景的QPixmap对象中绘图

3.怎样通过移动鼠标进行绘图

鼠标有三个事件：
1.鼠标按下
2.鼠标移动
3.鼠标抬起

'''
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QPixmap
from PyQt5.QtCore import Qt,QPoint

class Drawing(QWidget):
    def __init__(self,parent=None):
        super(Drawing,self).__init__(parent)
        self.setWindowTitle('绘图应用')
        self.pix=QPixmap()
        self.lastPoint=QPoint()
        self.endPoint=QPoint()
        self.initUI()

    def initUI(self):
        self.resize(600,600)
        #画布大小为400*400，背景为白色
        self.pix=QPixmap(600,600)
        self.pix.fill(Qt.white)

    def paintEvent(self,event):
        pp=QPainter(self.pix)
        #根据鼠标前后两个位置绘制直线
        pp.drawLine(self.lastPoint,self.endPoint)
        #让前一个坐标值等于后一个坐标值
        #这样就能实现画出连续的线
        self.lastPoint=self.endPoint
        painter=QPainter(self)
        painter.drawPixmap(0,0,self.pix)

    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton:
            self.lastPoint=event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.endPoint=event.pos()
            self.update()

    def mouseReleaseEvent(self,event):
        #鼠标左键释放
        if event.button()==Qt.LeftButton:
            self.endPoint=event.pos()
            #进行重新绘制
            self.update()

if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = Drawing()
        main.show()
        sys.exit(app.exec_())