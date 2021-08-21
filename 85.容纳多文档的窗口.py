'''
QMdiArea(容纳多文档)
QMdiSubWindow（子窗口）
需要将QMdiSubWindow添加到QMdiArea中
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class MultiWindows(QMainWindow):
    count=0#当前窗口数
    def __init__(self,parent=None):
        super(MultiWindows,self).__init__(parent)
        self.setWindowTitle('容纳多文档的窗口')

        self.mdi=QMdiArea()
        self.setCentralWidget(self.mdi)#将mdi添加到当前布局
        bar=self.menuBar()
        file=bar.addMenu('file')
        file.addAction('new')
        file.addAction('重叠')#多窗口两种放置方式：重叠，平铺
        file.addAction('展开')

        file.triggered.connect(self.windowaction)

    def windowaction(self,q):
        print(q.text())
        if q.text()=='new':
            MultiWindows.count=MultiWindows.count+1#窗口数量变化
            sub=QMdiSubWindow ()#创建子窗口
            sub.setWidget(QTextEdit())#在子窗口在放置控件
            sub.setWindowTitle('子窗口'+str(MultiWindows.count))#设置子窗口的标题
            self.mdi.addSubWindow(sub)#将子窗口添加到QMdiArea中
            sub.show()
        elif q.text()=='重叠':
            self.mdi.cascadeSubWindows()#成叠
        elif q.text()=='展开':
            self.mdi.tileSubWindows()#平铺

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main =MultiWindows()
    main.show()
    sys.exit(app.exec_())