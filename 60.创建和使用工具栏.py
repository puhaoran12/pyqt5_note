'''
创建和使用工具栏
工具栏默认按钮：只显示图标，将文本作为悬停提示展示

工具栏按钮有3种显示状态
1.只显示图标
2.只显示文本
3.同时显示文本和图标
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Toolbar(QMainWindow):
    def __init__(self):
        super(Toolbar,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('工具栏例子')
        self.resize(300,200)

        tb1=self.addToolBar('file')#创建工具栏
        new=QAction(QIcon('book1.png'), 'new', self)#创建工具栏按钮   QIcon是图标
        tb1.addAction(new)#给工具栏上添加按钮

        open=QAction(QIcon(),'open',self)
        tb1.addAction(open)

        save=QAction(QIcon(),'save',self)
        tb1.addAction(save)

        tb1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)#如果没有该代码，则只显示图标（控制工具栏相关属性）
        #如果需要有的只显示文本，有的只显示图标，则创建多个工具栏；一个工具栏只能有一个显示方式

        tb1.actionTriggered.connect(self.toolbtnpressed)

    def toolbtnpressed(self,a):
        print('按下的工具栏按钮是',a.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Toolbar()
    main.show()
    sys.exit(app.exec_())