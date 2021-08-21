import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class DockDemo(QMainWindow):
    def __init__(self,parent=None):
        super(DockDemo,self).__init__(parent)
        self.setWindowTitle('停靠控件（QDockWidget）')

        layout=QHBoxLayout()
        self.items=QDockWidget('Dockable',self)#创建停靠控件窗口
        self.listWidget=QListWidget()
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')

        self.items.setWidget(self.listWidget)
        self.setCentralWidget(QTextEdit())#在大窗口上添加一个文本编辑框
        self.items.setFloating(True)#默认停靠窗口处于悬浮状态；如果删除则默认为停靠状态
        self.addDockWidget(Qt.RightDockWidgetArea,self.items)#把停靠窗口放在大窗口


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main =DockDemo()
    main.show()
    sys.exit(app.exec_())